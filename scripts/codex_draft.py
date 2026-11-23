r"""Codex draft run: four subject lanes write first drafts of section plans, plan data and days, grade by grade.

    python -X utf8 scripts/codex_draft.py setup        make the queues (once; run in the draft checkout)
    python -X utf8 scripts/codex_draft.py run          run every lane until done, STOP, or each lane stops itself
    python -X utf8 scripts/codex_draft.py run --dry    walk the queues and print what would run; start nothing
    python -X utf8 scripts/codex_draft.py status       one line per lane: done, next, stopped

Cory, 2026-11-22: Codex writes all the drafts with its weekly allocation; Claude reviews much later. Each subject is a
lane that climbs its grades in order (a grade's section plans, then per unit its plan data and days, then the next
grade, the order scripts/coursegen.py writes); the four lanes run at the same time, each one job at a time.

It runs in its own checkout, S:\CurioClass-draft on branch draft/codex, so the main folder and other sessions are never
touched. Only the drafting jobs of each coursegen queue run (SEC, DATA, DAY, CHECKS, and for ELA TEXT and TEXT2); the
reads, key reads, fixes, cleanups and retool stops are skipped, and docs/pipeline/kit/draft-preamble.txt tells each job
so. The runner does the lead's mechanical steps itself: the ledger gate before each day job, and for ELA the text
merges into data/plans/ela-texts.csv and the section skeleton rebuild.

Every job: one fresh `codex exec` (workspace-write, web search on, JSON events kept). A session silent for 20 minutes
is resumed once with "that command hung"; a dropped session with no last message is resumed once with "carry on";
3 hours is the cap. After the job: for day and check jobs the fast lesson gate (scripts/lesson_course.py) on its days;
then a commit of everything changed (under one lock, so lanes never commit at the same time) and a push of the branch.

Stops (no Claude tokens are used; everything is automatic):
- a usage or rate limit message pauses every lane for 30 minutes, then the same job is tried again (never counted as
  a failure); the run never ends on a limit, so it drains the week and picks up again when the window resets;
- a lane stops itself after 3 failed jobs in a row (codex error, no last message, or a closed ledger gate), or when a
  grade's lesson gate failures pile up: more than 4 plus one for every 4 days drafted in that grade;
- the file _draft\STOP stops every lane gently (running jobs finish); _draft\STOP-<lane> stops one lane.
A per-job note in _draft
otes\<lane>-<job>.txt is added to that job's prompt; a job listed in done.txt never runs.
Restarting picks up where it stopped (done jobs are in _draft\done.txt; a stopped lane is in _draft\stopped.txt;
delete its line to let it go on).

Logs, all in S:\CurioClass-draft\_draft\ (not committed): run.log (what happened), usage.csv (one row per job: lane,
job, kind, course, detail, result, minutes, tokens in, cached, out, reasoning, gate failures), jobs\<lane>\<n>*.jsonl
and *-last.md (each session's events and last message).
"""
import csv
import ctypes
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAFT = ROOT / '_draft'
QUEUES = DRAFT / 'queues'
JOBS = DRAFT / 'jobs'
STOP = DRAFT / 'STOP'
LANES = {   # subject: courses in grade order (Cory 2026-11-22; math-grade-4 is another session's course)
    'math': ['math-kindergarten', 'math-grade-1', 'math-grade-2', 'math-grade-3'],
    'social-studies': ['social-studies-grade-4', 'social-studies-grade-5', 'world-geography-and-ancient-civilizations-i'],
    'ela': ['english-language-arts-grade-4', 'english-language-arts-grade-5'],
    'science': ['science-grade-4', 'science-grade-5', 'science-grade-6'],
}
KINDS = {'SEC', 'DATA', 'DAY', 'CHECKS', 'TEXT', 'TEXT2'}
STALL = 20 * 60
TIMEBOX = 3 * 3600
STAGGER = 120          # seconds between lane starts (two sandboxes starting at once failed their handshake, 2026-11-04)
LIMIT_PAUSE = 30 * 60
MAX_FAILS = 3
LIMIT_WORDS = ('usage limit', 'rate limit', 'rate_limit', 'quota', 'insufficient_quota', 'try again at', 'upgrade to')
HUNG = "That command hung, so I stopped it. Carry on with the next step and finish the job and its last message."
CARRY = "Your connection dropped. Carry on from where you were, finish the job, and send the last message the job asks for."
LOCK = threading.Lock()        # git and shared-file steps
LOGL = threading.Lock()
PAUSE_UNTIL = [0.0]            # a usage limit pauses every lane until this time
REPO = re.compile(r'S:[\\/]CurioClass(?![\w-])')
LESSONGATE = re.compile(r'python -X utf8 scripts/lesson\.py check 2>&1 \| grep "courses/([a-z0-9-]+)/"')


def now():
    return dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def log(line):
    with LOGL:
        DRAFT.mkdir(exist_ok=True)
        with open(DRAFT / 'run.log', 'a', encoding='utf-8') as f:
            f.write('%s %s\n' % (now(), line))
        print(now(), line, flush=True)


def keep_awake(on=True):
    try:
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | (0x00000001 if on else 0))
    except Exception:
        pass


def codex_exe():
    exe = shutil.which('codex') or shutil.which('codex.cmd')
    npm = Path(os.environ.get('APPDATA', str(Path.home() / 'AppData' / 'Roaming'))) / 'npm' / 'codex.cmd'
    if not exe and npm.exists():   # a scheduled task's PATH can miss the npm folder (2026-11-04)
        exe = str(npm)
    if not exe:
        local = Path(os.environ.get('LOCALAPPDATA', str(Path.home() / 'AppData' / 'Local')))
        hits = sorted(local.glob('Packages/Claude_*/LocalCache/Roaming/npm/codex.cmd'))
        exe = str(hits[0]) if hits else None
    if not exe:
        sys.exit('codex is not on PATH')
    return exe


def py(*args, timeout=900):
    r = subprocess.run([sys.executable, '-X', 'utf8', *args], cwd=ROOT, capture_output=True, text=True,
                       encoding='utf-8', errors='replace', timeout=timeout)
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def git(*args, check=False):
    r = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if check and r.returncode:
        raise RuntimeError('git %s: %s' % (' '.join(args), r.stderr.strip()))
    return r.returncode, (r.stdout or '') + (r.stderr or '')


# ---------------------------------------------------------------- queues

def setup():
    if ROOT.name != 'CurioClass-draft':
        sys.exit('setup runs in the draft checkout (S:\\CurioClass-draft), not %s' % ROOT)
    for subj, courses in LANES.items():
        out = QUEUES / subj
        if (out / 'queue.txt').exists():
            print('queue exists:', out / 'queue.txt')
            continue
        args = ['scripts/coursegen.py', subj, *courses, '--out', str(out)]
        if subj == 'ela':
            args.append('--texts')
        code, text = py(*args)
        print(subj, 'coursegen exit', code)
        print(text[-600:])


def load_queue(subj):
    """The lane's steps in order: ('job', num, kind, course, detail, file, gate) or ('merge'|'merge-new', course)."""
    steps, gate = [], None
    for line in (QUEUES / subj / 'queue.txt').read_text(encoding='utf-8').splitlines():
        if line.startswith('#') or '|' not in line:
            continue
        num, kind, course, detail, f = [x.strip() for x in line.split('|', 4)]
        if kind == 'GATE':
            gate = f
            continue
        if kind == 'LEAD' and detail.startswith('MERGE texts-out/'):
            steps.append(('merge-new' if '-new.csv' in detail else 'merge', course))
        elif kind in KINDS:
            steps.append(('job', num, kind, course, detail, f, gate if kind in ('DAY', 'CHECKS') else None))
        gate = None
    return steps


def done_set():
    p = DRAFT / 'done.txt'
    return set(p.read_text(encoding='utf-8').split()) if p.exists() else set()


def mark_done(key):
    with LOGL:
        with open(DRAFT / 'done.txt', 'a', encoding='utf-8') as f:
            f.write(key + '\n')


def stopped_lanes():
    p = DRAFT / 'stopped.txt'
    return {ln.split()[0] for ln in p.read_text(encoding='utf-8').splitlines() if ln.strip()} if p.exists() else set()


def stop_lane(subj, why):
    with LOGL:
        with open(DRAFT / 'stopped.txt', 'a', encoding='utf-8') as f:
            f.write('%s %s %s\n' % (subj, now(), why))
    log('LANE STOPPED %s: %s' % (subj, why))


# ---------------------------------------------------------------- ELA text merges (the lead's step, done here)

TEXTS = ROOT / 'data' / 'plans' / 'ela-texts.csv'
TEXTS_OUT = ROOT / '_scratch' / 'l87' / 'texts-out'


def merge_texts(course, new):
    """merge: texts-out/<course>-u<N>.csv onto existing rows; merge-new: <course>-u<N>-new.csv rows added or updated."""
    raw = TEXTS.read_bytes()
    nl = '\r\n' if b'\r\n' in raw else '\n'
    with open(TEXTS, encoding='utf-8', newline='') as f:
        rd = csv.DictReader(f)
        cols, rows = rd.fieldnames, list(rd)
    pat = course + ('-u*-new.csv' if new else '-u*.csv')
    n = 0
    for side in sorted(TEXTS_OUT.glob(pat)):
        if not new and side.name.endswith('-new.csv'):
            continue
        for s in csv.DictReader(open(side, encoding='utf-8', newline='')):
            hit = [r for r in rows if r['course'] == course and r['text_id'] == s.get('text_id')]
            if hit:
                r = hit[0]
                for k, v in s.items():
                    if k in cols and k not in ('text_id', 'course') and v:
                        r[k] = v
                if s.get('todo') == '':
                    r['todo'] = ''
                n += 1
            elif new and s.get('text_id'):
                row = {c: s.get(c, '') or '' for c in cols}
                at = [i for i, r in enumerate(rows) if r['course'] == course and r.get('unit') == s.get('unit')] or \
                     [i for i, r in enumerate(rows) if r['course'] == course] or [len(rows) - 1]
                rows.insert(at[-1] + 1, row)
                n += 1
            else:
                log('merge %s: no row for %s (from %s)' % (course, s.get('text_id'), side.name))
    tmp = TEXTS.with_suffix('.csv.tmp')
    with open(tmp, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, cols, lineterminator=nl)
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, TEXTS)
    code, out = py('scripts/section_skeleton.py', course, 'all', '--force')
    log('merge%s %s: %d rows; skeletons rebuilt (exit %d)' % ('-new' if new else '', course, n, code))


# ---------------------------------------------------------------- one job

class Run:
    def __init__(self, subj, num, kind, course, detail, prompt):
        self.subj, self.num, self.kind, self.course, self.detail = subj, num, kind, course, detail
        self.prompt = prompt
        self.stem = JOBS / subj / ('%s-%s-%s' % (num, kind.lower(), course))
        self.stem.parent.mkdir(parents=True, exist_ok=True)
        self.thread = None
        self.usage = [0, 0, 0, 0]
        self.limit = False
        self.last = ''

    def _session(self, args, prompt, suffix):
        events = Path('%s%s.jsonl' % (self.stem, suffix))
        last = Path('%s%s-last.md' % (self.stem, suffix))
        if last.exists():
            last.unlink()
        with open(events, 'w', encoding='utf-8') as out:
            p = subprocess.Popen([codex_exe(), *args, '--json', '-o', str(last), '-'], cwd=ROOT, stdin=subprocess.PIPE,
                                 stdout=out, stderr=subprocess.STDOUT, text=True, encoding='utf-8',
                                 creationflags=getattr(subprocess, 'CREATE_NEW_PROCESS_GROUP', 0))
            p.stdin.write(prompt)
            p.stdin.close()
            seen, grew, started, stalled = 0, time.time(), time.time(), False
            while p.poll() is None:
                time.sleep(15)
                try:
                    size = events.stat().st_size
                except OSError:
                    size = seen
                if size != seen:
                    seen, grew = size, time.time()
                if time.time() - grew > STALL or time.time() - self.t0 > TIMEBOX:
                    stalled = True
                    subprocess.run(['taskkill', '/T', '/F', '/PID', str(p.pid)], capture_output=True)
                    break
        for line in events.read_text(encoding='utf-8', errors='replace').splitlines():
            try:
                ev = json.loads(line)
            except ValueError:
                ev = {}
            t = ev.get('type')
            if t == 'thread.started' and not self.thread:
                self.thread = ev.get('thread_id')
            if t == 'turn.completed':
                u = ev.get('usage') or {}
                for i, k in enumerate(('input_tokens', 'cached_input_tokens', 'output_tokens', 'reasoning_output_tokens')):
                    self.usage[i] += int(u.get(k) or 0)
            if (t in ('turn.failed', 'error') or 'error' in line[:60].lower()) and \
                    any(w in line.lower() for w in LIMIT_WORDS):
                self.limit = True
        self.last = last.read_text(encoding='utf-8', errors='replace') if last.exists() else ''
        return stalled

    def go(self):
        self.t0 = time.time()
        stalled = self._session(['exec', '-s', 'workspace-write', '-C', str(ROOT), '-c', 'tools.web_search=true',
                                 '--color', 'never'], self.prompt, '')
        if self.limit or time.time() - self.t0 > TIMEBOX:
            return
        if (stalled or not self.last.strip()) and self.thread:
            log('%s %s: %s; resuming once' % (self.subj, self.num, 'silent 20 minutes' if stalled else 'no last message'))
            self._session(['exec', 'resume', '-c', 'sandbox_mode="workspace-write"', '-c', 'tools.web_search=true',
                           self.thread], HUNG if stalled else CARRY, '-resume')


# ---------------------------------------------------------------- a lane

def lane(subj, dry=False):
    steps = load_queue(subj)
    done = done_set()
    fails_row = 0
    grade_fails, grade_days, grade = 0, 0, None
    for st in steps:
        if STOP.exists() or (DRAFT / ('STOP-' + subj)).exists():
            log('%s: STOP file seen; lane ends' % subj)
            return
        if subj in stopped_lanes():
            return
        if st[0] in ('merge', 'merge-new'):
            key = '%s:%s:%s' % (subj, st[0], st[1])
            if key in done:
                continue
            if dry:
                print('[dry] %s %s %s' % (subj, st[0], st[1]))
                continue
            with LOCK:
                merge_texts(st[1], st[0] == 'merge-new')
                commit(subj, 'ela texts %s for %s' % (st[0], st[1]))
            mark_done(key)
            continue
        _, num, kind, course, detail, fname, gate = st
        key = '%s:%s' % (subj, num)
        if key in done:
            continue
        if course != grade:
            grade, grade_fails, grade_days = course, 0, 0
        if dry:
            print('[dry] %s %s %s %s %s%s' % (subj, num, kind, course, detail, ('  gate: ' + gate) if gate else ''))
            continue
        text = (QUEUES / subj / fname).read_text(encoding='utf-8')
        while True:   # one pass per try; a usage limit pauses every lane and tries the same job again
            while PAUSE_UNTIL[0] > time.time():
                time.sleep(60)
                if STOP.exists():
                    return
            result, gfails, ndays = 'ok', '', 0
            t0 = time.time()
            if gate:
                code, out = py(*gate.split()[3:]) if gate.startswith('python -X utf8 ') else (1, 'bad gate line')
                if code:
                    result = 'gate-closed'
                    log('%s %s %s %s: ledger gate closed: %s' % (subj, num, kind, course, out.strip().splitlines()[-1:]))
            run = None
            if result == 'ok':
                prompt = (ROOT / 'docs/pipeline/kit/draft-preamble.txt').read_text(encoding='utf-8') + text
                extra = DRAFT / 'notes' / ('%s-%s.txt' % (subj, num))
                if extra.exists():   # a per-job note (say, work already done by hand that the job must keep)
                    prompt += '\n\nNote for this job (it wins over the job above):\n' + extra.read_text(encoding='utf-8')
                prompt = LESSONGATE.sub(lambda m: 'python -X utf8 scripts/lesson_course.py ' + m.group(1), prompt)
                prompt = REPO.sub(lambda m: m.group(0) + '-draft', prompt)
                prompt = prompt.replace('python -X utf8 ', '"%s" -X utf8 ' % sys.executable)   # the sandbox's own python lacks markdown
                log('%s start %s %s %s %s' % (subj, num, kind, course, detail))
                run = Run(subj, num, kind, course, detail, prompt)
                run.go()
                if run.limit:
                    PAUSE_UNTIL[0] = max(PAUSE_UNTIL[0], time.time() + LIMIT_PAUSE)
                    log('%s %s: usage limit; every lane pauses 30 minutes, then this job runs again' % (subj, num))
                    row(subj, num, kind, course, detail, 'limit', t0, run, '')
                    with LOCK:
                        commit(subj, 'partial %s %s %s (usage limit)' % (kind.lower(), course, detail))
                    continue
                if not run.last.strip():
                    result = 'failed'
                elif 'gate closed' in run.last[:400]:
                    result = 'gate-closed'
            break
        if result == 'ok' and kind in ('DAY', 'CHECKS'):
            nums = [int(x) for x in re.findall(r'\d+', gate or '')[-2:]] if gate else []
            if len(nums) == 2:
                code, out = py('scripts/lesson_course.py', course, str(nums[0]), str(nums[1]))
                m = re.search(r'lesson_course: (\d+) failure\(s\) in (\d+) day', out)
                if m:
                    gfails, ndays = int(m.group(1)), int(m.group(2))
                    grade_fails += gfails
                    grade_days += ndays
        with LOCK:
            commit(subj, '%s %s %s (job %s, %s)' % (kind.lower(), course, detail, num, result))
        row(subj, num, kind, course, detail, result, t0, run, gfails)
        log('%s done %s %s %s %s: %s%s' % (subj, num, kind, course, detail, result,
                                          (', %s gate failures in %d days' % (gfails, ndays)) if gfails != '' else ''))
        if result == 'ok':
            fails_row = 0
            mark_done(key)
        else:
            fails_row += 1
            mark_done(key)   # a failed draft is left for the review; the lane moves on unless failures pile up
            if fails_row >= MAX_FAILS:
                stop_lane(subj, '%d failed jobs in a row (last %s %s)' % (fails_row, num, kind))
                return
        if grade_fails > 4 + grade_days // 4:
            stop_lane(subj, '%s: %d lesson gate failures in %d drafted days' % (course, grade_fails, grade_days))
            return
    log('%s: lane finished' % subj)


def safe_lane(subj):
    try:
        lane(subj)
    except Exception:
        import traceback
        stop_lane(subj, 'runner error: ' + traceback.format_exc().strip().splitlines()[-1])
        log(traceback.format_exc())


def row(subj, num, kind, course, detail, result, t0, run, gfails):
    p = DRAFT / 'usage.csv'
    with LOGL:
        new = not p.exists()
        with open(p, 'a', encoding='utf-8', newline='') as f:
            w = csv.writer(f)
            if new:
                w.writerow(['ended', 'lane', 'job', 'kind', 'course', 'detail', 'result', 'minutes',
                            'tokens_in', 'cached_in', 'tokens_out', 'reasoning_out', 'gate_failures'])
            u = run.usage if run else [0, 0, 0, 0]
            w.writerow([now(), subj, num, kind, course, detail, result, round((time.time() - t0) / 60, 1), *u, gfails])


def commit(subj, msg):
    """Commit everything changed in the draft checkout (call under LOCK), then push the branch."""
    git('add', '-A')
    code, out = git('diff', '--cached', '--quiet')
    if code == 0:
        return
    code, out = git('commit', '-q', '-m', 'Codex draft (%s): %s\n\nWritten by scripts/codex_draft.py; unreviewed draft.' % (subj, msg))
    if code:
        log('commit failed: %s' % out.strip()[:300])
        return
    code, out = git('push', '-q', 'origin', 'HEAD:refs/heads/draft/codex')
    if code:
        log('push failed (the commit stays local): %s' % out.strip()[:300])


# ---------------------------------------------------------------- main

def status():
    done, stopped = done_set(), stopped_lanes()
    for subj in LANES:
        steps = [s for s in load_queue(subj) if s[0] == 'job']
        left = [s for s in steps if '%s:%s' % (subj, s[1]) not in done]
        nxt = ('%s %s %s %s' % left[0][1:5]) if left else 'none'
        print('%-15s %3d of %3d done; next %s%s' % (subj, len(steps) - len(left), len(steps), nxt,
                                                  '; STOPPED' if subj in stopped else ''))


def main(a):
    if not a:
        sys.exit(__doc__)
    if a[0] == 'setup':
        return setup()
    if a[0] == 'status':
        return status()
    if a[0] != 'run':
        sys.exit(__doc__)
    dry = '--dry' in a
    if ROOT.name != 'CurioClass-draft' and not dry:
        sys.exit('the draft run only runs in S:\\CurioClass-draft (this is %s)' % ROOT)
    only = [x for x in a[1:] if x in LANES]
    DRAFT.mkdir(exist_ok=True)
    if not dry:
        log('run starts: lanes %s' % ', '.join(only or LANES))
        keep_awake(True)
    threads = []
    for i, subj in enumerate(only or LANES):
        if dry:
            lane(subj, dry=True)
            continue
        if i:
            time.sleep(STAGGER)
        t = threading.Thread(target=safe_lane, args=(subj,), name=subj)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    if not dry:
        keep_awake(False)
        log('run ends')
        status()


if __name__ == '__main__':
    main(sys.argv[1:])

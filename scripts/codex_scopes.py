r"""The scope and sequence long run (Cory 2026-11-14): Codex writes every science, ELA and math scope and sequence,
reconciles the three courses that have older work, and gives each a first read. Then it stops: the expert read
(Claude), the fix pass and the unit plans come later.

    python -X utf8 scripts/codex_scopes.py                 run everything not yet done, 3 jobs at once
    python -X utf8 scripts/codex_scopes.py --jobs 2        fewer at once
    python -X utf8 scripts/codex_scopes.py --only math     one subject (science, ela or math) or one course id
    python -X utf8 scripts/codex_scopes.py --dry           print the plan, start nothing
    python -X utf8 scripts/codex_scopes.py --status        what is done, from the disk

Start Menu or double-click: scripts\Start-Codex-Scopes.bat. To stop gently, create S:\CurioClass\_scopes\STOP:
nothing new starts, running jobs finish. Closing the window stops everything. Run it again any time: it picks up where
it stopped, because what is done comes from the disk:

- written: `python -X utf8 scripts/sequence.py check <course>` passes;
- reconciled (math-grade-4, english-language-arts-grade-6, science-grade-4 only): docs/reviews/sequence-<course>-reconcile-<date>.md;
- read: docs/reviews/sequence-<course>-codex-<date>.md.

Each course is one chain, write, then reconcile where there is older work, then read; a step that fails twice stops
that course (logged), never the run. Order: science, ELA, math (math last). New starts stop when the weekly Codex
budget is at or below --min-remaining percent (default 8; Cory 2026-11-06: never hit 0) or when a usage limit shows.
Writers and readers are blind to the older work; only the reconciler opens it.
Logs: S:\CurioClass\_scopes\summary.txt (git-ignored) and one log per job beside it. No git: the lead commits after.

The fix pass (added 2026-11-15, after the Claude expert reads): `--fix` runs one job per course instead, the brief
docs/pipeline/briefs/sequence-fix.md with the lead calls in docs/reviews/sequence-lead-calls-2026-11-15.md. A course is
fixed when docs/reviews/sequence-<course>-fixes-<date>.md exists and its gate passes; the job may edit the course's
frame.md, scope-and-sequence.md, days.csv and source-map.csv only. Shared files wait for one structure pass after.

    python -X utf8 scripts/codex_scopes.py --fix              fix every course not yet fixed
    python -X utf8 scripts/codex_scopes.py --fix --status     what is fixed
"""
import argparse, csv, datetime as dt, glob, os, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
PY = [sys.executable, '-X', 'utf8']
RUN = os.path.join(ROOT, '_scopes')   # was S:\CurioClass-codex\_scopes until 2026-11-25
STOP = os.path.join(RUN, 'STOP')
STAGGER = 120
LIMIT_WORDS = ('usage limit', 'rate limit', 'rate_limit', 'insufficient_quota', 'try again at', 'upgrade to')

BAR = {'science': 'docs/RUBRIC-SCIENCE.md', 'ela': 'docs/RUBRIC-ELA.md', 'math': 'docs/RUBRIC-MATH-K8.md for kindergarten to grade 8, docs/RUBRIC-MATH-HS.md for algebra I, geometry and algebra II'}
SUBJECT_NOTE = {
    'science': ('NGSS is the base for every science course (Cory, 2026-11-14); the Massachusetts STE framework is a '
                'crosswalk only. Each expectation\'s three dimensions are in data/standards/ngss-pe-dimensions.csv. '
                'Fill the optional tools, supplies and safety columns (sequence-write.md). Grades 6 to 8 follow '
                'OpenSciEd\'s order where the frame says so (S:\\CurioClass-sources\\openscied-ms), ideas only, never wording.'),
    'ela': ('Each unit\'s texts are rows of data/plans/ela-texts.csv (title, author, use, status); place the anchor and '
            'paired texts on days, and say in the note which text a day reads. Where the frame names an EL Education '
            'base (S:\\CurioClass-sources\\el-education-k5-2017), write the source map (rule 8).'),
    'math': ('The base text is Illustrative Mathematics (S:\\CurioClass-sources\\illustrative-math), openly licensed '
             'pages only, no login-gated material. Write data/plans/{course}/source-map.csv (rule 8). Fill the optional '
             'tools and supplies columns (sequence-write.md).'),
}
BLIND = ('Blind rule: do not open docs/courses/ela-6/, docs/courses/ela-6-spine.md, docs/courses/math-4/, '
         'docs/courses/math-4-spine.md, docs/courses/math-3-5-progression*.md, docs/courses/science-4-spine.md, '
         'docs/courses/NEXT-SPINES.md, data/plans/math-4/, courses/math-4/, im-g4-draft-map.csv, or '
         'docs/reviews/*reconcile*, *math-4*, *ela-6*, science-4-spine*. Another course\'s scope and sequence may '
         'be written at the same time as yours; do not edit it.')
OLD = {
    'math-grade-4': 'docs/courses/math-4-spine.md, docs/courses/math-4/ (built days), data/plans/math-4/ (days.csv, '
                    'source-map.csv and the rest), docs/courses/math-3-5-progression.md and its findings file',
    'english-language-arts-grade-6': 'docs/courses/ela-6-spine.md and docs/courses/ela-6/',
    'science-grade-4': 'docs/courses/science-4-spine.md',
}
ORDER = {'science': 0, 'ela': 1, 'math': 2}
LOCK = threading.Lock()
state = {'halt': None, 'last_start': 0.0}


def log(line):
    os.makedirs(RUN, exist_ok=True)
    text = '%s  %s' % (dt.datetime.now().strftime('%Y-%m-%d %H:%M'), line)
    with LOCK:
        print(text, flush=True)
        with open(os.path.join(RUN, 'summary.txt'), 'a', encoding='utf-8') as f:
            f.write(text + '\n')


def courses(only=None):
    rows = list(csv.DictReader(open(os.path.join(ROOT, 'data', 'plans', 'frames.csv'), encoding='utf-8')))
    out = [r for r in rows if r['subject'] in ORDER]
    if only:
        out = [r for r in out if only in (r['subject'], r['course'])]
    grade = lambda g: -1 if g in ('K', 'k', '0') else int(g) if str(g).isdigit() else 99
    return sorted(out, key=lambda r: (ORDER[r['subject']], grade(r['grade']), r['course']))


def done_file(kind, course):
    pat = os.path.join(ROOT, 'docs', 'reviews', 'sequence-%s-%s-*.md' % (course, kind))
    return [p for p in glob.glob(pat) if os.path.getsize(p) > 200]


def written(course):
    return subprocess.run(PY + ['scripts/sequence.py', 'check', course], cwd=ROOT,
                          capture_output=True, text=True, encoding='utf-8').returncode == 0


def budget():
    try:
        import codex_budget
        return codex_budget.codex_remaining()
    except Exception:
        return None


def may_start(a):
    if os.path.exists(STOP):
        state['halt'] = state['halt'] or 'STOP file'
    left = budget()
    if left is not None and left <= a.min_remaining:
        state['halt'] = state['halt'] or 'weekly Codex budget at %s%% left' % left
    if state['halt']:
        return False
    with LOCK:                       # two sandboxes starting at once failed their handshake (2026-11-04)
        wait = state['last_start'] + STAGGER - time.time()
        state['last_start'] = max(time.time(), state['last_start'] + STAGGER)
    if wait > 0:
        time.sleep(wait)
    return not state['halt']


def brief(name, extra, logdir, tag):
    text = open(os.path.join(ROOT, 'docs', 'pipeline', 'briefs', name), encoding='utf-8').read()
    p = os.path.join(logdir, '%s.brief.md' % tag)
    open(p, 'w', encoding='utf-8').write(text.rstrip() + '\n\n' + extra + '\n')
    return p


def run(cmd, logpath):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
    open(logpath, 'w', encoding='utf-8').write((r.stdout or '') + (r.stderr or ''))
    text = (r.stdout or '') + (r.stderr or '')
    if any(w in text.lower() for w in LIMIT_WORDS):
        state['halt'] = state['halt'] or 'usage limit reported'
    return r.returncode


def chain(c, a, logdir):
    course, subj = c['course'], c['subject']
    date = dt.date.today().isoformat()
    slots = ['subject=' + subj, 'bar=' + BAR[subj], 'date=' + date]
    note = SUBJECT_NOTE[subj].replace('{course}', course)
    # 1. write
    tries = 0
    while not written(course):
        if tries == 2:
            log('%s: write FAILED twice (gate still fails); course stopped' % course)
            return 'write failed'
        if not may_start(a):
            return 'held: ' + state['halt']
        tries += 1
        b = brief('sequence-write.md', '## For this run\n' + BLIND + (
            '' if tries == 1 else '\n\nA first try left the gate failing: open the files as they are, run the gate, '
            'and fix every FAIL.'), logdir, course + '-write')
        log('%s: write, try %d' % (course, tries))
        run(PY + ['scripts/codex_write.py', b, course] + slots +
            ['extra=' + note, 'allow=docs/courses/{course}/scope-and-sequence.md;data/plans/{course}/days.csv;'
             'data/plans/{course}/source-map.csv', 'tag=%s-scope' % course,
             'log=' + os.path.join(logdir, course + '-write.codex.log')],
            os.path.join(logdir, course + '-write.log'))
    log('%s: written, gate passes' % course)
    # 2. reconcile, where there is older work
    if course in OLD and not done_file('reconcile', course):
        for t in (1, 2):
            if not may_start(a):
                return 'held: ' + state['halt']
            log('%s: reconcile, try %d' % (course, t))
            b = brief('sequence-reconcile.md', '', logdir, course + '-reconcile')
            run(PY + ['scripts/codex_write.py', b, course] + slots +
                ['old=' + OLD[course], 'allow=docs/courses/{course}/scope-and-sequence.md;data/plans/{course}/days.csv;'
                 'data/plans/{course}/source-map.csv', 'tag=%s-reconcile' % course,
                 'log=' + os.path.join(logdir, course + '-reconcile.codex.log')],
                os.path.join(logdir, course + '-reconcile.log'))
            src = os.path.join(ROOT, 'docs', 'reviews', 'codex-write-%s-reconcile-%s.md' % (course, date))
            if os.path.exists(src) and os.path.getsize(src) > 200 and written(course):
                os.replace(src, os.path.join(ROOT, 'docs', 'reviews', 'sequence-%s-reconcile-%s.md' % (course, date)))
                break
        else:
            log('%s: reconcile FAILED twice; course stopped before its read' % course)
            return 'reconcile failed'
    # 3. the first read
    if not done_file('codex', course):
        for t in (1, 2):
            if not may_start(a):
                return 'held: ' + state['halt']
            log('%s: read, try %d' % (course, t))
            b = brief('sequence-read.md', '## For this run\nYou are the first reader, before the expert. ' + BLIND,
                      logdir, course + '-read')
            out = os.path.join(ROOT, 'docs', 'reviews', 'sequence-%s-codex-%s.md' % (course, date))
            run(PY + ['scripts/codex_read.py', b, out, 'course=' + course] + slots,
                os.path.join(logdir, course + '-read.log'))
            if os.path.exists(out + '.log'):
                os.replace(out + '.log', os.path.join(logdir, course + '-read.codex.log'))
            if done_file('codex', course):
                break
        else:
            log('%s: read FAILED twice' % course)
            return 'read failed'
    log('%s: DONE (written%s, read)' % (course, ', reconciled' if course in OLD else ''))
    return 'done'


def fix_chain(c, a, logdir):
    course, subj = c['course'], c['subject']
    date = dt.date.today().isoformat()
    if done_file('fixes', course) and written(course):
        return 'done'
    slots = ['subject=' + subj, 'bar=' + BAR[subj], 'date=' + date]
    for t in (1, 2):
        if not may_start(a):
            return 'held: ' + state['halt']
        log('%s: fix, try %d' % (course, t))
        b = brief('sequence-fix.md', '## For this run\n' + BLIND + '\n\n' + SUBJECT_NOTE[subj].replace('{course}', course) + (
            '' if t == 1 else '\n\nA first try did not finish (no report, or the gate still fails): open the files as '
            'they are, finish the work, run the gates and fix every FAIL.'), logdir, course + '-fix')
        run(PY + ['scripts/codex_write.py', b, course] + slots +
            ['allow=docs/courses/{course}/scope-and-sequence.md;docs/courses/{course}/frame.md;'
             'data/plans/{course}/days.csv;data/plans/{course}/source-map.csv', 'tag=%s-fixes' % course,
             'log=' + os.path.join(logdir, course + '-fix.codex.log')],
            os.path.join(logdir, course + '-fix.log'))
        src = os.path.join(ROOT, 'docs', 'reviews', 'codex-write-%s-fixes-%s.md' % (course, date))
        if os.path.exists(src) and os.path.getsize(src) > 200 and written(course):
            os.replace(src, os.path.join(ROOT, 'docs', 'reviews', 'sequence-%s-fixes-%s.md' % (course, date)))
            log('%s: FIXED, gate passes' % course)
            return 'done'
    log('%s: fix FAILED twice (no report or the gate fails)' % course)
    return 'fix failed'


def status(cs):
    for c in cs:
        k = c['course']
        print('%-36s %-8s written=%s reconcile=%s read=%s fixed=%s' % (
            k, c['subject'], 'yes' if written(k) else 'no',
            ('yes' if done_file('reconcile', k) else 'no') if k in OLD else '-',
            'yes' if done_file('codex', k) else 'no', 'yes' if done_file('fixes', k) else 'no'))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--jobs', type=int, default=3)
    p.add_argument('--only')
    p.add_argument('--min-remaining', type=float, default=8)
    p.add_argument('--dry', action='store_true')
    p.add_argument('--status', action='store_true')
    p.add_argument('--fix', action='store_true', help='the fix pass (sequence-fix.md), one job per course')
    a = p.parse_args()
    cs = courses(a.only)
    if a.status or a.dry:
        status(cs)
        if a.dry:
            print('\n%d courses; %d at once; budget left: %s%%' % (len(cs), a.jobs, budget()))
        return
    if os.path.exists(STOP):
        os.remove(STOP)
    day = dt.datetime.now().strftime('%Y-%m-%d_%H%M')
    logdir = os.path.join(RUN, day)
    os.makedirs(logdir, exist_ok=True)
    if os.name == 'nt':
        import ctypes
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x00000001)
    log('%s start: %d courses, %d at once, budget left %s%%' % ('fix pass' if a.fix else 'run', len(cs), a.jobs, budget()))
    job = fix_chain if a.fix else chain
    with ThreadPoolExecutor(a.jobs) as ex:
        results = dict(zip([c['course'] for c in cs], ex.map(lambda c: job(c, a, logdir), cs)))
    tally = {}
    for v in results.values():
        tally[v.split(':')[0]] = tally.get(v.split(':')[0], 0) + 1
    log('run end: %s; budget left %s%%%s' % (tally, budget(), '; halted: ' + state['halt'] if state['halt'] else ''))
    for k, v in results.items():
        if v != 'done':
            log('  %s: %s' % (k, v))


if __name__ == '__main__':
    main()

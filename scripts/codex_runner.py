r"""Run Cory's Codex queue unattended: each build and each review is its own fresh `codex exec` session, the same as
pasting a block from _queue.txt into a new Codex chat.

    python scripts/codex_runner.py                  run until the queue is empty, the usage limit is hit, or STOP
    python scripts/codex_runner.py --builds 2 --reviews 2      fewer at once (defaults 3 builds, 4 reviews, 2 fixes)
    python scripts/codex_runner.py --fixes 0                                no fixes this run
    python scripts/codex_runner.py --max-builds 15 --max-reviews 15         stop starting each kind after this many
    python scripts/codex_runner.py --max-jobs 1 --reviews 1 --builds 0      one review only (a test)
    python scripts/codex_runner.py --only nonsense-words                    only these tools
    python scripts/codex_runner.py --dry                                    print what it would start, start nothing

Start Menu: "Codex Queue" runs it in a window (scripts\Start-Codex-Queue.bat). To stop it gently, create the file
S:\CurioClass-codex\_runner\STOP: nothing new starts, running sessions finish. Closing the window stops everything.

What is done comes from the disk, as in codex_queue.py: codex-report.md means built, codex-review.md means reviewed,
polish.md means fixed (a fix is wanted only for tools in codex_queue.FIX with an OPEN or ROUND 2 refine.md; see
docs/agents/CODEX-FIX.md). A finished build makes its review eligible in a new session. Fixes go first, then reviews,
oldest built first, then builds.

Watchdog (docs/agents/CODEX.md, "Run"): a session whose events log stops growing for 20 minutes gets the hung-command
message as a resume of the same session; a "model at capacity" or dropped turn gets "carry on". At most 3 resumes and
3 hours per job, then it is logged as failed and left for a person. A usage or rate limit message stops new starts.
A tool someone touched in the last 20 minutes waits (looked at again every pass), in case a hand-pasted chat is working
on it, unless this run just finished it. A slot whose ports are in use waits; when a job ends, the runner kills whatever
still listens on that slot's ports. codex_queue.REDO adds a note to a rebuild's prompt.

Logs: S:\CurioClass-codex\_runner\<date>\ (one events .jsonl and last-message .md per session) and
_runner\summary.txt (one line per job). The PC is kept awake while it runs. _queue.txt is refreshed at the end.

Change a run while it runs: the runner writes _runner\LIMITS.json at start (how many at once, and the caps per kind) and
re-reads it every 30 seconds, so editing a number there (say "max_reviews": 15 to 25) takes effect without a restart.
It also re-reads scripts/codex_queue.py each time, so tools added to QUEUE or FIX there join the run. A bad edit is
logged and ignored; the last good values stay.
Budget floor: "min_remaining" (default 8, --min-remaining) starts nothing new once the weekly Codex budget is at or below that
percent left, read from the newest rate_limits in ~/.codex/sessions; running sessions finish (Cory 2026-11-06: never hit 0). Lowering a number never stops a running session.
"""
import argparse, ctypes, datetime as dt, importlib, json, os, shutil, socket, subprocess, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import codex_queue as cq  # noqa: E402

BASE = cq.BASE
RUN = BASE / '_runner'
STOP = RUN / 'STOP'
STALL = 20 * 60
TIMEBOX = 3 * 3600
MAX_RESUMES = 3
FRESH = 20 * 60
STAGGER = 120      # seconds between session starts: two sandboxes starting at once failed their handshake (2026-11-04)
EARLY = 10 * 60    # a session that ends this fast without its file failed to start; it gets one fresh restart
HUNG = ("That command hung, so I stopped it. Close any Chrome or server you started, note it under Left open in the report, "
        "and carry on with the next step.")
CARRY = "Your connection dropped. Carry on from where you were and finish the report."
CUT = ("Your session was cut off and has been restarted. Any Chrome or server you had started is gone, so start fresh ones "
       "when you need them. Check what is already done in the tool folder, then carry on from where you were and finish the report.")
LIMIT_WORDS = ('usage limit', 'rate limit', 'rate_limit', 'quota', 'insufficient_quota', 'try again at', 'upgrade to')
CAPACITY_WORDS = ('at capacity', 'overloaded', 'stream disconnected', 'server_error', 'internal server error')


SESSIONS = Path.home() / '.codex' / 'sessions'


def codex_remaining():
    """Percent of the weekly Codex budget left, from the newest "rate_limits" any Codex session logged (its last 4 MB;
    rollouts reach 140 MB). None when nothing recent says. Every session, the runner's and the app's, shares one budget."""
    days = sorted((d for d in SESSIONS.glob('*/*/*') if d.is_dir()), reverse=True)[:3]
    files = sorted((f for d in days for f in d.glob('rollout-*.jsonl')), key=lambda f: f.stat().st_mtime, reverse=True)
    for f in files[:6]:
        try:
            with open(f, 'rb') as h:
                h.seek(max(0, f.stat().st_size - 4_000_000))
                tail = h.read().decode('utf-8', 'replace')
        except OSError:
            continue
        i = tail.rfind('"primary":{"used_percent":')
        if i >= 0:
            num = tail[i + 26:i + 40].split(',')[0].split('}')[0]
            try:
                return round(100 - float(num), 1)
            except ValueError:
                continue
    return None


def now():
    return dt.datetime.now().strftime('%Y-%m-%d %H:%M')


def log(line):
    RUN.mkdir(parents=True, exist_ok=True)
    text = f'{now()}  {line}'
    print(text, flush=True)
    with open(RUN / 'summary.txt', 'a', encoding='utf-8') as f:
        f.write(text + '\n')


def keep_awake(on=True):
    if os.name == 'nt':  # ES_CONTINUOUS | ES_SYSTEM_REQUIRED; the display may still sleep
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | (0x00000001 if on else 0))


def recently_touched(t):
    cutoff = time.time() - FRESH
    for root in (BASE / 'tools' / t, BASE / '_scratch' / t):
        if not root.exists():
            continue
        for p in root.rglob('*'):
            try:
                if p.is_file() and p.stat().st_mtime > cutoff:
                    return True
            except OSError:
                pass
    return False


LIMITS = RUN / 'LIMITS.json'
LIMIT_KEYS = {'builds': 3, 'reviews': 4, 'fixes': 2, 'max_builds': None, 'max_reviews': None, 'max_fixes': None, 'max_jobs': None,
              'min_remaining': 100}
# "no_new_after": "YYYY-MM-DD HH:MM" in LIMITS.json: start nothing new after then; running sessions finish (empty = no limit)
TABLES = {}


def load_tables():
    TABLES.update({'build': (cq.BUILD_PORTS, cq.BUILD), 'review': (cq.REVIEW_PORTS, cq.REVIEW), 'fix': (cq.FIX_PORTS, cq.FIXP)})


load_tables()


def write_limits(a):
    LIMITS.write_text(json.dumps({**{k: getattr(a, k) for k in LIMIT_KEYS}, 'no_new_after': a.no_new_after}, indent=2) + '\n', encoding='utf-8')


def read_limits(a, seen):
    """Apply LIMITS.json and a fresh codex_queue.py; log what changed. `seen` keeps the last bad-edit message, so it logs once."""
    global cq
    try:
        cq = importlib.reload(cq)
        load_tables()
    except Exception as e:  # a half-saved edit: keep the module already loaded
        if seen.get('queue') != str(e):
            log(f'codex_queue.py did not load ({e}); keeping the last good queue')
            seen['queue'] = str(e)
    else:
        seen.pop('queue', None)
    try:
        new = json.loads(LIMITS.read_text(encoding='utf-8'))
        for k, top in LIMIT_KEYS.items():
            v = int(new.get(k, getattr(a, k)))
            v = max(0, min(v, top) if top else v)
            if v != getattr(a, k):
                log(f'LIMITS.json: {k} {getattr(a, k)} -> {v}')
                setattr(a, k, v)
        cut = str(new.get('no_new_after', a.no_new_after) or '').strip().replace('T', ' ')
        if cut:
            dt.datetime.strptime(cut, '%Y-%m-%d %H:%M')
        if cut != a.no_new_after:
            log(f'LIMITS.json: no_new_after {a.no_new_after or "none"} -> {cut or "none"}')
            a.no_new_after = cut
        seen.pop('limits', None)
    except FileNotFoundError:
        write_limits(a)
    except (ValueError, TypeError, AttributeError) as e:
        if seen.get('limits') != str(e):
            log(f'LIMITS.json did not read ({e}); keeping {", ".join(f"{k}={getattr(a, k)}" for k in LIMIT_KEYS)}')
            seen['limits'] = str(e)


def port_busy(kind, slot):
    """True when a hand-pasted chat (or anything else) is using this slot's host or Chrome ports right now."""
    c, h = TABLES[kind][0][slot]
    for port in [h, *range(c, c + 8)]:
        with socket.socket() as s:
            s.settimeout(0.2)
            if s.connect_ex(('127.0.0.1', port)) == 0:
                return True
    return False


_ANCESTORS = set()


def ancestors():
    """This process and every parent up the chain. A socket handle inherited by the launcher can make the runner's own
    parent (the python shim or cmd) the "owner" of a slot port, and taskkill /T on it ended the runner at 05:13 on
    2026-11-06 (no log line after "done fix poets-workbench"; three finished jobs went unrecorded)."""
    if not _ANCESTORS:
        _ANCESTORS.add(os.getpid())
        try:
            rows = subprocess.run(['powershell', '-NoProfile', '-Command',
                                   'Get-CimInstance Win32_Process | ForEach-Object { "$($_.ProcessId) $($_.ParentProcessId)" }'],
                                  capture_output=True, text=True, timeout=60).stdout.splitlines()
            parent = dict(tuple(map(int, r.split())) for r in rows if len(r.split()) == 2)
            pid = os.getpid()
            while pid in parent and parent[pid] not in _ANCESTORS and parent[pid] > 4:
                pid = parent[pid]
                _ANCESTORS.add(pid)
        except (OSError, subprocess.SubprocessError, ValueError):
            pass
    return _ANCESTORS


def free_ports(kind, slot):
    """Kill whatever still listens on a finished job's host and Chrome ports: a session's drive.py server or Chrome can
    outlive it and hold the slot (reviews stalled 05:05 to 10:31 on 2026-11-05)."""
    c, h = TABLES[kind][0][slot]
    ports = {h, *range(c, c + 8)}
    # netstat does not list sockets made inside the Codex sandbox; Get-NetTCPConnection does (2026-11-05)
    cmd = ('Get-NetTCPConnection -LocalPort ' + ','.join(map(str, sorted(ports))) +
           ' -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess -Unique')
    try:
        out = subprocess.run(['powershell', '-NoProfile', '-Command', cmd], capture_output=True, text=True, timeout=60).stdout
    except (OSError, subprocess.SubprocessError):
        return
    pids = {p for p in out.split() if p.isdigit() and int(p) not in (0, 4) and int(p) not in ancestors()}
    ended = 0
    for pid in pids:  # /T can fail on an orphan whose parent is gone (2026-11-05); then kill it alone
        if subprocess.run(['taskkill', '/T', '/F', '/PID', pid], capture_output=True).returncode == 0 or \
                subprocess.run(['taskkill', '/F', '/PID', pid], capture_output=True).returncode == 0:
            ended += 1
    # one session can start drive.py on the same host port several times, and Windows lets each copy bind it while
    # the port lookup above names only one; the rest kept slots looking busy all night (2026-11-07). Match by command.
    extra = {pid for pid, _ in drive_servers(h)} - {int(p) for p in pids}
    for pid in extra:
        if subprocess.run(['taskkill', '/F', '/PID', str(pid)], capture_output=True).returncode == 0:
            ended += 1
    if pids or extra:
        log(f'freed {kind} slot {slot}: ended {ended} of {len(pids) + len(extra)} leftover process(es) on its ports')


def drive_servers(host=None):
    """(pid, tool) for every drive.py server running, or only those on one host port."""
    cmd = ("Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | Where-Object CommandLine -match 'drive[.]py' |"
           " Select-Object ProcessId,CommandLine | ConvertTo-Json -Compress")
    try:
        out = subprocess.run(['powershell', '-NoProfile', '-Command', cmd], capture_output=True, text=True, timeout=60).stdout
        rows = json.loads(out) if out.strip() else []
    except (OSError, subprocess.SubprocessError, ValueError):
        return []
    found = []
    for r in rows if isinstance(rows, list) else [rows]:
        words = [w.strip('"') for w in (r.get('CommandLine') or '').split()]
        try:
            tool, port = words[words.index('scripts/drive.py') + 1], int(words[words.index('--host') + 1])
        except (ValueError, IndexError):
            continue
        if host is None or port == host:
            found.append((r['ProcessId'], tool))
    return found


def reap_orphans(kind, slot, busy):
    """A slot none of our jobs holds but whose ports are taken: free it when every holder is a drive.py server for a tool
    nobody is working on (not running here, untouched for 20 minutes). A hand-pasted chat's server stays."""
    c, h = TABLES[kind][0][slot]
    servers = drive_servers(h)
    if servers and all(t not in busy and not recently_touched(t) for _, t in servers):
        free_ports(kind, slot)


def codex_exe():
    exe = shutil.which('codex') or shutil.which('codex.cmd')
    npm = Path(os.environ.get('APPDATA', str(Path.home() / 'AppData' / 'Roaming'))) / 'npm' / 'codex.cmd'
    if not exe and npm.exists():  # a scheduled task's PATH can miss the npm folder (2026-11-04)
        exe = str(npm)
    if not exe:  # installed from inside the Claude app: its private AppData copy, unseen by tasks
        local = Path(os.environ.get('LOCALAPPDATA', str(Path.home() / 'AppData' / 'Local')))
        hits = sorted(local.glob('Packages/Claude_*/LocalCache/Roaming/npm/codex.cmd'))
        exe = str(hits[0]) if hits else None
    if not exe:
        sys.exit('codex is not on PATH')
    return exe


class Job:
    def __init__(self, kind, t, slot, day):
        self.kind, self.t, self.slot = kind, t, slot
        table, template = TABLES[kind]
        c, h = cq.ports(table, slot)
        text = template.format(t=t, c=c, h=h)
        if t in cq.NOTES and kind != 'fix':
            text += '\n\n' + cq.NOTES[t]
        if kind == 'build' and t in getattr(cq, 'REDO', {}):
            text += '\n\n' + cq.REDO[t]
        text += ('\n\nThis session runs unattended: nobody will answer questions. Where you would ask, take the option the '
                 'spec or brief leans toward and note it in the report.')
        self.prompt = text
        self.stem = day / f'{kind}-{t}'
        self.thread = None
        self.resumes = 0
        self.started = time.time()
        self.proc = None
        self.events = None
        self.seen = 0
        self.grew = time.time()
        self.limit = False
        self.failed_turn = None
        self.restarted = False

    def _launch(self, args, prompt, suffix):
        self.events = Path(f'{self.stem}{suffix}.jsonl')
        last = Path(f'{self.stem}{suffix}-last.md')
        out = open(self.events, 'w', encoding='utf-8')
        self.proc = subprocess.Popen([codex_exe(), *args, '--json', '-o', str(last), '-'], cwd=BASE, stdin=subprocess.PIPE,
                                     stdout=out, stderr=subprocess.STDOUT, text=True, encoding='utf-8',
                                     creationflags=getattr(subprocess, 'CREATE_NEW_PROCESS_GROUP', 0))
        self.proc.stdin.write(prompt)
        self.proc.stdin.close()
        self.seen, self.grew = 0, time.time()

    def start(self):
        """Start a fresh session, or pick up today's session for this job if an earlier run was cut off mid-way."""
        prev = Path(f'{self.stem}.jsonl')
        if prev.exists() and not self.thread:
            with open(prev, encoding='utf-8', errors='replace') as f:
                first = f.readline()
            try:
                self.thread = json.loads(first).get('thread_id')
            except ValueError:
                self.thread = None
            if self.thread:
                log(f'pick up {self.kind} {self.t}: an earlier run was cut off; resuming its session')
                self.resume(CUT)
                return
        self._launch(['exec', '--sandbox', 'workspace-write', '-C', str(BASE)], self.prompt, '')

    def resume(self, prompt):
        self.resumes += 1
        n = self.resumes
        while Path(f'{self.stem}-resume{n}.jsonl').exists():
            n += 1
        self._launch(['exec', 'resume', '-c', 'sandbox_mode="workspace-write"', self.thread], prompt, f'-resume{n}')

    def kill(self):
        if self.proc and self.proc.poll() is None:
            subprocess.run(['taskkill', '/T', '/F', '/PID', str(self.proc.pid)], capture_output=True)

    def scan(self):
        """Read new events; note the thread id, a failed turn, and any usage-limit message."""
        try:
            size = self.events.stat().st_size
        except OSError:
            return
        if size == self.seen:
            return
        with open(self.events, encoding='utf-8', errors='replace') as f:
            f.seek(self.seen)
            chunk = f.read()
        self.seen, self.grew = size, time.time()
        for line in chunk.splitlines():
            low = line.lower()
            try:
                ev = json.loads(line)
            except ValueError:
                ev = {}
            if ev.get('type') == 'thread.started' and not self.thread:
                self.thread = ev.get('thread_id')
            if ev.get('type') in ('turn.failed', 'error') or 'error' in low[:40]:
                if any(w in low for w in LIMIT_WORDS):
                    self.limit = True
                if ev.get('type') == 'turn.failed':
                    self.failed_turn = line[:300]

    def done(self):
        if self.kind == 'fix':
            return (cq.BASE / 'tools' / self.t / 'polish.md').exists()
        built, reviewed = cq.state(self.t)
        return built if self.kind == 'build' else reviewed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--builds', type=int, default=3)
    ap.add_argument('--reviews', type=int, default=4)
    ap.add_argument('--fixes', type=int, default=2)
    ap.add_argument('--no-new-after', default='', help='"YYYY-MM-DD HH:MM": start nothing new after this time')
    for k in ('builds', 'reviews', 'fixes'):
        ap.add_argument(f'--max-{k}', type=int, default=0, help=f'stop starting {k} after this many (0 = no limit)')
    ap.add_argument('--max-jobs', type=int, default=0, help='stop starting new jobs after this many (0 = no limit)')
    ap.add_argument('--min-remaining', type=int, default=8,
                    help='start nothing new once the weekly Codex budget is at or below this percent left (0 = off); running sessions finish')
    ap.add_argument('--only', nargs='*')
    ap.add_argument('--dry', action='store_true')
    a = ap.parse_args()
    a.builds, a.reviews, a.fixes = min(a.builds, 3), min(a.reviews, 4), min(a.fixes, 2)
    a.no_new_after = a.no_new_after.strip().replace('T', ' ')
    if a.no_new_after:
        dt.datetime.strptime(a.no_new_after, '%Y-%m-%d %H:%M')  # fail now, not at midnight

    day = RUN / dt.date.today().isoformat()
    day.mkdir(parents=True, exist_ok=True)
    if STOP.exists():
        STOP.unlink()
    if not a.dry:
        write_limits(a)
    seen = {}
    running, tried, started, stop_reason, last_start = [], set(), 0, None, 0.0
    reaped = 0.0  # last orphan sweep
    ours, noted = set(), set()  # tools this run just finished (their fresh files are ours); waits already logged
    count = {'build': 0, 'review': 0, 'fix': 0}
    keep_awake(True)
    log(f'runner start: up to {a.builds} builds, {a.reviews} reviews and {a.fixes} fixes at once')
    if not a.dry:  # leftovers from an earlier run hold slots until killed
        for kind, (table, _) in list(TABLES.items()):
            for slot in table:
                free_ports(kind, slot)
    try:
        while True:
            if not a.dry:
                read_limits(a, seen)
            queue = [t for t in cq.QUEUE if not a.only or t in a.only]
            fixq = [t for t in cq.FIX if not a.only or t in a.only]
            cap_of = {'build': a.max_builds, 'review': a.max_reviews, 'fix': a.max_fixes}
            if STOP.exists() and not stop_reason:
                stop_reason = 'STOP file'
            if a.min_remaining and not stop_reason and not a.dry:
                left = codex_remaining()
                if left is not None and left <= a.min_remaining:
                    stop_reason = f'Codex budget at {left}% left (floor {a.min_remaining}%)'
                    log(f'{stop_reason}: no new starts; running sessions finish')
            if a.no_new_after and not stop_reason and now() >= a.no_new_after:
                stop_reason = f'no new starts after {a.no_new_after}'
                log(f'{stop_reason}: running sessions finish')
            # start new work (one start per STAGGER; waiting = there was work to start but the stagger held it back)
            waiting = False
            if not stop_reason and not (a.max_jobs and started >= a.max_jobs):
                busy = {j.t for j in running}
                sweep = not a.dry and time.time() - reaped > 300
                if sweep:
                    reaped = time.time()
                for kind, cap, slots, tools in (('fix', a.fixes, 'AB', fixq), ('review', a.reviews, 'ABCD', queue),
                                                ('build', a.builds, 'ABC', queue)):
                    mine = {j.slot for j in running if j.kind == kind}
                    if sweep:  # leftovers that outlived their job (2026-11-07)
                        for s in slots[:cap]:
                            if s not in mine and port_busy(kind, s):
                                reap_orphans(kind, s, busy)
                    free = [s for s in slots[:cap] if s not in mine and (a.dry or not port_busy(kind, s))]
                    for t in tools:
                        if not free or (a.max_jobs and started >= a.max_jobs) or (cap_of[kind] and count[kind] >= cap_of[kind]):
                            break
                        built, reviewed = cq.state(t)
                        want = ((kind == 'review' and built and not reviewed) or (kind == 'build' and not built)
                                or (kind == 'fix' and cq.fix_wanted(t)))
                        if not want or t in busy or (kind, t) in tried:
                            continue
                        if t not in ours and recently_touched(t):
                            if (kind, t) not in noted:  # wait for now; looked at again every pass
                                noted.add((kind, t))
                                log(f'wait {kind} {t}: touched in the last 20 minutes (a hand-pasted chat?)')
                            continue
                        if not a.dry and time.time() - last_start < STAGGER:
                            waiting = True
                            break
                        tried.add((kind, t))
                        count[kind] += 1
                        if a.dry:
                            log(f'would start {kind} {t} (slot {free[0]})')
                            free.pop(0)
                            continue
                        j = Job(kind, t, free.pop(0), day)
                        j.start()
                        running.append(j)
                        busy.add(t)
                        started += 1
                        last_start = time.time()
                        left = codex_remaining()
                        log(f'start {kind} {t} (slot {j.slot})' + (f', Codex budget {left}% left' if left is not None else ''))
            if a.dry:
                break
            if not running and not waiting:
                break
            time.sleep(30)
            # watch running work
            for j in list(running):
                j.scan()
                if j.limit and not stop_reason:
                    stop_reason = 'usage limit'
                    log(f'usage limit reported in {j.kind} {j.t}: no new sessions start')
                exited = j.proc.poll() is not None
                if exited:
                    j.scan()
                if exited and j.done():
                    running.remove(j)
                    ours.add(j.t)
                    free_ports(j.kind, j.slot)
                    log(f'done {j.kind} {j.t} in {int((time.time() - j.started) / 60)} min, {j.resumes} resumes')
                    continue
                stalled = not exited and time.time() - j.grew > STALL
                over = time.time() - j.started > TIMEBOX
                if over or (exited or stalled) and (j.limit or not j.thread or j.resumes >= MAX_RESUMES):
                    j.kill()
                    running.remove(j)
                    free_ports(j.kind, j.slot)
                    why = 'timebox' if over else 'usage limit' if j.limit else 'no session id' if not j.thread else 'resumes used up'
                    log(f'FAILED {j.kind} {j.t}: {why}; left for a person ({j.events.name})')
                    continue
                if exited and not j.restarted and time.time() - j.started < EARLY and not j.limit:
                    j.restarted = True
                    log(f'restart {j.kind} {j.t}: ended in its first minutes without its file (startup failure?)')
                    j.started = time.time()
                    j.thread = None
                    j.stem = Path(f'{j.stem}-fresh')
                    j.start()
                    continue
                if stalled:
                    j.kill()
                    log(f'resume {j.kind} {j.t}: no events for 20 minutes')
                    j.resume(HUNG)
                elif exited:
                    log(f'resume {j.kind} {j.t}: session ended without its file ({(j.failed_turn or "no error")[:120]})')
                    j.resume(CARRY)
    except KeyboardInterrupt:
        for j in running:
            j.kill()
        log('runner stopped by hand; running sessions killed')
    finally:
        keep_awake(False)
    if not a.dry:
        log(f'runner end: {stop_reason or "queue empty for this run"}')
        cq.prompts()


if __name__ == '__main__':
    main()

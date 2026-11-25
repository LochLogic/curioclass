"""One safe way to rewrite a shared data file while other jobs run (consolidation 4.E2, step 0).

    with safe_write.lock(path):          # one writer at a time per file; read, change and write inside the block
        ...
        safe_write.replace(path, data)   # bytes or str: a temp file unique to this process, then os.replace

    python -X utf8 scripts/safe_write.py --self-test    six processes add rows to one file at once; none may be lost

The lock is a file <name>.lock made with O_EXCL. A waiting writer retries for up to WAIT seconds; a lock older than
STALE seconds (a crashed job) is cleared. os.replace is retried on PermissionError, which Windows raises while
another process has the target open for reading. Used by scripts/ledger.py and scripts/rows.py.
"""
import contextlib
import os
import sys
import threading
import time
from pathlib import Path

WAIT, STALE, STEP = 60.0, 120.0, 0.05


@contextlib.contextmanager
def lock(path):
    p = Path(str(path) + '.lock')
    p.parent.mkdir(parents=True, exist_ok=True)
    start = time.time()
    while True:
        try:
            fd = os.open(p, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, ('%d\n' % os.getpid()).encode())
            os.close(fd)
            break
        except FileExistsError:
            try:
                if time.time() - p.stat().st_mtime > STALE:
                    p.unlink()
                    continue
            except FileNotFoundError:
                continue
            if time.time() - start > WAIT:
                raise SystemExit('safe_write: %s is locked by another job for over %d seconds; if no job is running, '
                                 'delete the .lock file' % (path, WAIT))
            time.sleep(STEP)
        except PermissionError:
            if time.time() - start > WAIT:
                raise
            time.sleep(STEP)
    try:
        yield
    finally:
        for _ in range(200):
            try:
                p.unlink()
                break
            except FileNotFoundError:
                break
            except PermissionError:
                time.sleep(STEP)


def replace(path, data):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, str):
        data = data.encode('utf-8')
    tmp = p.with_name('%s.%d-%d.tmp' % (p.name, os.getpid(), threading.get_ident()))
    tmp.write_bytes(data)
    for i in range(200):
        try:
            os.replace(tmp, p)
            return
        except PermissionError:
            if i == 199:
                tmp.unlink(missing_ok=True)
                raise
            time.sleep(STEP)


def read_text(path):
    """Reads a file that another process may be replacing at this moment."""
    for i in range(200):
        try:
            return Path(path).read_bytes().decode('utf-8')
        except PermissionError:
            if i == 199:
                raise
            time.sleep(STEP)


def _worker(target, n, tag):
    for i in range(n):
        with lock(target):
            old = read_text(target) if Path(target).exists() else ''
            replace(target, old + '%s-%d\n' % (tag, i))


def self_test():
    import subprocess
    import tempfile
    d = Path(tempfile.mkdtemp())
    target = d / 't.csv'
    procs = [subprocess.Popen([sys.executable, __file__, '--worker', str(target), '40', 'p%d' % k]) for k in range(6)]
    codes = [p.wait() for p in procs]
    got = read_text(target).splitlines()
    left = [x.name for x in d.iterdir() if x.name != 't.csv']
    ok = codes == [0] * 6 and len(got) == 240 and len(set(got)) == 240 and not left
    print('safe_write self-test: %s (exit codes %s, %d of 240 rows, leftovers %s)' % (
        'all passed' if ok else 'FAILED', codes, len(got), left or 'none'))
    return 0 if ok else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--worker':
        _worker(a[1], int(a[2]), a[3])
        sys.exit(0)
    if a == ['--self-test']:
        sys.exit(self_test())
    raise SystemExit(__doc__)

"""Move files or folders into the archive with a hash check and an index row (docs/CONSOLIDATION-PLAN.md, rule 2).

    python -X utf8 scripts/archive_move.py <bucket> <step> <reason> <path>... [--copy] [--dry]

<bucket> is the folder name under S:\\CurioClass-archive (for example codex-write-stubs-2026-11-24). Each path is
copied there keeping its path relative to its root (S:\\CurioClass when inside it, else the drive root), the copy's
sha256 is checked against the source, a row goes into S:\\CurioClass-archive\\INDEX.csv (archived_path, old_path, size,
sha256, date, step, reason), and only then is the source removed. --copy keeps the source; --dry prints and writes
nothing. Tracked files are refused unless --tracked is passed (2026-11-24: a glob once caught 290 committed
files). A folder is hashed by its sorted file list with each file's hash.
"""
import csv
import datetime
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

ARCHIVE = Path(r'S:\CurioClass-archive')
INDEX = ARCHIVE / 'INDEX.csv'
REPO = Path(__file__).resolve().parent.parent
FIELDS = ['archived_path', 'old_path', 'size', 'sha256', 'date', 'step', 'reason']


def fhash(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def tree(p):
    """(size, sha256) of a file, or of a folder's sorted relative paths and file hashes."""
    if p.is_file():
        return p.stat().st_size, fhash(p)
    h, size = hashlib.sha256(), 0
    for f in sorted(x for x in p.rglob('*') if x.is_file()):
        size += f.stat().st_size
        h.update(('%s %s\n' % (f.relative_to(p).as_posix(), fhash(f))).encode())
    return size, h.hexdigest()


def rel(p):
    try:
        return p.relative_to(REPO)
    except ValueError:
        return Path(*p.parts[1:])


def main(a):
    flags = {x for x in a if x.startswith('--')}
    a = [x for x in a if not x.startswith('--')]
    if len(a) < 4:
        raise SystemExit(__doc__)
    bucket, step, reason, paths = a[0], a[1], a[2], [Path(x).resolve() for x in a[3:]]
    rows = []
    for src in paths:
        if not src.exists():
            raise SystemExit('missing: %s' % src)
        if '--tracked' not in flags and REPO in src.parents:
            t = subprocess.run(['git', 'ls-files', '--', str(src)], cwd=REPO, capture_output=True, text=True).stdout
            if t.strip():
                raise SystemExit('tracked by git (use git rm, or pass --tracked on purpose): %s' % src)
        dst = ARCHIVE / bucket / rel(src)
        if dst.exists():
            raise SystemExit('already archived: %s' % dst)
        size, digest = tree(src)
        print('%s %s -> %s (%d bytes)' % ('would move' if '--dry' in flags else 'move', src, dst, size))
        if '--dry' in flags:
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        (shutil.copytree if src.is_dir() else shutil.copy2)(src, dst)
        if tree(dst) != (size, digest):
            raise SystemExit('hash mismatch, source kept: %s' % src)
        rows.append(dict(archived_path=str(dst), old_path=str(src), size=size, sha256=digest,
                         date=datetime.date.today().isoformat(), step=step, reason=reason))
        if '--copy' not in flags:
            (shutil.rmtree if src.is_dir() else Path.unlink)(src)
    if rows:
        new = not INDEX.exists()
        with open(INDEX, 'a', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, FIELDS)
            if new:
                w.writeheader()
            w.writerows(rows)
        print('%d row(s) added to %s' % (len(rows), INDEX))


if __name__ == '__main__':
    main(sys.argv[1:])

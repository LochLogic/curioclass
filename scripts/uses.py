"""What uses an object, by course and day (consolidation 4.F). Reads data/index.db (built by scripts/index.py).

    python -X utf8 scripts/uses.py <id>          an item id (s01-X2), a full key (item:<course>:s01-X2,
                                                 day:<course>:d042), a standard code (3.OA.A.1), a skill id, or a path
    python -X utf8 scripts/uses.py <id> --course <course>
    python -X utf8 scripts/uses.py --changed     what depends on the files changed since the last commit

Hard edges (links, leans_on, CSV ids) and soft ones (`mentions`: "day N" in plans, bare item ids in prose) are both
listed; soft ones are marked. The index is rebuilt first when it is missing or older than the newest data or page file
it reads (a rebuild takes seconds).
"""
import sqlite3
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import index  # noqa: E402


def stale():
    """True when any file the index reads is newer than data/index.db (a stat of the tracked and new files under data/,
    docs/ and courses/, about a second), so a lookup rebuilds only after a change."""
    if not index.DB.exists():
        return True
    built = index.DB.stat().st_mtime
    out = subprocess.run(['git', 'ls-files', '-co', '--exclude-standard', 'data', 'docs', 'courses'], cwd=ROOT,
                         capture_output=True, text=True).stdout
    for f in out.splitlines():
        try:
            if (ROOT / f).stat().st_mtime > built:
                return True
        except OSError:
            return True   # a file gone since the build
    return False


def fresh():
    if index.DB.exists() and ('--no-build' in sys.argv or not stale()):
        return
    ix = index.build()
    index.save(ix)


def targets(con, q, course=None):
    """Node keys and path keys the query names."""
    keys = set()
    if ':' in q and q.split(':', 1)[0] in ('item', 'day', 'unit', 'section', 'piece', 'code', 'prog', 'file', 'path',
                                            'source', 'course', 'tool', 'word'):
        keys.add(q)
    p = q.replace('\\', '/')
    if (ROOT / p).exists():
        keys.update({'path:' + p, 'file:' + p})
        keys.update(r[0] for r in con.execute('select key from nodes where path = ? and type in '
                                              '("piece", "day-file", "plan")', (p,)))
    for (k,) in con.execute('select key from nodes where local = ?', (q,)):
        keys.add(k)
    keys.add('code:' + q)
    if course:
        keys = {k for k in keys if (':%s:' % course) in k or k.startswith(('code:', 'path:', 'file:', 'word:'))}
    return keys


def show(con, keys, label):
    rows = []
    for k in sorted(keys):
        rows += con.execute('select src, dst, kind, hard, path, line, course, day from edges where dst = ?',
                            (k,)).fetchall()
    if not rows:
        print('%s: nothing uses it' % label)
        return 0
    rows = sorted(set(rows), key=lambda r: (r[4], r[5], r[2]))
    by = defaultdict(list)
    for r in rows:
        by[(r[6] or '-', r[7] if r[7] is not None else -1)].append(r)
    print('%s: %d use(s) in %d course(s)' % (label, len(rows), len({k[0] for k in by})))
    last = None
    for (c, d), rs in sorted(by.items()):
        if c != last:
            print('  %s' % c)
            last = c
        for src, dst, kind, hard, path, line, _, _ in sorted(set(rs), key=lambda r: (r[4], r[5])):
            print('    %s%s:%s %s%s' % ('day %d  ' % d if d >= 0 else '', path, line, kind, '' if hard else ' (soft)'))
    return len(rows)


def changed():
    out = subprocess.run(['git', 'diff', '--name-only', 'HEAD'], cwd=ROOT, capture_output=True, text=True).stdout
    out += subprocess.run(['git', 'ls-files', '-o', '--exclude-standard'], cwd=ROOT, capture_output=True,
                          text=True).stdout
    return sorted({x.strip() for x in out.splitlines() if x.strip()})


def main(a):
    if not a or a[0] in ('-h', '--help'):
        print(__doc__)
        return 2
    fresh()
    con = sqlite3.connect(index.DB)
    course = a[a.index('--course') + 1] if '--course' in a else None
    if '--changed' in a:
        files = changed()
        if not files:
            print('no files changed since the last commit')
            return 0
        for f in files:
            keys = targets(con, f, course)
            # a changed plan CSV: everything defined in it
            keys.update(r[0] for r in con.execute('select key from nodes where path = ?', (f,)))
            show(con, keys, f)
        return 0
    q = [x for x in a if not x.startswith('--') and x != course][0]
    show(con, targets(con, q, course), q)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

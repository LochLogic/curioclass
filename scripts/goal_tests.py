"""The 12 end-goal tests as numbers (docs/CONSOLIDATION-PLAN.md, "What each word means"; consolidation 4.J).

    python -X utf8 scripts/goal_tests.py            print the 12 counts
    python -X utf8 scripts/goal_tests.py --write    also write today's counts to data/plans/goal-tests.csv

gate.py runs it with --write after `--all --save`. data/plans/goal-tests.csv (test, name, count, target, detail, date)
keeps one row per test per date; SCALE.md and the Desk read it. A count at its target meets the test; a count above
it is the backlog that test measures (known misses sit in data/index-baseline.csv and later.csv, not here).
"""
import csv
import datetime
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
OUT = ROOT / 'data' / 'plans' / 'goal-tests.csv'
COLS = ['test', 'name', 'count', 'target', 'detail', 'date']


def git(*a):
    return subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True).stdout


HOMES = ['docs/courses/{c}/frame.md', 'docs/courses/{c}/scope-and-sequence.md', 'data/plans/{c}/days.csv',
         'data/plans/{c}/ledger.csv']


def missing_homes():
    """Each home a framed course (one with docs/courses/<course>/frame.md) lacks (close review finding 6)."""
    framed = sorted(p.parent.name for p in (ROOT / 'docs' / 'courses').glob('*/frame.md'))
    return [h.format(c=c) for c in framed for h in HOMES if not (ROOT / h.format(c=c)).exists()]


def tests():
    import homes
    import index
    import lint
    ix = index.build()
    index.save(ix)
    index.load_days()
    out = []

    def add(n, name, count, target, detail):
        out.append({'test': n, 'name': name, 'count': count, 'target': target, 'detail': detail})

    trees = [ln for ln in git('worktree', 'list').splitlines() if ln.strip()]
    add(1, 'one working folder', len(trees), 1, 'git worktrees (the main checkout counts as one)')
    lay = index.r_layout(ix)
    missing = missing_homes()
    add(2, 'every course has the same homes', len(lay) + len(missing), 0,
        'index layout report lines (data/homes.csv) plus %d home(s) a framed course lacks' % len(missing))
    drift = index.r_drift(ix)
    add(3, 'one home per fact', len(drift), 0, 'plans holding a stored <!-- skel --> block (the marker guard)')
    add(4, 'no curriculum list from the tool catalog', len(lint.catalog()), 0,
        'catalog lint lines over every script but the named tool-side set (two named exceptions, '
        'course_pages.known_standards and course_status.py placement counts, are outside the count)')
    t = time.time()
    subprocess.run([sys.executable, '-X', 'utf8', 'scripts/uses.py', 'word:runoff'], cwd=ROOT, capture_output=True)
    add(5, 'any object found by id', round(time.time() - t, 1), '<10', 'seconds for uses.py word:runoff, index fresh')
    rc = subprocess.run([sys.executable, '-X', 'utf8', 'scripts/rows.py', 'check'], cwd=ROOT, capture_output=True,
                        text=True).stdout
    m = re.search(r'(\d+) problems', rc)
    add(6, 'changes run as scripts, rows through rows.py', int(m[1]) if m else -1, 0,
        'a convention, not a test (4.L): plan CSVs rows.py check cannot split like the csv reader (a hand edit '
        'that broke a row); how a row was written cannot be read from the file')
    old = 0
    for p in list((ROOT / 'docs' / 'pipeline' / 'kit').glob('*.txt')) + list(
            (ROOT / 'docs' / 'pipeline' / 'briefs').glob('*.md')):
        old += len(re.findall(r'\{PLANGATE\}|\{LESSONGATE\}', p.read_text(encoding='utf-8')))
    add(7, 'one gate command', old, 0, 'old filtered gate placeholders left in the kit and briefs')
    gen = [ln for ln in homes.check() if ln.startswith('generated ')]
    add(8, 'generated things never stored twice', len(gen), 0, 'tracked files data/homes.csv marks generated-ignored')
    res = index.r_resolve(ix)
    known = {k for r, k in index.baseline() if r == 'resolve'}
    add(9, 'every relation resolves', len(res), 0,
        '%d misses, %d of them new against data/index-baseline.csv' % (len(res), sum(1 for k, _ in res if k not in known)))
    st = index.r_status(ix)
    add(10, 'one status per object', len(st), 0,
        'status report lines (flow-status rows a file contradicts; ledger rows at stage written with no day file)')
    import ids
    idl = [ln for ln in ids.check() + ids.left_tables() if ln.startswith('FAIL')]
    add(11, 'retired ids never reused', len(idl), 0, '%d retired ids recorded; also fails an item, day or source id that left its table since the last commit '
        'with no retire row' % len(ids.retired()))
    orph = index.r_orphans(ix)
    add(12, 'nothing orphaned', len(orph), 0, 'orphans report lines')
    return out


def write(rows):
    today = datetime.date.today().isoformat()
    old = []
    if OUT.exists():
        with open(OUT, encoding='utf-8', newline='') as f:
            old = [r for r in csv.DictReader(f) if r['date'] != today]
    with open(OUT, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, COLS, lineterminator='\n')
        w.writeheader()
        w.writerows(old + [dict(r, date=today) for r in rows])


def main(a):
    rows = tests()
    for r in rows:
        print('goal %2d %-46s %8s  (target %s) %s' % (r['test'], r['name'], r['count'], r['target'], r['detail']))
    if '--write' in a:
        write(rows)
        print('goal tests: written to %s' % OUT.relative_to(ROOT).as_posix())
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

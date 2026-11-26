"""The 16 end-goal tests as numbers (docs/CONSOLIDATION-PLAN.md, "What each word means"; consolidation 4.J; 13 to 16 from
the pedagogy-architecture review, change 14).

    python -X utf8 scripts/goal_tests.py            print the 16 counts
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
    """Each home a started course lacks (close review finding 6): a course-list.csv id with any of the four homes
    must have all four, so a deleted frame.md or a days.csv with no frame fails (Fable read of 4.L, finding 4).
    A listed course with none of them has not started and is not counted, and neither is one with its frame.md
    alone: a framed course gets its scope, days and ledger when its course run starts (2026-11-25, all 117 frames
    written before any after-core run)."""
    import csv
    with open(ROOT / 'data' / 'plans' / 'course-list.csv', encoding='utf-8', newline='') as f:
        ids = [r['id'] for r in csv.DictReader(f)]
    out = []
    for c in ids:
        have = [h for h in HOMES if (ROOT / h.format(c=c)).exists()]
        if have and have != [HOMES[0]]:
            out += [h.format(c=c) for h in HOMES if h not in have]
    return out


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
        'index layout report lines (data/homes.csv) plus %d home(s) a started course lacks' % len(missing))
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
    sk = {k for r, k in index.baseline() if r == 'status'}
    add(10, 'one status per object', len(st), 0,
        'status report lines, %d of them new against data/index-baseline.csv (flow-status rows a file contradicts; '
        'ledger and day files that disagree either way; day files with no version line; L133)'
        % sum(1 for k, _ in st if k not in sk))
    import ids
    idl = [ln for ln in ids.check() + ids.left_tables() if ln.startswith('FAIL')]
    add(11, 'retired ids never reused', len(idl), 0, '%d retired ids recorded; also fails an item, day or source id that left its table since the last commit '
        'with no retire row' % len(ids.retired()))
    orph = index.r_orphans(ix)
    add(12, 'nothing orphaned', len(orph), 0, 'orphans report lines')
    # 13 to 16: the curriculum goal tests (pedagogy-architecture review change 14, later.csv L141)
    gaps, units = unassessed_codes()
    add(13, 'every owned code assessed', len(gaps), 0,
        'frame Owned standards codes with no end item (items.csv check end) citing the code, a lettered part or its '
        'parent, over the %d units that have end items so far' % units)
    od = [r for r in index.rows_of(ROOT / 'data' / 'plans' / 'defects.csv') if r.get('status') == 'open']
    add(14, 'no open alignment defects', sum(1 for r in od if r.get('kind') == 'alignment'), 0,
        'open kind-alignment rows in data/plans/defects.csv (plan.py defect); %d open rows of every kind' % len(od))
    import contextlib
    import io
    import ledger
    tal = {}
    for s in ('math', 'ela', 'science', 'social-studies'):
        with contextlib.redirect_stdout(io.StringIO()):
            tal[s] = ledger.recheck_tally(s)[0]
    add(15, 'every review claim matches', sum(t['unmatched'] for t in tal.values()), 0,
        'ledger recheck citations that match no item or day row (ledger.recheck_tally, four core subjects; '
        '%d citations, %d flagged in all)' % (sum(t['citations'] for t in tal.values()),
                                              sum(t['flagged'] for t in tal.values())))
    below, total = days_below_read()
    add(16, 'every day read at grade close', below, 0,
        'day files whose version line has no "grade read" or "signed off" (day_version.py), of %d' % total)
    return out


def unassessed_codes():
    """[(course, unit, code)] for each owned code (frame Units table, Owned standards, ~ codes left out) of a unit
    with at least one end item, where no end item of the course cites the code, a lettered part of it or its parent."""
    import frame
    import index
    with open(ROOT / 'data' / 'plans' / 'course-list.csv', encoding='utf-8', newline='') as f:
        ids = [r['id'] for r in csv.DictReader(f)]
    gaps, units = [], 0
    for c in ids:
        if c in index.PILOT or not (ROOT / 'docs' / 'courses' / c / 'frame.md').exists():
            continue
        ends = [r for r in index.rows_of(ROOT / 'data' / 'plans' / c / 'items.csv') if r.get('check') == 'end']
        if not ends:
            continue
        cited = {x.strip().lstrip('~') for r in ends for x in frame.split_codes(r.get('code'))}
        have = {(r.get('stretch') or '').strip() for r in ends}
        for u in frame.parse(c)['table']:
            n = (u.get('#') or '').strip()
            if n not in have:
                continue
            units += 1
            cell = (u.get('Owned standards') or '').replace('`', '')
            for code in frame.split_codes(cell):
                if code.startswith('~') or code.lower() in ('none', 'none owned'):
                    continue
                part = any(x.startswith(code) and x[len(code):].isalpha() and x[len(code):].islower() for x in cited)
                parent = code[-1:].islower() and code[:-1] in cited
                if code not in cited and not part and not parent:
                    gaps.append((c, n, code))
    return gaps, units


def days_below_read():
    """(day files whose version line has no grade read and no signed off date, all day files), over every course."""
    import day_version as dv
    below = total = 0
    for d in sorted(p for p in (ROOT / 'courses').iterdir() if p.is_dir()):
        for f in dv.day_files(d.name):
            total += 1
            m = dv.LINE.search(f.read_text(encoding='utf-8')[:3000])
            p = dv.parse(m.group(1)) if m else {}
            if not (p.get('read') or p.get('signed')):
                below += 1
    return below, total


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

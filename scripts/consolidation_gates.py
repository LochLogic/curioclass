"""Before and after gates for each consolidation step (docs/CONSOLIDATION-PLAN.md, ground rule 3).

    python -X utf8 scripts/consolidation_gates.py run <step>              run every gate, save to docs/reviews/consolidation/<step>/
    python -X utf8 scripts/consolidation_gates.py compare <before> <after>  print lines new in <after>, gate by gate

Each gate's stdout and stderr go to <gate>.txt; summary.csv holds the gate, its exit code and its last line. The gates:
plan.py check and lesson_course.py per course with plan data, ledger.py check per subject, check_tools.py,
check_safety.py, board.py, desk_stats.py, course_status.py and the site build. board.py and course_status.py rewrite
docs/BUILD-BOARD.md and docs/COURSES-STATUS.md; commit or restore those before the step's own commit.
Output lines that only carry timings or counts of seconds are dropped before comparing.
"""
import csv
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'docs' / 'reviews' / 'consolidation'
PY = [sys.executable, '-X', 'utf8']
NOISE = re.compile(r'\b\d+(\.\d+)?\s*(s|sec|seconds|ms)\b|elapsed|took ', re.I)


def courses():
    return sorted(p.name for p in (ROOT / 'data' / 'plans').iterdir()
                  if p.is_dir() and p.name != 'ledgers' and (p / 'days.csv').exists())


def gates():
    g = [('plan-' + c, ['scripts/plan.py', 'check', c]) for c in courses()]
    g += [('lesson-' + c, ['scripts/lesson_course.py', c]) for c in courses()]
    g += [('ledger-' + s.stem, ['scripts/ledger.py', 'check', s.stem])
          for s in sorted((ROOT / 'data' / 'plans' / 'ledgers').glob('*.csv'))]
    g += [('check_tools', ['scripts/check_tools.py']), ('check_safety', ['scripts/check_safety.py']),
          ('board', ['scripts/board.py']), ('course_status', ['scripts/course_status.py']),
          ('build_site', ['scripts/build_site.py'])]
    return g


def run(step):
    d = OUT / step
    d.mkdir(parents=True, exist_ok=True)
    jobs = gates() + [('desk_stats', ['scripts/desk_stats.py', str(d / 'desk_stats.json')])]

    def one(job):
        name, args = job
        p = subprocess.run(PY + args, cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
        text = p.stdout + ('\n--- stderr ---\n' + p.stderr if p.stderr.strip() else '')
        (d / (name + '.txt')).write_text(text, encoding='utf-8')
        last = next((l for l in reversed(text.splitlines()) if l.strip()), '')
        return name, p.returncode, last[:200]

    serial = {'board', 'course_status', 'build_site', 'desk_stats'}   # these write shared files or the whole dist/
    par = [j for j in jobs if j[0] not in serial]
    with ThreadPoolExecutor(4) as ex:
        rows = list(ex.map(one, par))
    rows += [one(j) for j in jobs if j[0] in serial]
    with open(d / 'summary.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['gate', 'exit', 'last_line'])
        w.writerows(sorted(rows))
    bad = [r for r in rows if r[1] != 0]
    print('%d gates run into %s; %d exited non-zero: %s' % (len(rows), d.relative_to(ROOT), len(bad),
                                                           ', '.join(r[0] for r in sorted(bad)) or 'none'))


def lines(p):
    if not p.exists():
        return set()
    return {l.strip() for l in p.read_text(encoding='utf-8').splitlines() if l.strip() and not NOISE.search(l)}


def compare(a, b):
    da, db = OUT / a, OUT / b
    new = 0
    for f in sorted(db.glob('*.txt')):
        extra = sorted(lines(f) - lines(da / f.name))
        if extra:
            new += len(extra)
            print('== %s (%d new line(s))' % (f.stem, len(extra)))
            for l in extra[:40]:
                print('  ' + l)
    print('compare %s -> %s: %d new line(s)' % (a, b, new))


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) == 2 and a[0] == 'run':
        run(a[1])
    elif len(a) == 3 and a[0] == 'compare':
        compare(a[1], a[2])
    else:
        raise SystemExit(__doc__)

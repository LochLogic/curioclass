"""Before and after gates for each consolidation step (docs/CONSOLIDATION-PLAN.md, ground rule 3).

    python -X utf8 scripts/consolidation_gates.py run <step> [<glob> ...]   run the gates, or only those whose name matches
    python -X utf8 scripts/consolidation_gates.py compare <before> <after>  print lines new in <after>, gate by gate
    python -X utf8 scripts/consolidation_gates.py list                      print every gate name

Raw output goes to build/gates/<step>/<gate>.txt (ignored); summary.csv and, for compare, compare-<before>.txt go to
docs/reviews/consolidation/<step>/ and are the only files committed. Older steps kept their raw files in
docs/reviews/consolidation/<step>/, and compare reads them there when build/gates has none.

The gates: plan.py check, lesson_course.py and unitplan.py check per course with plan data, ledger.py check per subject
and `ledger.py files`, `rows.py check`, frame.py check, sequence.py check, the self-tests of the three skeleton scripts,
rows.py, safe_write.py and ledger.py, check_tools.py, check_safety.py, board.py,
desk_stats.py, course_status.py, and the site built with the deploy flags plus courses into build/gates/<step>/dist
(CURIO_DIST, never dist/), then check_site.py on that folder. board.py and course_status.py rewrite
docs/BUILD-BOARD.md and docs/COURSES-STATUS.md; commit or restore those before the step's own commit.
Output lines that only carry timings or counts of seconds are dropped before comparing.
"""
import csv
import fnmatch
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'docs' / 'reviews' / 'consolidation'
RAW = ROOT / 'build' / 'gates'
PY = [sys.executable, '-X', 'utf8']
NOISE = re.compile(r'\b\d+(\.\d+)?\s*(s|sec|seconds|ms)\b|elapsed|took ', re.I)
SITE = ['build_site', 'check_site']                      # run last, in this order, against one scratch folder
SERIAL = {'board', 'course_status', 'desk_stats'}         # these write shared files


def courses():
    return sorted(p.name for p in (ROOT / 'data' / 'plans').iterdir()
                  if p.is_dir() and (p / 'days.csv').exists())


def gates(raw):
    cs = courses()
    g = [('plan-' + c, ['scripts/plan.py', 'check', c]) for c in cs]
    g += [('lesson-' + c, ['scripts/lesson_course.py', c]) for c in cs]
    g += [('unitplan-' + c, ['scripts/unitplan.py', 'check', c]) for c in cs]
    sys.path.insert(0, str(ROOT / 'scripts'))
    import ledger
    g += [('ledger-' + s, ['scripts/ledger.py', 'check', s]) for s in sorted(ledger.LEDGER_SUBJECTS)]
    g += [('ledger-files', ['scripts/ledger.py', 'files']), ('rows-check', ['scripts/rows.py', 'check'])]
    g += [('frame', ['scripts/frame.py', 'check']), ('sequence', ['scripts/sequence.py', 'check'])]
    g += [('selftest-' + s, ['scripts/%s.py' % s, '--self-test'])
          for s in ('day_skeleton', 'section_skeleton', 'unit_skeleton', 'rows', 'safe_write', 'ledger')]
    g += [('check_tools', ['scripts/check_tools.py']), ('check_safety', ['scripts/check_safety.py']),
          ('board', ['scripts/board.py']), ('course_status', ['scripts/course_status.py']),
          ('desk_stats', ['scripts/desk_stats.py', str(raw / 'desk_stats.json')]),
          ('build_site', ['scripts/build_site.py', '--library', '--closet', '--courses']),
          ('check_site', ['scripts/check_site.py'])]
    return g


def run(step, pats):
    raw, d = RAW / step, OUT / step
    raw.mkdir(parents=True, exist_ok=True)
    d.mkdir(parents=True, exist_ok=True)
    jobs = [j for j in gates(raw) if not pats or any(fnmatch.fnmatch(j[0], p) for p in pats)]
    if not jobs:
        raise SystemExit('no gate matches %s' % ' '.join(pats))
    site = raw / 'dist'
    env = dict(os.environ, CURIO_DIST=str(site))

    def one(job):
        name, args = job
        p = subprocess.run(PY + args, cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace',
                           env=env)
        text = p.stdout + ('\n--- stderr ---\n' + p.stderr if p.stderr.strip() else '')
        (raw / (name + '.txt')).write_text(text, encoding='utf-8')
        last = next((l for l in reversed(text.splitlines()) if l.strip()), '')
        return name, p.returncode, last[:200]

    par = [j for j in jobs if j[0] not in SERIAL and j[0] not in SITE]
    with ThreadPoolExecutor(4) as ex:
        rows = list(ex.map(one, par))
    rows += [one(j) for j in jobs if j[0] in SERIAL]
    names = {j[0] for j in jobs}
    if 'build_site' in names:
        shutil.rmtree(site, ignore_errors=True)
        rows.append(one(('build_site', dict(gates(raw))['build_site'])))
    if 'check_site' in names:
        if not (site / 'index.html').exists():
            raise SystemExit('check_site needs build_site in the same run')
        rows.append(one(('check_site', ['scripts/check_site.py'])))
    with open(d / 'summary.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['gate', 'exit', 'last_line'])
        w.writerows(sorted(rows))
    bad = [r for r in rows if r[1] != 0]
    print('%d gates run into %s; %d exited non-zero: %s' % (len(rows), raw.relative_to(ROOT), len(bad),
                                                           ', '.join(r[0] for r in sorted(bad)) or 'none'))


def rawdir(step):
    return RAW / step if (RAW / step).exists() else OUT / step


def lines(p):
    if not p.exists():
        return set()
    return {l.strip() for l in p.read_text(encoding='utf-8').splitlines() if l.strip() and not NOISE.search(l)}


def compare(a, b):
    da, db = rawdir(a), rawdir(b)
    new, out = 0, []
    for f in sorted(db.glob('*.txt')):
        extra = sorted(lines(f) - lines(da / f.name))
        if extra:
            new += len(extra)
            out.append('== %s (%d new line(s))%s' % (f.stem, len(extra), '' if (da / f.name).exists() else ' [no before file]'))
            out += ['  ' + l for l in extra[:40]]
    out.append('compare %s -> %s: %d new line(s)' % (a, b, new))
    text = '\n'.join(out) + '\n'
    (OUT / b).mkdir(parents=True, exist_ok=True)
    (OUT / b / ('compare-%s.txt' % a)).write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == 'run':
        run(a[1], a[2:])
    elif len(a) == 3 and a[0] == 'compare':
        compare(a[1], a[2])
    elif a == ['list']:
        print('\n'.join(n for n, _ in gates(RAW / 'list')))
    else:
        raise SystemExit(__doc__)

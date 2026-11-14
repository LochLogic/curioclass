"""Write every unit plan of one course with Codex, one unit per run, in order.

Usage: python -X utf8 scripts/codex_units.py <course> [logdir=PATH] [tries=2]

For each unit: make the skeleton if missing (scripts/unit_skeleton.py), skip the unit if
scripts/unitplan.py already passes it, else run scripts/codex_write.py with
docs/pipeline/briefs/plan-codex.md (unit=, uu=). A unit that still fails after the tries
stops the course, since later units build on it. Logs go to logdir (default: system temp),
never under docs/reviews.
"""
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = [sys.executable, '-X', 'utf8']


def units(course):
    out = subprocess.run(PY + ['scripts/unit_skeleton.py', '--list'], cwd=ROOT, capture_output=True,
                         text=True, encoding='utf-8').stdout
    for line in out.splitlines():
        p = line.split()
        if p and p[0] == course:
            return int(p[1])
    raise SystemExit('unknown course ' + course)


def passes(course, uu):
    r = subprocess.run(PY + ['scripts/unitplan.py', 'check', course], cwd=ROOT, capture_output=True,
                       text=True, encoding='utf-8')
    name = 's%s.md' % uu
    return any(l.startswith('PASS') and l.rstrip().endswith(name) for l in r.stdout.splitlines())


def main(a):
    if not a:
        raise SystemExit(__doc__)
    course = a[0]
    opts = dict(x.split('=', 1) for x in a[1:])
    logdir = opts.get('logdir', tempfile.gettempdir())
    tries = int(opts.get('tries', '2'))
    os.makedirs(logdir, exist_ok=True)
    for u in range(1, units(course) + 1):
        uu = '%02d' % u
        path = os.path.join(ROOT, 'docs', 'courses', course, 's%s.md' % uu)
        if not os.path.exists(path):
            subprocess.run(PY + ['scripts/unit_skeleton.py', course, str(u)], cwd=ROOT, check=True)
        if passes(course, uu):
            print(course, uu, 'passes, skipped', flush=True)
            continue
        for t in range(1, tries + 1):
            log = os.path.join(logdir, 'codex-write-%s-s%s-try%d.log' % (course, uu, t))
            r = subprocess.run(PY + ['scripts/codex_write.py', 'docs/pipeline/briefs/plan-codex.md', course,
                                     'unit=%d' % u, 'uu=' + uu, 'log=' + log], cwd=ROOT)
            ok = passes(course, uu)
            print(course, uu, 'try', t, 'exit', r.returncode, 'PASS' if ok else 'FAIL', flush=True)
            if ok:
                break
        else:
            print(course, uu, 'STOPPED: still failing after', tries, 'tries', flush=True)
            return 1
    print(course, 'DONE', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

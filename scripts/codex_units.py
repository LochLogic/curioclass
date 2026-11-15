"""Write every unit plan of one course with Codex, one unit per run, in order.

Usage: python -X utf8 scripts/codex_units.py <course> [logdir=PATH] [tries=2]

For each unit of the course's days.csv (its real unit numbers): make the skeleton if missing
(scripts/unit_skeleton.py), skip the unit if scripts/unitplan.py already passes it, else run
scripts/codex_write.py with the subject's brief (docs/pipeline/briefs/plan-codex-<subject>.md
for math, ELA and science; plan-codex.md for social studies) and unit=, uu=. A unit that still
fails after the tries stops the course, since later units build on it; so does a skeleton that
cannot be made (its message is printed). Logs go to logdir (default: system temp), never under
docs/reviews.
"""
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = [sys.executable, '-X', 'utf8']
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import unit_skeleton as sk  # noqa: E402

BRIEFS = 'docs/pipeline/briefs'


def brief_for(subject):
    """The Codex brief of a subject: plan-codex-<subject>.md where it exists, else plan-codex.md (social studies)."""
    own = '%s/plan-codex-%s.md' % (BRIEFS, subject)
    return own if os.path.exists(os.path.join(ROOT, own)) else '%s/plan-codex.md' % BRIEFS


def units(course):
    """(subject, [unit numbers]) of a course, or SystemExit with a clear message."""
    subject = sk.subject_of(course)
    if subject is None:
        raise SystemExit('not a course in data/plans/frames.csv: %s' % course)
    sk.set_subject(subject)
    try:
        nums = sk.unit_numbers(course)
    except sk.DataError as e:
        raise SystemExit('codex_units: %s: %s' % (course, e))
    if not nums:
        raise SystemExit('%s has no days.csv yet' % course)
    return subject, nums


def passes(course, uu):
    r = subprocess.run(PY + ['scripts/unitplan.py', 'check', course], cwd=ROOT, capture_output=True,
                       text=True, encoding='utf-8')
    name = 's%s.md' % uu
    return any(l.startswith('PASS') and l.rstrip().endswith(name) for l in r.stdout.splitlines())


def main(a):
    if not a or a[0] in ('-h', '--help'):
        print(__doc__)
        return 0 if a else 2
    course = a[0]
    opts = {}
    for x in a[1:]:
        if '=' not in x:
            raise SystemExit('option %r is not key=value (logdir=PATH, tries=N)' % x)
        k, v = x.split('=', 1)
        opts[k] = v
    logdir = opts.get('logdir', tempfile.gettempdir())
    tries = int(opts.get('tries', '2'))
    os.makedirs(logdir, exist_ok=True)
    subject, nums = units(course)
    brief = brief_for(subject)
    print(course, 'brief', brief, 'units', sk.runs_text(nums), flush=True)
    for u in nums:
        uu = '%02d' % u
        path = os.path.join(ROOT, 'docs', 'courses', course, 's%s.md' % uu)
        if not os.path.exists(path):
            r = subprocess.run(PY + ['scripts/unit_skeleton.py', course, str(u)], cwd=ROOT, capture_output=True,
                               text=True, encoding='utf-8')
            if r.returncode != 0 or not os.path.exists(path):
                print((r.stdout + r.stderr).strip(), flush=True)
                print(course, uu, 'STOPPED: no skeleton', flush=True)
                return 1
        if passes(course, uu):
            print(course, uu, 'passes, skipped', flush=True)
            continue
        for t in range(1, tries + 1):
            log = os.path.join(logdir, 'codex-write-%s-s%s-try%d.log' % (course, uu, t))
            r = subprocess.run(PY + ['scripts/codex_write.py', brief, course,
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

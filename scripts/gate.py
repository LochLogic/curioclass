"""The one gate command (consolidation 4.G).

    python -X utf8 scripts/gate.py --course <id>     the course's gates; new lines against its stored baseline
    python -X utf8 scripts/gate.py --changed         the gates of every course the uncommitted changes touch, plus
                                                     the shared ones (and the self-tests if a script changed)
    python -X utf8 scripts/gate.py --all [--site]    every gate; --site also builds the site into the run folder
                                                     and runs check_site.py on it
    add --baseline to store this run as the scope's baseline (build/gates/base-<scope>/, ignored)
    add --save <name> to keep the run as build/gates/<name>/ with docs/reviews/consolidation/<name>/summary.csv
    python -X utf8 scripts/gate.py compare <a> <b>   new lines in run b against run a (folder names under build/gates)
    python -X utf8 scripts/gate.py list [--course <id> | --changed | --all]

Per course: plan.py check, lesson_course.py, unitplan.py check, ledger.py check for its subject, frame.py check, the
index reports (scripts/index.py) and lint (scripts/lint.py) for the course. --all adds ledger.py files, rows.py
check, the marker guard, sequence.py check, the self-tests (the skeletons, rows.py, safe_write.py, ledger.py,
index.py), lesson.py check, front_office.py check, check_tools.py, check_safety.py, board.py, course_status.py and
desk_stats.py. board.py and course_status.py rewrite docs/BUILD-BOARD.md and docs/COURSES-STATUS.md; commit or
restore them.

The compare prints, gate by gate, every line that is new (no cap in the stored file), and flags a gate that
disappeared, an exit code that changed and a count of failing lines that rose (a count that fell is reported once).
A new line fails when it is a FAIL line or a lint line; anything else new is shown as a note. The exit code is 1 when
anything fails, so turn.py, the lead, coursegen's gate lines and the consolidation runner all read one answer.
Output lines that only carry timings are dropped before comparing.
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
RAW = ROOT / 'build' / 'gates'
REVIEWS = ROOT / 'docs' / 'reviews' / 'consolidation'
PY = [sys.executable, '-X', 'utf8']
NOISE = re.compile(r'\b\d+(\.\d+)?\s*(s|sec|seconds|ms)\b|elapsed|took ', re.I)
FAILING = re.compile(r'\bFAIL\b|^(catalog|never-touch|generated|layout|style) ')
SITE = ['build_site', 'check_site']
SERIAL = {'board', 'course_status', 'desk_stats'}
SELFTESTS = ('vocabulary', 'day_skeleton', 'section_skeleton', 'unit_skeleton', 'rows', 'safe_write', 'ledger', 'index',
             'plan_facts', 'homes')

sys.path.insert(0, str(ROOT / 'scripts'))


def courses():
    """Every course the gate checks: the index's courses plus the pilot (math-4), which the index leaves out
    but the gate keeps checking until the pilot retires."""
    import index
    return index.courses() + sorted(p for p in index.PILOT if (index.DOCS / p).is_dir())


def subject_ledger(course):
    import ledger
    import unit_skeleton as u
    s = u.subject_of(course)
    names = {'ela': 'english-language-arts'}
    for x in (s, names.get(s)):
        if x in ledger.LEDGER_SUBJECTS:
            return x
    return None


def course_gates(c):
    g = [('plan-' + c, ['scripts/plan.py', 'check', c]), ('lesson-' + c, ['scripts/lesson_course.py', c]),
         ('unitplan-' + c, ['scripts/unitplan.py', 'check', c]), ('lint-' + c, ['scripts/lint.py', '--course', c])]
    s = subject_ledger(c)
    if s:
        g.append(('ledger-' + s, ['scripts/ledger.py', 'check', s]))
    return g


def shared():
    return [('frame', ['scripts/frame.py', 'check']), ('index-reports', ['scripts/index.py', '--reports']),
            ('rows-check', ['scripts/rows.py', 'check']), ('skel-guard', ['scripts/skel_strip.py', '--guard']),
            ('ids-check', ['scripts/ids.py', 'check']), ('vocabulary-check', ['scripts/vocabulary.py', 'check'])]   # homes.py check runs inside index-reports (the layout report)


def selftests():
    return [('selftest-' + s, ['scripts/%s.py' % s, '--self-test']) for s in SELFTESTS]


def changed():
    import lint
    return lint.changed()


def gates(scope, raw):
    """[(name, args)] for a scope: ('course', id), ('changed', None) or ('all', None)."""
    kind, arg = scope
    if kind == 'course':
        g = course_gates(arg) + shared()
    elif kind == 'changed':
        import lint
        files = changed()
        g = []
        for c in sorted(lint.courses_of(files) & set(courses())):
            g += course_gates(c)
        g += shared() + [('lint-changed', ['scripts/lint.py', '--changed'])]
        if any(f.startswith('scripts/') and f.endswith('.py') for f in files):
            g += selftests()
    else:
        g = []
        for c in courses():
            g += [x for x in course_gates(c) if not x[0].startswith('lint-')]
        g += shared() + selftests()
        g += [('ledger-files', ['scripts/ledger.py', 'files']), ('sequence', ['scripts/sequence.py', 'check']),
              ('lint-all', ['scripts/lint.py', '--all']), ('lesson-check', ['scripts/lesson.py', 'check']),
              ('front-office', ['scripts/front_office.py', 'check']),
              ('check_tools', ['scripts/check_tools.py']), ('check_safety', ['scripts/check_safety.py']),
              ('board', ['scripts/board.py']), ('course_status', ['scripts/course_status.py']),
              ('desk_stats', ['scripts/desk_stats.py', str(raw / 'desk_stats.json')])]
        if arg == 'site':
            g += [('build_site', ['scripts/build_site.py', '--library', '--closet', '--courses']),
                  ('check_site', ['scripts/check_site.py'])]
    seen, out = set(), []
    for n, a in g:
        if n not in seen:
            seen.add(n)
            out.append((n, a))
    return out


def run(scope, raw, pats=(), summary=None):
    if raw.exists():
        shutil.rmtree(raw, ignore_errors=True)
    raw.mkdir(parents=True, exist_ok=True)
    jobs = [j for j in gates(scope, raw) if not pats or any(fnmatch.fnmatch(j[0], p) for p in pats)]
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
        rows.append(one(('build_site', dict(jobs)['build_site'])))
    if 'check_site' in names:
        if not (site / 'index.html').exists():
            raise SystemExit('check_site needs build_site in the same run')
        rows.append(one(('check_site', ['scripts/check_site.py'])))
    rows.sort()
    for d in [raw] + ([summary] if summary else []):
        d.mkdir(parents=True, exist_ok=True)
        with open(d / 'summary.csv', 'w', encoding='utf-8', newline='') as f:
            w = csv.writer(f)
            w.writerow(['gate', 'exit', 'last_line'])
            w.writerows(rows)
    bad = [r for r in rows if r[1] != 0]
    print('%d gates run into %s; %d exited non-zero: %s' % (len(rows), raw.relative_to(ROOT).as_posix(), len(bad),
                                                           ', '.join(r[0] for r in bad) or 'none'))
    return rows


def rawdir(name):
    """A run folder: build/gates/<name>, or (older consolidation steps) docs/reviews/consolidation/<name>."""
    return RAW / name if (RAW / name).exists() else REVIEWS / name


def lines(p):
    if not p.exists():
        return set()
    return {l.strip() for l in p.read_text(encoding='utf-8').splitlines() if l.strip() and not NOISE.search(l)}


def exits(d):
    p = d / 'summary.csv'
    if not p.exists():
        p = REVIEWS / d.name / 'summary.csv'      # runs saved by the older runner keep it there
    if not p.exists():
        return {g.stem: '?' for g in d.glob('*.txt') if not g.stem.startswith('compare-')}
    return {r['gate']: r['exit'] for r in csv.DictReader(open(p, encoding='utf-8'))}


def compare_dirs(da, db, label, out_file=None, show=40):
    """Print what is new in run db against run da; return the number of failing findings."""
    out, fails, notes = [], 0, 0
    ea, eb = exits(da), exits(db)
    for g in sorted(set(ea) - set(eb)):
        out.append('== %s: GATE GONE (it ran in the baseline, not now)' % g)
        fails += 1
    for g in sorted(set(ea) & set(eb)):
        if ea[g] != eb[g] and '?' not in (ea[g], eb[g]):
            out.append('== %s: exit code %s -> %s' % (g, ea[g], eb[g]))
            fails += ea[g] == '0'
    for f in sorted(db.glob('*.txt')):
        before, now = lines(da / f.name), lines(f)
        ca = sum(1 for l in before if FAILING.search(l))
        cb = sum(1 for l in now if FAILING.search(l))
        extra = sorted(now - before)
        bad = [l for l in extra if FAILING.search(l)]
        head = []
        if cb > ca:
            head.append('failing lines %d -> %d' % (ca, cb))
        elif cb < ca:
            head.append('failing lines fell %d -> %d' % (ca, cb))
        if not extra and not head:
            continue
        fails += len(bad) + (1 if cb > ca and not bad else 0)
        notes += len(extra) - len(bad)
        out.append('== %s (%d new line(s), %d failing)%s%s' % (
            f.stem, len(extra), len(bad), '' if (da / f.name).exists() else ' [no baseline file]',
            ('; ' + '; '.join(head)) if head else ''))
        out += ['  FAIL-NEW ' + l if FAILING.search(l) else '  note ' + l for l in extra]
    out.append('%s: %d failing finding(s), %d new note line(s)' % (label, fails, notes))
    if out_file:
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text('\n'.join(out) + '\n', encoding='utf-8')
    shown, per = [], {}
    for l in out:
        if l.startswith('=='):
            per = {'n': 0}
            shown.append(l)
        elif l.startswith('  '):
            per['n'] = per.get('n', 0) + 1
            if per['n'] <= show:
                shown.append(l)
            elif per['n'] == show + 1:
                shown.append('  ... (the rest is in %s)' % (out_file.relative_to(ROOT).as_posix() if out_file
                                                             else 'the stored compare'))
        else:
            shown.append(l)
    print('\n'.join(shown))
    return fails


def scope_of(a):
    if '--course' in a:
        return ('course', a[a.index('--course') + 1]), a[a.index('--course') + 1]
    if '--changed' in a:
        return ('changed', None), 'changed'
    if '--all' in a:
        return ('all', 'site' if '--site' in a else None), 'all'
    raise SystemExit(__doc__)


def current_failures(raw, course=None):
    """Every failing line in this run (for a course scope: what the course's own gates print)."""
    out = []
    for f in sorted(raw.glob('*.txt')):
        for l in f.read_text(encoding='utf-8').splitlines():
            l = l.strip()
            if FAILING.search(l) and (not course or f.stem.endswith(course) or course in l):
                out.append('%s: %s' % (f.stem, l))
    return out


def main(a):
    if a[:1] == ['compare'] and len(a) == 3:
        return 1 if compare_dirs(rawdir(a[1]), rawdir(a[2]), 'compare %s -> %s' % (a[1], a[2]),
                                 REVIEWS / a[2] / ('compare-%s.txt' % a[1])) else 0
    if a[:1] == ['list']:
        scope, _ = scope_of(a[1:] or ['--all'])
        print('\n'.join(n for n, _ in gates(scope, RAW / 'list')))
        return 0
    scope, key = scope_of(a)
    pats = []
    if '--only' in a:
        pats = a[a.index('--only') + 1].split(',')
    if '--save' in a:
        name = a[a.index('--save') + 1]
        raw, summary = RAW / name, REVIEWS / name
    else:
        raw, summary = RAW / ('now-' + key), None
    run(scope, raw, pats, summary)
    base = RAW / ('base-' + key)
    if '--baseline' in a:
        if base.exists():
            shutil.rmtree(base)
        shutil.copytree(raw, base)
        print('baseline stored: %s' % base.relative_to(ROOT).as_posix())
        return 0
    if scope[0] == 'course':
        cur = current_failures(raw, scope[1])
        print('%d failing line(s) for %s now:' % (len(cur), scope[1]))
        print('\n'.join('  ' + l for l in cur))
    if not base.exists():
        print('no stored baseline for %s: the lines above are the whole answer (store one with --baseline)' % key)
        return 1 if scope[0] != 'course' and current_failures(raw) else 0
    return 1 if compare_dirs(base, raw, 'gate %s against its baseline' % key, raw / 'compare.txt') else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

"""Where every kind of file lives and who writes it: data/homes.csv (consolidation 4.H).

    python -X utf8 scripts/homes.py check         every tracked file has a home; generated-ignored files are not tracked
    python -X utf8 scripts/homes.py kind <path>   the row a path falls under
    python -X utf8 scripts/homes.py list <kind>   the patterns of one kind (never-touch, blind, pilot, ...)
    python -X utf8 scripts/homes.py briefs [--write]   rebuild each brief's "Never open (data/homes.csv kinds ...)" line

Patterns are globs over repository paths: `*` stays inside one folder, `**` crosses folders, `?` is one character,
`[...]` a character class. The first row that matches wins, so specific rows come before general ones.
Kinds: source, generated-ignored, generated-committed, state, frozen, never-touch, blind (never opened by any writer),
pilot (the math 4 pilot: blind to the plan briefs, open to math course runs), stray (inside a course home but not one
of its kinds of file: a layout line until it is moved).
Readers: lint.py (never-touch and generated guards), the index's layout report, turn.py (never-touch), and the
briefs and kit files, whose one "Never open (data/homes.csv kinds ...)" line is rendered from this file and checked.
"""
import csv
import re
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILE = ROOT / 'data' / 'homes.csv'
KINDS = ('source', 'generated-ignored', 'generated-committed', 'state', 'frozen', 'never-touch', 'blind', 'pilot',
         'stray')


def _rx(pattern):
    out, i = '', 0
    while i < len(pattern):
        c = pattern[i]
        if pattern.startswith('**', i):
            out += '.*'
            i += 2
            continue
        if c == '*':
            out += '[^/]*'
        elif c == '?':
            out += '[^/]'
        elif c == '[':
            j = pattern.index(']', i)
            out += pattern[i:j + 1]
            i = j + 1
            continue
        else:
            out += re.escape(c)
        i += 1
    return re.compile(out + r'\Z')


@lru_cache(None)
def rows():
    out = []
    for r in csv.DictReader(open(FILE, encoding='utf-8', newline='')):
        r['rx'] = _rx(r['pattern'])
        out.append(r)
    return out


COURSE_ROW = re.compile(r'(docs/courses|courses|data/plans)/\*/')
COURSE_PATH = re.compile(r'(docs/courses|courses|data/plans)/([^/]+)/')


@lru_cache(None)
def course_ids():
    p = ROOT / 'data' / 'plans' / 'course-list.csv'
    return {r['id'] for r in csv.DictReader(open(p, encoding='utf-8', newline=''))}


def row_of(path):
    """The first row that matches. A course row (a pattern with the course folder as `*`) matches only a folder that
    is a data/plans/course-list.csv id, so a made-up course has no home (close review finding 6)."""
    path = path.replace('\\', '/')
    for r in rows():
        if r['rx'].match(path):
            if COURSE_ROW.match(r['pattern']):
                m = COURSE_PATH.match(path)
                if m and m.group(2) not in course_ids():
                    return None
            return r
    return None


def kind(path):
    r = row_of(path)
    return r['kind'] if r else None


def patterns(*kinds):
    return [r['pattern'] for r in rows() if r['kind'] in kinds]


def readable(patterns_):
    """A pattern list as prose for a brief: folders end in /, `**x**` reads "any path containing x"."""
    out = []
    for p in patterns_:
        m = re.fullmatch(r'\*\*([^*/]+)\*\*', p)
        out.append('any path containing %s' % m.group(1) if m else p.replace('/**', '/'))
    return ', '.join(out)


BRIEF_LINE = re.compile(r'^Never open \(data/homes\.csv kinds ([a-z, -]+); scripts/homes\.py briefs keeps this line\): .*$',
                        re.M)
BRIEF_DIRS = ['docs/pipeline/briefs/*.md', 'docs/pipeline/kit/*.txt']


def brief_line(kinds):
    ks = [k.strip() for k in kinds.split(',')]
    bad = [k for k in ks if k not in KINDS]
    if bad:
        raise SystemExit('homes: unknown kind in a brief line: %s' % bad)
    return 'Never open (data/homes.csv kinds %s; scripts/homes.py briefs keeps this line): %s.' % (
        ', '.join(ks), readable(patterns(*ks)))


def briefs(write=False):
    """Every brief and kit line that names its never-open paths from homes.csv, rebuilt; lines for any that differ."""
    lines = []
    for g in BRIEF_DIRS:
        for p in sorted(ROOT.glob(g)):
            text = p.read_text(encoding='utf-8')
            new = BRIEF_LINE.sub(lambda m: brief_line(m.group(1)), text)
            if new != text:
                lines.append('generated %s: its never-open line differs from data/homes.csv (scripts/homes.py briefs '
                             '--write)' % p.relative_to(ROOT).as_posix())
                if write:
                    with open(p, 'w', encoding='utf-8', newline='') as f:
                        f.write(new)
    return lines


def tracked():
    out = subprocess.run(['git', '-c', 'core.quotepath=off', 'ls-files'], cwd=ROOT, capture_output=True,
                         text=True, encoding='utf-8').stdout
    return [x for x in out.splitlines() if x]


def course_files(course):
    """Every file in a course's three homes that git would see: tracked, plus untracked and not ignored, so a stray
    a writer just made fails that writer's gate (close review finding 6)."""
    out = subprocess.run(['git', '-c', 'core.quotepath=off', 'ls-files', '--cached', '--others', '--exclude-standard',
                          '--', 'docs/courses/' + course, 'courses/' + course, 'data/plans/' + course], cwd=ROOT,
                         capture_output=True, text=True, encoding='utf-8').stdout
    return sorted({x for x in out.splitlines() if x and (ROOT / x).exists()})


def check(files=None):
    """Lines for each tracked file with no home, and each tracked file whose home says it is never committed."""
    lines = []
    for f in files if files is not None else tracked():
        r = row_of(f)
        if r is None:
            lines.append('layout %s: no row in data/homes.csv' % f)
        elif r['kind'] == 'stray':
            lines.append('layout %s: %s' % (f, r['note']))
        elif r['kind'] == 'generated-ignored':
            lines.append('generated %s: tracked, but data/homes.csv says %s writes it and it is never committed'
                         % (f, r['owner']))
    return lines + briefs()


def self_test():
    bad = [r for r in rows() if r['kind'] not in KINDS]
    assert not bad, 'unknown kinds: %s' % [r['pattern'] for r in bad]
    for path, want in [('courses/math-grade-3/u01-1/d001.md', 'source'), ('docs/courses/math-4/DEFAULTS.md', 'pilot'),
                       ('docs/courses/biology/section-skeletons/s01.md', 'generated-ignored'),
                       ('closet/words/a.html', 'never-touch'), ('data/media-manifest.txt', 'state'),
                       ('data/modules/x.json', 'frozen'), ('docs/reviews/ela-6-x.md', 'blind'),
                       ('docs/BUILD-BOARD.md', 'generated-committed'), ('README.md', 'source')]:
        assert kind(path) == want, (path, kind(path), want)
    assert row_of('courses/biology/u01-1/d012a.md')['note'].startswith("a day's teaching")
    for path in ['docs/courses/biology/summary.md', 'docs/courses/biology/unit-notes.md',
                 'data/plans/biology/notes.csv', 'courses/newcourse-not-listed/u01-1/d001.md',
                 'data/plans/newcourse-not-listed/days.csv']:     # the close review's made-up paths
        assert kind(path) in (None, 'stray'), (path, kind(path))
    assert kind('data/plans/newcourse-not-listed/days.csv') is None
    print('homes self-test: all passed')
    return 0


def main(a):
    if a[:1] == ['check']:
        lines = check()
        print('\n'.join(lines))
        print('homes: %d tracked file(s) checked, %d line(s)' % (len(tracked()), len(lines)))
        return 1 if lines else 0
    if a[:1] == ['kind'] and len(a) == 2:
        r = row_of(a[1])
        print('%s: %s' % (a[1], ('%s (%s; owner %s; check %s) %s' % (r['kind'], r['pattern'], r['owner'],
                                                                     r['check'] or '-', r['note'])) if r else 'no home'))
        return 0
    if a[:1] == ['list'] and len(a) == 2:
        print('\n'.join(patterns(a[1])))
        return 0
    if a[:1] == ['briefs']:
        lines = briefs('--write' in a)
        print('\n'.join(lines) or 'homes: every never-open line matches data/homes.csv')
        return 1 if lines and '--write' not in a else 0
    if a == ['--self-test']:
        return self_test()
    raise SystemExit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

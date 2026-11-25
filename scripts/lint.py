"""Repository lint, run inside gate.py (consolidation 4.G).

    python -X utf8 scripts/lint.py [--course <id> | --changed | --all]

Checks (each line starts with the check's name, so a gate compare shows what is new):
- catalog: no curriculum script (CURRICULUM below) opens a tool catalog file (data/modules.csv, sequence.csv,
  coverage.csv, tools-concepts.csv, data/concepts/). One named exception until the standards pages are rebuilt:
  course_pages.py `known_standards` (docs/CONSOLIDATION-PLAN.md test 4).
- never-touch: a changed file whose data/homes.csv kind is never-touch or state (state files change only through
  their owner script, which the lead runs).
- generated and layout: scripts/homes.py check over the files in scope (all tracked files under --all): a file with
  no home, a stray in a course home, or a tracked file that homes.csv says is generated and never committed.
  Generated and committed files are checked by their own gate (homes.csv `check` column).
- style: an em dash, "Curio" not followed by " Class", or a UK spelling from the short US list below, in finished
  pages and plans (docs/courses/<course>/, courses/<course>/) and in what the generators print (each unit and section
  plan's rendered facts, scripts/plan_facts.py). Quoted titles keep their spelling: a word inside double quotes is
  skipped.

Exit 0 always: gate.py compares the lines against its stored baseline, so old lines are known and new ones fail there.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))

CURRICULUM = ['plan.py', 'plan_facts.py', 'plan_flow.py', 'unitplan.py', 'unit_skeleton.py', 'section_skeleton.py',
              'day_skeleton.py', 'lesson.py', 'lesson_course.py', 'ledger.py', 'rows.py', 'safe_write.py', 'frame.py',
              'coursegen.py', 'turn.py', 'index.py', 'uses.py', 'gate.py', 'lint.py', 'skel_strip.py',
              'front_office.py', 'front_office_docs.py', 'course_pages.py']
CATALOG = re.compile(r"modules\.csv|sequence\.csv|coverage\.csv|tools-concepts\.csv|data[/\\]concepts\b|"
                     r"'concepts'\)")
EXCEPTION = ('course_pages.py', 'known_standards')
EMDASH = '—'
UK = re.compile(r'\b(colour(?:s|ed|ing)?|centre(?:s|d)?|(?:centi|milli|kilo)?metres?|(?:milli)?litres?|'
                r'practis(?:e|es|ed|ing)|licences?|modelling|modelled|labell(?:ed|ing)|'
                r'behaviours?|favourites?|organis(?:e|es|ed|ing|ation|ations)|recognis(?:e|es|ed|ing)|'
                r'analys(?:e|ed|ing)|moulds?|programmes?|travell(?:ed|ing)|grey)\b', re.I)
QUOTED = re.compile(r'"[^"\n]*"|“[^”\n]*”')


def changed():
    out = subprocess.run(['git', 'diff', '--name-only', 'HEAD'], cwd=ROOT, capture_output=True, text=True).stdout
    out += subprocess.run(['git', 'ls-files', '-o', '--exclude-standard'], cwd=ROOT, capture_output=True,
                          text=True).stdout
    return sorted({x.strip() for x in out.splitlines() if x.strip()})


def courses_of(files):
    out = set()
    for f in files:
        m = re.match(r'(?:data/plans|docs/courses|courses)/([a-z0-9-]+)/', f)
        if m:
            out.add(m.group(1))
    return out


def catalog():
    out = []
    for name in CURRICULUM:
        if name == 'lint.py':          # it names the catalog files in order to look for them
            continue
        p = ROOT / 'scripts' / name
        if not p.exists():
            continue
        func = ''
        for i, ln in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            m = re.match(r'def (\w+)', ln)
            if m:
                func = m.group(1)
            if CATALOG.search(ln) and not ln.lstrip().startswith('#') and (name, func) != EXCEPTION:
                out.append('catalog scripts/%s:%d: a curriculum script reads a tool catalog file' % (name, i))
    return out


def never(files):
    import homes
    return ['never-touch %s: changed, and data/homes.csv marks it %s (owner %s)' % (f, r['kind'], r['owner'])
            for f in files for r in [homes.row_of(f)] if r and r['kind'] in ('never-touch', 'state')]


def style_text(where, text):
    """Style lines for one file, one per kind with its count, so an edit that only moves lines
    changes nothing, and one more hit changes the count (a new line for the gate compare)."""
    hits = {}
    for i, ln in enumerate(text.splitlines(), 1):
        found = []
        if EMDASH in ln:
            found.append('em dash')
        if re.search(r'\bCurio\b(?! Class)', ln):
            found.append('"Curio" not followed by " Class"')
        bare = QUOTED.sub(' ', re.sub(r'`[^`]*`|\]\([^)]*\)|https?://\S+', ' ', ln))
        found += ['UK spelling "%s"' % m.group(0).lower() for m in UK.finditer(bare)]
        for k in found:
            n, first = hits.get(k, (0, i))
            hits[k] = (n + 1, first)
    return ['style %s: %s x%d' % (where, k, n) for k, (n, _) in sorted(hits.items())]   # no line number: moves are not new


def style(course):
    import plan_facts as pf
    out = []
    for base in (ROOT / 'docs' / 'courses' / course, ROOT / 'courses' / course):
        if not base.is_dir():
            continue
        for p in sorted(base.rglob('*.md')):
            if 'skeletons' in p.parts:
                continue
            out += style_text(p.relative_to(ROOT).as_posix(), p.read_text(encoding='utf-8'))
    d = ROOT / 'docs' / 'courses' / course
    for p in sorted(d.glob('*.md')) if d.is_dir() else []:
        if pf.PLAN.fullmatch(p.name):
            try:
                text = pf.render(course, p.name)
            except Exception as e:            # a render error is the generator's own gate's business
                out.append('style render:%s/%s: render failed: %s' % (course, p.name, type(e).__name__))
                continue
            out += style_text('render:%s/%s' % (course, p.name), text)
    return out


def main(a):
    import index
    if '--course' in a:
        scope = [a[a.index('--course') + 1]]
        files = []
    elif '--changed' in a:
        files = changed()
        scope = sorted(courses_of(files))
    else:
        files = changed()
        import gate
        scope = gate.courses()
    import homes
    tracked = set(homes.tracked())
    lines = catalog() + never(files) + homes.check(None if '--all' in a or not ('--course' in a or '--changed' in a)
                                                   else [f for f in files if f in tracked])
    for c in scope:
        lines += style(c)
    print('\n'.join(lines))
    kinds = {}
    for ln in lines:
        kinds[ln.split(' ', 1)[0]] = kinds.get(ln.split(' ', 1)[0], 0) + 1
    print('lint: %d line(s) over %d course(s): %s' % (len(lines), len(scope),
                                                      ', '.join('%s %d' % kv for kv in sorted(kinds.items())) or 'none'))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

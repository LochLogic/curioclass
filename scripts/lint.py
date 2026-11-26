"""Repository lint, run inside gate.py (consolidation 4.G).

    python -X utf8 scripts/lint.py [--course <id> | --changed | --all]

Checks (each line starts with the check's name, so a gate compare shows what is new):
- catalog: no curriculum script opens a tool catalog file (data/modules.csv, sequence.csv, coverage.csv,
  tools-concepts.csv, data/concepts/). Every script under scripts/ is a curriculum script except the named tool-side
  set (TOOL_SIDE below, each with its reason), so a new script is linted by default. Two named exceptions
  (EXCEPTIONS): course_pages.py `known_standards`, until the standards pages are rebuilt, and course_status.py's
  module-level catalog placement counts (docs/CONSOLIDATION-PLAN.md test 4, close review finding 9). A curriculum
  script that imports a TOOL_SIDE module (`import build_db`, `from catalog_maps import ...`, import_module) fails
  too, since that module's loaders read the catalog for it (later.csv L134); lint.py itself may be imported.
- never-touch: a changed file whose data/homes.csv kind is never-touch or state (state files change only through
  their owner script, which the lead runs).
- generated and layout: scripts/homes.py check over the files in scope (--course: every file git would see in the
  course's homes, untracked too; --changed: changed and new files; --all: all tracked files): a file with
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

# Every script under scripts/ is a curriculum script except these, which exist to serve tools, the tool catalog, the
# Supply Closet or the tool site (close review finding 9: the list is inverted, so a new script is linted by default).
TOOL_SIDE = {
    'add_codes.py': 'module codes in data/modules/*.txt',
    'apply_ideas.py': 'tool idea cards into data/concepts/',
    'board.py': 'the tool build board',
    'build_db.py': 'builds the catalog itself',
    'build_site.py': 'the tool site and topic pages (course pages come from course_pages.py)',
    'catalog_batch.py': 'catalog review', 'catalog_compute.py': 'catalog review', 'catalog_maps.py': 'catalog review',
    'check_charts.py': 'Supply Closet charts', 'check_concepts.py': 'tool concepts', 'check_games.py': 'Supply Closet games',
    'check_plans.py': "tools' lesson plans", 'check_words.py': 'the Word Wall', 'check_words_review.py': 'the Word Wall',
    'check_worksheets.py': 'worksheet lists',
    'coverage_ledger.py': 'how the tools cover the standards (writes data/coverage.csv, a catalog file)',
    'desk_stats.py': 'tool counts for the Desk', 'gen_links.py': 'worksheet generator links on topic pages',
    'neighbors.py': 'tool spec context', 'rename_tools.py': 'tool renames', 'review_word_pictures.py': 'the Word Wall',
    'shape_courses.py': 'catalog shape (path step 3)', 'spec_fixes.py': 'tool spec fixes', 'teaching_map.py': 'the Map',
    'tool_bins.py': 'tool demand bins', 'tool_record.py': 'tool records', 'tool_stages.py': 'tool stages',
    'wordart.py': 'Word Wall pictures',
    'lint.py': 'it names the catalog files in order to look for them',
}
# Tool-side modules a curriculum script may import: lint.py is tool-side only because it names the catalog files.
IMPORT_OK = {'lint.py'}
# Imports of a tool-side module found when the import check was added (2026-11-26, later.csv L134): Supply Closet and
# tool scripts that are not in TOOL_SIDE. Known until the lead says which of them are tool-side; any other fails.
IMPORT_KNOWN = {('charts.py', 'check_charts'), ('refine_pack.py', 'tool_record'), ('wordpeople.py', 'check_words'),
                ('wordpeople.py', 'wordart'), ('wordsvg.py', 'check_words'), ('worksheets.py', 'check_worksheets'),
                ('ws_gen_propose.py', 'check_worksheets'), ('ws_generated.py', 'check_worksheets')}
CATALOG = re.compile(r"modules\.csv|sequence\.csv|coverage\.csv|tools-concepts\.csv|data[/\\]concepts\b|"
                     r"'concepts'\)")
# Named exceptions inside curriculum scripts: (script, function; '' = module level)
EXCEPTIONS = {('course_pages.py', 'known_standards'): 'until the standards pages are rebuilt',
              ('course_status.py', ''): "its catalog placement counts (docs/COURSES-STATUS.md's module column)"}
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
    for p in sorted((ROOT / 'scripts').glob('*.py')):
        name = p.name
        if name in TOOL_SIDE:
            continue
        func = ''
        for i, ln in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            m = re.match(r'def (\w+)', ln)
            if m:
                func = m.group(1)
            elif ln and not ln[0].isspace():
                func = ''                  # back at module level
            if CATALOG.search(ln) and not ln.lstrip().startswith('#') and (name, func) not in EXCEPTIONS:
                out.append('catalog scripts/%s:%d: a curriculum script reads a tool catalog file' % (name, i))
            for mod in imported(ln):     # a tool-side module's loaders read the catalog for it (L134)
                if (mod + '.py' in TOOL_SIDE and mod + '.py' not in IMPORT_OK and (name, func) not in EXCEPTIONS
                        and (name, mod) not in IMPORT_KNOWN):
                    out.append('catalog scripts/%s:%d: a curriculum script imports the tool-side %s.py' % (name, i, mod))
    return out


IMPORT = re.compile(r'^\s*(?:import\s+([\w.]+(?:\s+as\s+\w+)?(?:\s*,\s*[\w.]+(?:\s+as\s+\w+)?)*)|from\s+([\w.]+)\s+import\b)')
DYNAMIC = re.compile(r'''(?:import_module|__import__)\(\s*['"]([\w.]+)['"]''')


def imported(ln):
    """The top-level module names a line imports: `import a, b as c`, `from a import x`, importlib.import_module('a')
    and __import__('a')."""
    if ln.lstrip().startswith('#'):
        return []
    m = IMPORT.match(ln)
    names = []
    if m and m[1]:
        names = [x.split()[0] for x in m[1].split(',')]
    elif m:
        names = [m[2]]
    names += DYNAMIC.findall(ln)
    return [x.split('.')[0] for x in names if x]


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
    # layout: --course reads every file git would see in the course's homes, untracked ones too, and --changed every
    # changed or new file still on disk, so a stray a writer just made fails that writer's gate (close review 6)
    if '--course' in a:
        lay = homes.check(homes.course_files(scope[0]))
    elif '--changed' in a:
        lay = homes.check([f for f in files if (ROOT / f).exists()])
    else:
        lay = homes.check()
    lines = catalog() + never(files) + lay
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

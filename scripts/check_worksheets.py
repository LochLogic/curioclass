r"""Check the worksheet concept lists (docs/worksheets/<file>.md) against docs/WORKSHEETS-PLAN.md.

    python scripts/check_worksheets.py                 check every list, exit 1 on any problem
    python scripts/check_worksheets.py math ela        check some files
    python scripts/check_worksheets.py --units         list every unit: id, label, file
    python scripts/check_worksheets.py --modules <unit-id>   the modules a unit's sheets must cover

A unit is one class a teacher teaches: a grade of a K-12 subject (`ela-3`), a high school course (`algebra-1`) or a
language level (`spanish-novice-k5`). Each unit is a section in its file:

    ## ela-3: Grade 3 English Language Arts

    | # | Worksheet | Type | Module | Students |
    |---|---|---|---|---|
    | 1 | Who Is Telling? Point of View Sort | Practice | Point of View | Sort 12 sentences by narrator, then ... |

Module is a module title from data/modules.csv for that unit, or "-" when the unit has no modules yet.
"""
import csv, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / 'docs' / 'worksheets'
GRADES = ['k', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
LABEL = {g: 'Kindergarten' if g == 'k' else f'Grade {g}' for g in GRADES}
TYPES = {'Practice', 'Apply', 'Read and respond', 'Organizer', 'Diagram', 'Data and graphs', 'Lab', 'Map',
         'Timeline', 'Source analysis', 'Writing frame', 'Vocabulary', 'Review', 'Planner', 'Reflection', 'Log',
         'Critique', 'Puzzle'}
COUNT = (40, 50)
MIN_PER_MODULE = 2
WORDS = 30  # max words in the Students cell

# file -> [(course_id, mode)]; mode: 'grades' (one unit per grade), 'course' (one unit), 'levels' (language levels)
FILES = {
    'math': [('math-k8', 'grades'), ('algebra-1', 'course'), ('geometry', 'course'), ('algebra-2', 'course'),
             ('precalculus', 'course'), ('statistics', 'course'), ('calculus', 'course')],
    'ela': [('ela-k12', 'grades')],
    'science': [('science-k5', 'grades'), ('science-ms', 'grades'), ('earth-space', 'course'), ('biology', 'course'),
                ('chemistry', 'course'), ('physics', 'course'), ('environmental', 'course')],
    'social-studies': [('ss-k5', 'grades'), ('world-geo-6', 'course'), ('world-hist-7', 'course'),
                       ('us-hist-8', 'course'), ('world-hist-hs', 'course'), ('us-hist-hs', 'course'),
                       ('government', 'course'), ('economics', 'course'), ('psychology', 'course')],
    'visual-arts': [('visual-arts', 'grades')], 'media-arts': [('media-arts', 'grades')],
    'music': [('music', 'grades')], 'theater': [('theater', 'grades')], 'dance': [('dance', 'grades')],
    'health': [('health', 'grades')], 'pe': [('pe', 'grades')],
    'computer-science': [('cs-k12', 'grades')], 'library': [('library', 'grades')],
    'sel': [('sel-k12', 'grades')], 'eld': [('eld-k12', 'grades')],
    'world-languages': [('spanish', 'levels'), ('french', 'levels'), ('asl', 'levels')],
    'cte': [('cte-explore', 'grades'), ('cte-pathways', 'course'), ('personal-finance', 'course')],
}
LEVELS = [('novice-k5', 'Novice, grades K-5', 'Novice', 'k-5'), ('novice', 'Novice, grades 6-12', 'Novice', '6-12'),
          ('intermediate', 'Intermediate', 'Intermediate', '6-12'), ('advanced', 'Advanced', 'Advanced', '9-12')]


def span(g):
    """'3-5' -> {'3','4','5'}; 'k' -> {'k'}"""
    if '-' not in g:
        return {g}
    a, b = g.split('-')
    return set(GRADES[GRADES.index(a):GRADES.index(b) + 1])


def units():
    """unit id -> dict(label, file, modules=[titles])"""
    courses = {r['course_id']: r for r in csv.DictReader(open(ROOT / 'data' / 'courses.csv'))}
    mods = list(csv.DictReader(open(ROOT / 'data' / 'modules.csv')))
    out = {}
    for f, parts in FILES.items():
        for cid, mode in parts:
            c = courses[cid]
            mine = [m for m in mods if m['course_id'] == cid]
            if mode == 'course':
                out[cid] = dict(label=c['title'], file=f, modules=[m['title'] for m in mine])
            elif mode == 'grades':
                stem = cid.split('-k')[0] if cid.endswith(('-k12', '-k5', '-k8')) else cid
                for g in sorted(span(c['grades']), key=GRADES.index):
                    title = c['title'] if cid not in ('math-k8', 'science-k5', 'ss-k5') else \
                        {'math-k8': 'Math', 'science-k5': 'Science', 'ss-k5': 'Social Studies'}[cid]
                    out[f'{stem}-{g}'] = dict(label=f'{LABEL[g]} {title}', file=f,
                                              modules=[m['title'] for m in mine if g in span(m['grade'])])
            else:
                name = c['title'].split(' (')[0]
                for key, label, strand, grades in LEVELS:
                    if cid == 'french' and key == 'novice-k5':
                        continue
                    out[f'{cid}-{key}'] = dict(label=f'{name}, {label}', file=f,
                                               modules=[m['title'] for m in mine if m['strand'] == strand])
    return out


SECTION = re.compile(r'^## ([a-z0-9-]+): (.+)$', re.M)
ROW = re.compile(r'^\|\s*(\d+)\s*\|(.+)\|\s*$')


def check_file(f, U):
    path = DIR / f'{f}.md'
    if not path.exists():
        return [f'{f}: missing {path.relative_to(ROOT)}'], []
    text = path.read_text()
    problems, titles = [], []
    say = problems.append
    heads = list(SECTION.finditer(text))
    want = [u for u, d in U.items() if d['file'] == f]
    got = [m.group(1) for m in heads]
    if got != want:
        say(f'{f}: units {got}, want {want} in that order')
    for i, m in enumerate(heads):
        uid = m.group(1)
        if uid not in U:
            say(f'{f}: unknown unit {uid}')
            continue
        if m.group(2).strip() != U[uid]['label']:
            say(f'{uid}: heading label should be {U[uid]["label"]!r}')
        body = text[m.end():heads[i + 1].start() if i + 1 < len(heads) else len(text)]
        rows = [ROW.match(l) for l in body.splitlines()]
        rows = [r for r in rows if r]
        nums = [int(r.group(1)) for r in rows]
        if nums != list(range(1, len(rows) + 1)):
            say(f'{uid}: rows not numbered 1..{len(rows)}')
        if not COUNT[0] <= len(rows) <= COUNT[1]:
            say(f'{uid}: {len(rows)} worksheets, want {COUNT[0]}-{COUNT[1]}')
        mods = U[uid]['modules']
        used, seen = Counter(), set()
        for r in rows:
            cells = [c.strip() for c in r.group(2).split('|')]
            n = r.group(1)
            if len(cells) != 4:
                say(f'{uid} #{n}: {len(cells)} cells')
                continue
            title, kind, mod, does = cells
            key = re.sub(r'[^a-z0-9]+', ' ', title.lower()).strip()
            if not title or key in seen:
                say(f'{uid} #{n}: empty or repeated title {title!r}')
            seen.add(key)
            titles.append((uid, title))
            if kind not in TYPES:
                say(f'{uid} #{n}: type {kind!r}')
            if mods and mod not in mods:
                say(f'{uid} #{n}: module {mod!r} is not one of this unit\'s modules')
            if not mods and mod != '-':
                say(f'{uid} #{n}: unit has no modules, use "-"')
            used[mod] += 1
            w = len(does.split())
            if not 6 <= w <= WORDS:
                say(f'{uid} #{n}: Students cell has {w} words')
        for mt in mods:
            if used[mt] < MIN_PER_MODULE:
                say(f'{uid}: module {mt!r} has {used[mt]} sheets, want at least {MIN_PER_MODULE}')
        types = Counter(c for r in rows for c in [r.group(2).split('|')[1].strip()])
        if rows and types.most_common(1)[0][1] > 0.6 * len(rows):
            say(f'{uid}: one type is over 60% of the list')
        if len(types) < 4 and rows:
            say(f'{uid}: fewer than 4 types')
    if '—' in text:
        say(f'{f}: em dash')
    if re.search(r'\bCurio\b(?! Class)', text):
        say(f'{f}: "Curio" alone')
    return problems, titles


def main(args):
    U = units()
    if args[:1] == ['--units']:
        for u, d in U.items():
            print(f'{u}\t{d["label"]}\t{d["file"]}\t{len(d["modules"])} modules')
        return 0
    if args[:1] == ['--modules']:
        for u in args[1:]:
            print(f'{u}: {U[u]["label"]}')
            for m in U[u]['modules']:
                print(f'  {m}')
        return 0
    files = args or list(FILES)
    problems, total = [], 0
    for f in files:
        p, t = check_file(f, U)
        problems += p
        total += len(t)
    for p in problems:
        print(p)
    print(f'{total} worksheets checked, {len(problems)} problems')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

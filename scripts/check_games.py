r"""Check Family Game Night (data/closet/games/<game-id>.md) against docs/SUPPLY-CLOSET-PLAN.md, Phase E.

    python scripts/check_games.py            check every game, exit 1 on any problem
    python scripts/check_games.py rhyme-time check some games

A game file is "key: value" header lines, a blank line, then eight "## " sections: the four English ones, then the
four Spanish ones, in this order. modules lists module slugs for the game's grade and subject (math-3-area is
written "area"). materials and es_materials are ";"-separated. build_site.py uses load() for /closet/game-night/
and runs problems() so a bad game stops a closet build.
"""
import csv, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GAMES = ROOT / 'data' / 'closet' / 'games'
HEADER = ['title', 'es_title', 'grade', 'subject', 'modules', 'players', 'minutes', 'materials', 'es_materials']
SECTIONS = ['How to play', 'What your child is learning', 'Make it easier', 'Make it harder',
            'Cómo jugar', 'Qué está aprendiendo', 'Más fácil', 'Más difícil']
CORE = ['math', 'ela', 'science', 'social-studies']
PER_PAIR = (2, 3)
STEPS = (3, 8)
STEP_CAP, LEARN_CAP, TWEAK_CAP = 35, 45, 30  # words; Spanish gets 40% more
# Materials: paper, pencils, crayons, a deck of cards, dice, coins, a timer and ordinary household objects (the plan's
# list). Each item must name one of these; anything else is a problem until it is added here on purpose.
ALLOWED = re.compile(r'\b(paper|pencils?|pens?|crayons?|markers?|cards?|dice|die|coins?|pennies|timer|clock|phone|'
                     r'cups?|glass(es)?|bowls?|spoons?|plates?|water|ice|salt|pepper|sugar|rice|beans|buttons|books?|'
                     r'ruler|tape measure|tape|string|scissors|flashlight|lamp|ball|orange|toothpicks|towels?|'
                     r'objects?|things|wall|toys?|socks?|box|bag|pillowcase|household|packages?|labels?|magnets?|'
                     r'spoon|blanket|stuffed animals?|keys?|chairs?|table|tray|food|snacks?|newspaper|ads|'
                     r'magazines?|flyers?|calendar|map|globe|recipe|measuring cups?|leaves|rocks|sticks|'
                     r'jar|lid|straw|rubber bands?|paper clips?|envelopes?|sticky notes|containers?|blocks)\b', re.I)
READING = re.compile(r'\b(read|reads|write|writes|spell|spells)\b', re.I)


def load(names=None):
    """{game_id: game dict} for every game file (or just some)."""
    out = {}
    for f in sorted(GAMES.glob('*.md')):
        if names and f.stem not in names:
            continue
        text = f.read_text(encoding='utf-8')
        head, _, body = text.partition('\n\n')
        g = {'id': f.stem, 'file': f.name, 'url': f'/closet/game-night/{f.stem}/', 'bad_lines': []}
        for line in head.splitlines():
            k, sep, v = line.partition(':')
            if sep:
                g[k.strip()] = v.strip()
            else:
                g['bad_lines'].append(line)
        g['sections'] = [(m.group(1).strip(), m.group(2).strip())
                         for m in re.finditer(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)', body, re.M | re.S)]
        sec = dict(g['sections'])
        for i, (key, name) in enumerate(zip(['steps', 'learn', 'easier', 'harder'] * 2, SECTIONS)):
            k = key if i < 4 else 'es_' + key
            v = sec.get(name, '')
            g[k] = [re.sub(r'^\d+\.\s*', '', s).strip() for s in v.splitlines() if s.strip()] if key == 'steps' else ' '.join(v.split())
        g['module_slugs'] = [s.strip() for s in g.get('modules', '').split(',') if s.strip()]
        g['module_ids'] = [f"{g.get('subject')}-{g.get('grade')}-{s}" for s in g['module_slugs']]
        g['materials_list'] = [s.strip() for s in g.get('materials', '').split(';') if s.strip()]
        g['es_materials_list'] = [s.strip() for s in g.get('es_materials', '').split(';') if s.strip()]
        out[f.stem] = g
    return out


def words(s):
    return len(s.split())


def problems(g, modules):
    out, where = [], g['file']
    for line in g['bad_lines']:
        out.append(f'{where}: header line without a colon: {line!r}')
    for k in HEADER:
        if not g.get(k):
            out.append(f'{where}: {k} is missing')
    if [n for n, _ in g['sections']] != SECTIONS:
        out.append(f"{where}: sections must be {', '.join(SECTIONS)} in that order")
    if g.get('subject') not in CORE:
        out.append(f"{where}: subject {g.get('subject')!r} is not one of {', '.join(CORE)}")
    for mid in g['module_ids']:
        if mid not in modules:
            out.append(f'{where}: {mid} is not a module in data/modules.csv')
    if not g['module_ids']:
        out.append(f'{where}: no modules')
    m = re.fullmatch(r'(\d+)(?:-(\d+)|\+)?', g.get('players', ''))
    if not m or int(m.group(1)) != 2:
        out.append(f"{where}: players {g.get('players')!r} must start at 2 (one adult and one child), like 2-4 or 2+")
    if not g.get('minutes', '').isdigit() or not 15 <= int(g['minutes']) <= 20:
        out.append(f"{where}: minutes {g.get('minutes')!r} must be 15 to 20")
    for item in g['materials_list']:
        if not ALLOWED.search(item):
            out.append(f'{where}: material {item!r} is not on the allowed list (paper, pencils, cards, dice, coins, a timer, household objects)')
    if len(g['materials_list']) != len(g['es_materials_list']):
        out.append(f'{where}: materials and es_materials have different counts')
    for lang, pre, mult in (('English', '', 1), ('Spanish', 'es_', 1.4)):
        steps = g[pre + 'steps']
        if not STEPS[0] <= len(steps) <= STEPS[1]:
            out.append(f'{where}: {lang} has {len(steps)} steps, needs {STEPS[0]} to {STEPS[1]}')
        for i, s in enumerate(steps, 1):
            if words(s) > STEP_CAP * mult:
                out.append(f'{where}: {lang} step {i} is {words(s)} words, the cap is {int(STEP_CAP * mult)}')
        for k, cap in (('learn', LEARN_CAP), ('easier', TWEAK_CAP), ('harder', TWEAK_CAP)):
            if not g[pre + k]:
                out.append(f'{where}: {lang} {k} is empty')
            elif words(g[pre + k]) > cap * mult:
                out.append(f'{where}: {lang} {k} is {words(g[pre + k])} words, the cap is {int(cap * mult)}')
    if len(g['steps']) != len(g['es_steps']):
        out.append(f'{where}: English has {len(g["steps"])} steps, Spanish has {len(g["es_steps"])}')
    if g.get('grade') in ('k', '1'):
        for i, s in enumerate(g['steps'], 1):
            if READING.search(s) and not re.search(r'\b(grown-up|adult)\b', s, re.I):
                out.append(f'{where}: step {i} asks for reading or writing in a K-1 game (have the grown-up do it)')
    if re.search(r'\b[1-9K]\.[A-Z]{1,4}\.', g['learn']):
        out.append(f'{where}: learning line has a standard code; say it in plain words')
    text = '\n'.join(str(v) for k, v in g.items() if k in HEADER) + '\n' + '\n'.join(t for _, t in g['sections'])
    if '—' in text:
        out.append(f'{where}: em dash')
    if re.search(r'\bCurio\b(?! Class)', text):
        out.append(f'{where}: "Curio" without "Class"')
    return out


def gaps(games):
    """Core subject-grade pairs with too few or too many games."""
    n = Counter((g.get('grade'), g.get('subject')) for g in games.values())
    grades = ['k'] + [str(i) for i in range(1, 13)]
    return [f'grade {gr} {s}: {n[(gr, s)]} games, wants {PER_PAIR[0]} to {PER_PAIR[1]}'
            for gr in grades for s in CORE if not PER_PAIR[0] <= n[(gr, s)] <= PER_PAIR[1]]


def main():
    modules = {m['module_id']: m for m in csv.DictReader(open(ROOT / 'data' / 'modules.csv', encoding='utf-8'))}
    games = load(sys.argv[1:] or None)
    bad = [p for g in games.values() for p in problems(g, modules)]
    for p in bad:
        print('  -', p)
    short = gaps(games) if not sys.argv[1:] else []
    for p in short[:12]:
        print('  ~', p)
    print(f'{len(games)} games, {len(bad)} problems, {len(short)} subject-grade pairs outside {PER_PAIR[0]}-{PER_PAIR[1]}')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()

r"""Check anchor charts and posters (data/closet/charts/<module-id>.md, data/closet/posters/<id>.md) against
docs/SUPPLY-CLOSET-PLAN.md, Phase D.

    python scripts/check_charts.py              check every chart and poster, exit 1 on any problem
    python scripts/check_charts.py <id>...      check some

A chart file is "key: value" header lines, a blank line, then the parts. Every text line is "English | Spanish".

    layout: cycle                                   steps, parts, compare, cycle, big-idea, list (posters also: grid)
    title: The water cycle | El ciclo del agua
    idea: Water keeps moving. | El agua siempre se mueve.        (optional; big-idea needs one)
    example: ... | ...                                            (optional, a worked example under the chart)

    - Evaporation: The sun warms [[water]] into vapor. | Evaporación: El sol convierte el [[agua]] en vapor.
    ## Weather | Tiempo                              (compare only: starts a column; its "- " items follow)

"- Label: text" gives an item a label (parts and cycle need one; steps may have one). [[word]] is a blank on the
fill-in version and bold on the finished one. Posters also have "band: k2" (k2, 35, 68 or 912) and a "for:" line saying
where it hangs, and may set "color:" (a subject color name from curio.css), "theme:" (classic, bold or soft) and
"orient: landscape"; a drawn poster has "layout: grid", a "grid:" kind (see GRIDS) and no items ("range: -10 10" sets a
number line's ends). build_site.py uses load() and runs
problems() so a bad chart stops a closet build; scripts/charts.py draws them.
"""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHARTS = ROOT / 'data' / 'closet' / 'charts'
POSTERS = ROOT / 'data' / 'closet' / 'posters'
LAYOUTS = {'steps': (3, 6), 'parts': (3, 6), 'cycle': (3, 6), 'compare': (2, 3), 'big-idea': (2, 4), 'list': (6, 12),
           'grid': (0, 0)}
LABELED = {'parts', 'cycle'}
GRIDS = {'hundred', 'times', 'numberline', 'fractions', 'coordinate', 'unitcircle', 'coins', 'usmap', 'worldmap', 'periodic'}
LANDSCAPE = {'usmap', 'worldmap', 'periodic'}  # these grids only fit sideways
THEMES = {'classic', 'bold', 'soft'}
COLORS = {'math', 'ela', 'science', 'social', 'arts', 'health', 'cs', 'lang', 'cte', 'sel', 'eld', 'library', 'teal', 'accent'}
BANDS = {'k2', '35', '68', '912'}
TITLE_CAP, IDEA_CAP, ITEM_CAP, LABEL_CAP, BLANK_CAP = 9, 26, 22, 4, 3  # words; Spanish gets 40% more
COL_ITEMS = (2, 5)
BLANK = re.compile(r'\[\[(.+?)\]\]')


def pair(text):
    en, sep, es = text.partition(' | ')
    return en.strip(), es.strip() if sep else ''


def item(text):
    """(label, text) from 'Label: text', or (None, text). A label is short and comes before the first colon."""
    label, sep, rest = text.partition(': ')
    if sep and len(label.split()) <= LABEL_CAP and '[[' not in label:
        return label.strip(), rest.strip()
    return None, text.strip()


def parse(f, kind):
    text = f.read_text(encoding='utf-8')
    head, _, body = text.partition('\n\n')
    c = {'id': f.stem, 'kind': kind, 'file': f'{f.parent.name}/{f.name}', 'raw': text, 'bad_lines': [], 'items': [], 'cols': []}
    for line in head.splitlines():
        k, sep, v = line.partition(':')
        if sep:
            c[k.strip()] = v.strip()
        else:
            c['bad_lines'].append(line)
    for key in ('title', 'idea', 'example', 'for'):
        if key in c:
            c[key] = pair(c[key])
    col = None
    for line in body.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('## '):
            col = {'name': pair(line[3:]), 'items': []}
            c['cols'].append(col)
        elif line.startswith('- '):
            en, es = pair(line[2:])
            it = {'en': item(en), 'es': item(es)}
            (col['items'] if col else c['items']).append(it)
        else:
            c['bad_lines'].append(line)
    c['url'] = f'/modules/{f.stem}/chart/' if kind == 'chart' else f'/closet/anchor-charts/posters/{f.stem}/'
    return c


def load(kind='chart', names=None):
    """{id: chart dict} for every chart (kind='chart') or poster (kind='poster')."""
    folder = CHARTS if kind == 'chart' else POSTERS
    return {f.stem: parse(f, kind) for f in sorted(folder.glob('*.md')) if not names or f.stem in names}


def words(s):
    return len(BLANK.sub(lambda m: m[1], s).split())


def problems(c, modules=None):
    out, cid, lay = [], c['file'], c.get('layout')
    out += [f'{cid}: not a "key: value" header line: {b!r}' for b in c['bad_lines']]
    if lay not in LAYOUTS or (lay == 'grid' and c['kind'] != 'poster'):
        return out + [f"{cid}: layout {lay!r} must be one of {', '.join(k for k in LAYOUTS if k != 'grid')}"]
    if c['kind'] == 'chart' and modules is not None and c['id'] not in modules:
        out.append(f"{cid}: no module {c['id']} in data/modules.csv")
    if c['kind'] == 'poster':
        if c.get('band') not in BANDS:
            out.append(f"{cid}: band {c.get('band')!r} must be one of {', '.join(sorted(BANDS))}")
        if not c.get('for'):
            out.append(f'{cid}: posters need a "for:" line (what it is for, English | Spanish)')
        if c.get('color') and c['color'] not in COLORS:
            out.append(f"{cid}: color {c['color']!r} must be one of {', '.join(sorted(COLORS))}")
    if c.get('theme') and c['theme'] not in THEMES:
        out.append(f"{cid}: theme {c['theme']!r} must be one of {', '.join(sorted(THEMES))}")
    if c.get('orient') not in (None, 'landscape'):
        out.append(f"{cid}: orient can only be landscape")
    if lay == 'grid' and (c.get('grid') in LANDSCAPE) != (c.get('orient') == 'landscape'):
        out.append(f"{cid}: grid {c.get('grid')!r} {'needs' if c.get('grid') in LANDSCAPE else 'cannot have'} orient: landscape")
    if c.get('range') and not re.fullmatch(r'-?\d+ -?\d+', c['range']):
        out.append(f"{cid}: range must be two whole numbers, like -10 10")
    lines = []  # (where, en, es, cap)
    if not c.get('title'):
        out.append(f'{cid}: no title')
    else:
        lines.append(('title', *c['title'], TITLE_CAP))
    if c.get('idea'):
        lines.append(('idea', *c['idea'], IDEA_CAP))
    elif lay == 'big-idea':
        out.append(f'{cid}: a big-idea chart needs an idea: line')
    if c.get('example'):
        lines.append(('example', *c['example'], ITEM_CAP + 14))
    if c.get('for'):
        lines.append(('for', *c['for'], IDEA_CAP))
    lo, hi = LAYOUTS[lay]
    if lay == 'grid':
        if c.get('grid') not in GRIDS:
            out.append(f"{cid}: grid {c.get('grid')!r} must be one of {', '.join(sorted(GRIDS))}")
        if c['items'] or c['cols']:
            out.append(f'{cid}: a grid poster has no items')
    elif lay == 'compare':
        if c['items']:
            out.append(f'{cid}: compare items go under "## " columns')
        if not lo <= len(c['cols']) <= hi:
            out.append(f"{cid}: {len(c['cols'])} columns, compare needs {lo} to {hi}")
        for col in c['cols']:
            lines.append(('column', *col['name'], LABEL_CAP))
            if not COL_ITEMS[0] <= len(col['items']) <= COL_ITEMS[1]:
                out.append(f"{cid}: column {col['name'][0]!r} has {len(col['items'])} items, needs {COL_ITEMS[0]} to {COL_ITEMS[1]}")
    else:
        if c['cols']:
            out.append(f'{cid}: only compare charts have "## " columns')
        if not lo <= len(c['items']) <= hi:
            out.append(f"{cid}: {len(c['items'])} items, {lay} needs {lo} to {hi}")
    for i, it in enumerate(c['items'] + [x for col in c['cols'] for x in col['items']], 1):
        (le, te), (ls, ts) = it['en'], it['es']
        if lay in LABELED and not (le and ls):
            out.append(f'{cid}: item {i} needs a "Label: text" in both languages ({lay} charts label every part)')
        if bool(le) != bool(ls):
            out.append(f'{cid}: item {i} has a label in one language only')
        lines.append((f'item {i}', f'{le}: {te}' if le else te, f'{ls}: {ts}' if ls else ts, ITEM_CAP + LABEL_CAP))
    blanks = 0
    for where, en, es, cap in lines:
        if not es:
            out.append(f'{cid}: {where} has no Spanish (" | " then the Spanish)')
        if words(en) > cap:
            out.append(f'{cid}: {where} is {words(en)} words, the cap is {cap}')
        if es and words(es) > round(cap * 1.4):
            out.append(f'{cid}: {where} Spanish is {words(es)} words, the cap is {round(cap * 1.4)}')
        be, bs = BLANK.findall(en), BLANK.findall(es)
        if where in ('title', 'column', 'for') and (be or bs):
            out.append(f'{cid}: {where} cannot have a blank; blanks go in the idea, items and example')
        if len(be) != len(bs):
            out.append(f'{cid}: {where} has {len(be)} blanks in English and {len(bs)} in Spanish')
        out += [f'{cid}: blank [[{b}]] is more than {BLANK_CAP} words' for b in be + bs if len(b.split()) > BLANK_CAP]
        blanks += len(be)
    if lay != 'grid' and not 2 <= blanks <= 10:
        out.append(f'{cid}: {blanks} blanks; a fill-in version needs 2 to 10')
    if '—' in c['raw']:
        out.append(f'{cid}: em dash')
    if re.search(r'\bCurio\b(?! Class)', c['raw']):
        out.append(f'{cid}: "Curio" without "Class"')
    return out


def main():
    modules = {m['module_id'] for m in csv.DictReader(open(ROOT / 'data' / 'modules.csv', encoding='utf-8'))}
    names = sys.argv[1:] or None
    found = list(load('chart', names).values()) + list(load('poster', names).values())
    bad = 0
    for c in found:
        p = problems(c, modules)
        bad += bool(p)
        for line in p:
            print(line)
    charts = sum(c['kind'] == 'chart' for c in found)
    print(f'{charts} charts, {len(found) - charts} posters, {bad} with problems')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()

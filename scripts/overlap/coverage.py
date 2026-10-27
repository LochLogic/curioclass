"""Catalog-wide standards coverage, per framework and grade band, at three stages: live, live+specced, all planned.

    python scripts/overlap/coverage.py [--missing]

Fine frameworks are measured against the official lists in data/standards/*.txt (one id per line, `#` header):
CSTA 2026, NGSS performance expectations, CCSS math clusters, CCSS ELA standards, C3 indicators. Module codes coarser
or finer than the list are matched at the list's level (A-REI.A.2 counts for A-REI.A). Frameworks that modules.csv
codes only at top level (NCAS anchors, NHES, SHAPE, AASL, CASEL, WIDA, NSPFE) are measured as standard x band grids.
A tool is live when tools/<id>/tool.json exists and specced when tools/<id>/spec.md does. --missing prints the
uncovered ids. Codes in modules.csv that match no list entry are printed at the end (spelling or invalid codes).
"""
import csv, io, os, re, sys, collections
from common import ROOT

BANDS = ['K-2', '3-5', '6-8', '9-12']
GRADE_BAND = {'k': 'K-2', '1': 'K-2', '2': 'K-2', 'k-2': 'K-2', '3': '3-5', '4': '3-5', '5': '3-5', '3-5': '3-5',
              '6': '6-8', '7': '6-8', '8': '6-8', '6-8': '6-8', '9': '9-12', '10': '9-12', '11': '9-12', '12': '9-12',
              '9-12': '9-12', '9-10': '9-12', '11-12': '9-12'}


def grade_bands(g):
    g = g.lower()
    if g in GRADE_BAND: return [GRADE_BAND[g]]
    if g == 'k-12': return list(BANDS)
    if g == '6-12': return ['6-8', '9-12']
    if g == 'k-5': return ['K-2', '3-5']
    if g == '3-8': return ['3-5', '6-8']
    raise ValueError(g)


def band_of(fw, code):
    if fw == 'CSTA':
        p = code.split('-')[0]
        return {'EK': 'K-2', 'E1': 'K-2', 'E2': 'K-2', 'E3': '3-5', 'E4': '3-5', 'E5': '3-5', 'MS': '6-8', 'HS': '9-12'}[p]
    if fw == 'NGSS':
        p = code.rsplit('-', 2)[0] if code.count('-') == 3 else code.split('-')[0]
        return {'K': 'K-2', '1': 'K-2', '2': 'K-2', 'K-2': 'K-2', '3': '3-5', '4': '3-5', '5': '3-5', '3-5': '3-5',
                'MS': '6-8', 'HS': '9-12'}[p]
    if fw == 'CCSS-Math':
        if '-' in code.split('.')[0]: return '9-12'
        return GRADE_BAND[code.split('.')[0].lower()]
    if fw == 'CCSS-ELA':
        g = code.split('.')[1].lower()
        return GRADE_BAND.get(g) or '9-12'
    if fw == 'C3':
        return code.rsplit('.', 1)[1]


def at_level(fw, code):
    """Bring a module code to the list's level."""
    if fw == 'CCSS-Math':
        parts = code.split('.')
        return '.'.join(parts[:3]) if '-' not in parts[0] else '.'.join(parts[:2])
    if fw == 'CCSS-ELA':
        return re.sub(r'(\.\d+)[a-f]$', r'\1', code)
    return code


FINE = {'CSTA': 'csta-2026-ids.txt', 'NGSS': 'ngss-pes.txt', 'CCSS-Math': 'ccss-math-clusters.txt',
        'CCSS-ELA': 'ccss-ela-standards.txt', 'C3': 'c3-indicators.txt'}
GRIDS = {
    'NCAS anchors': (re.compile(r'^(VA|MU|TH|DA|MA):(Cr|Pr|Re|Cn)(\d+)$'),
                     [f'{d}:{p}{n}' for d in ('DA', 'MA', 'MU', 'TH', 'VA')
                      for p, n in [('Cr', 1), ('Cr', 2), ('Cr', 3), ('Pr', 4), ('Pr', 5), ('Pr', 6), ('Re', 7), ('Re', 8),
                                   ('Re', 9), ('Cn', 10), ('Cn', 11)]]),
    'NHES': (re.compile(r'^NHES\.S\d$'), [f'NHES.S{i}' for i in range(1, 9)]),
    'SHAPE': (re.compile(r'^SHAPE\.S\d$'), [f'SHAPE.S{i}' for i in range(1, 5)]),
    'AASL': (re.compile(r'^AASL\.'), [f'AASL.{x}' for x in ('Inquire', 'Include', 'Collaborate', 'Curate', 'Explore', 'Engage')]),
    'CASEL': (re.compile(r'^CASEL\.'), [f'CASEL.{x}' for x in ('Self-Awareness', 'Self-Management', 'Social Awareness',
                                                               'Relationship Skills', 'Responsible Decision-Making')]),
    'WIDA standards': (re.compile(r'^WIDA\.ELD-\d$'), [f'WIDA.ELD-{i}' for i in range(1, 6)]),
    'WIDA language uses': (re.compile(r'^WIDA\.[A-Z][a-z]+$'), [f'WIDA.{x}' for x in ('Narrate', 'Inform', 'Explain', 'Argue')]),
    'NSPFE': (re.compile(r'^NSPFE\.'), [f'NSPFE.{x}' for x in ('Earning Income', 'Spending', 'Saving', 'Investing',
                                                               'Managing Credit', 'Managing Risk')]),
}
GRID_BANDS = {'NSPFE': ['3-5', '6-8', '9-12']}  # NSPFE benchmarks are for grades 4, 8 and 12 only


def read_list(name):
    path = os.path.join(ROOT, 'data', 'standards', name)
    return [l.strip() for l in io.open(path, encoding='utf-8') if l.strip() and not l.startswith('#')]


def main():
    concepts = list(csv.DictReader(io.open(os.path.join(ROOT, 'data', 'tools-concepts.csv'), encoding='utf-8')))
    mods = {m['module_id']: m for m in csv.DictReader(io.open(os.path.join(ROOT, 'data', 'modules.csv'), encoding='utf-8'))}
    measure(concepts, mods, '--missing' in sys.argv)


def measure(concepts, mods, show_missing=False):
    """Print the coverage table. concepts: rows with tool_id and module_id; mods: module_id -> row with standards, grade.
    A concept row may carry stage='planned' to skip the tools/ lookup (staged tools in stage_check.py)."""
    stage_rank = {'live': 0, 'spec': 1, 'planned': 2}
    # code -> best stage carrying it; for grids, (code, band) -> best stage
    best, best_grid, all_codes = {}, {}, set()
    for t in concepts:
        tid = t['tool_id']
        st = t.get('stage') or ('live' if os.path.exists(os.path.join(ROOT, 'tools', tid, 'tool.json')) else
                                'spec' if os.path.exists(os.path.join(ROOT, 'tools', tid, 'spec.md')) else 'planned')
        m = mods[t['module_id']]
        for code in (c.strip() for c in m['standards'].split(';') if c.strip()):
            all_codes.add(code)
            if best.get(code, 'planned') != 'live' and (code not in best or stage_rank[st] < stage_rank[best[code]]):
                best[code] = st
            for b in grade_bands(m['grade']):
                k = (code, b)
                if k not in best_grid or stage_rank[st] < stage_rank[best_grid[k]]:
                    best_grid[k] = st

    matched = set()
    print('framework'.ljust(20), 'band'.ljust(6), 'live'.rjust(9), 'live+spec'.rjust(10), 'all'.rjust(9))
    for fw, fname in FINE.items():
        ids = read_list(fname)
        idset = set(ids)
        cover = {}
        for code, st in best.items():
            lv = at_level(fw, code)
            if lv in idset:
                matched.add(code)
                if lv not in cover or stage_rank[st] < stage_rank[cover[lv]]:
                    cover[lv] = st
        for b in BANDS + ['all']:
            ids_b = [i for i in ids if b == 'all' or band_of(fw, i) == b]
            if not ids_b: continue
            n = len(ids_b)
            c = [sum(1 for i in ids_b if i in cover and stage_rank[cover[i]] <= k) for k in range(3)]
            print(fw.ljust(20), b.ljust(6), *[f'{x}/{n}'.rjust(w) for x, w in zip(c, (9, 10, 9))])
        if show_missing:
            miss = [i for i in ids if i not in cover]
            print(f'  uncovered ({len(miss)}): {" ".join(miss)}')
    for fw, (pat, ids) in GRIDS.items():
        for code in all_codes:
            if pat.match(code): matched.add(code)
        fb = GRID_BANDS.get(fw, BANDS)
        for b in fb + ['all']:
            bs = fb if b == 'all' else [b]
            cells = [(i, x) for i in ids for x in bs]
            n = len(cells)
            c = [sum(1 for k in cells if k in best_grid and stage_rank[best_grid[k]] <= s) for s in range(3)]
            print(fw.ljust(20), b.ljust(6), *[f'{x}/{n}'.rjust(w) for x, w in zip(c, (9, 10, 9))])
        if show_missing:
            miss = [f'{i}@{x}' for i in ids for x in fb if (i, x) not in best_grid]
            print(f'  uncovered ({len(miss)}): {" ".join(miss)}')
    other = sorted(c for c in all_codes - matched)
    print(f'\nmodule codes outside every list ({len(other)}): {" ".join(other)}')


if __name__ == '__main__':
    main()

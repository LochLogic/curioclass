"""Concept-list rows backed by a Worksheet Generator (docs/WORKSHEETS-PLAN.md, "generator first").

    data/closet/worksheets/generated.csv      unit,n,gen,query,note
    python scripts/ws_generated.py            check the file: every row exists, no built sheet with the same number,
                                              every generator and every setting is real (reads the generator files)

A backed row keeps its title and its place in the year on the class page; its link opens the generator with the
settings in `query` (a URL query string, for example grade=3&skill=equiv&count=12). `note` says in a few words how
the generated sheet does what the row's Students line asks, for the reviewer. A row with a written sheet in
data/closet/worksheets/<unit>.md is not backed here: the written sheet wins.
"""
import csv, json, re, sys
from pathlib import Path
from urllib.parse import parse_qs

ROOT = Path(__file__).resolve().parent.parent
FILE = ROOT / 'data' / 'closet' / 'worksheets' / 'generated.csv'
GEN_DIR = ROOT / 'site' / 'assets' / 'gen'
REG = {g['id']: g for g in json.loads((ROOT / 'data/closet/generators.json').read_text(encoding='utf-8'))['generators']}


def load():
    """-> {unit: {n: dict(gen, query, note, url)}}"""
    out = {}
    if not FILE.exists():
        return out
    for r in csv.DictReader(FILE.open(encoding='utf-8', newline='')):
        if not r.get('unit'):
            continue
        u, n = r['unit'].strip(), int(r['n'])
        q = r['query'].strip()
        out.setdefault(u, {})[n] = dict(gen=r['gen'].strip(), query=q, note=r.get('note', '').strip(),
                                        url=f'/closet/worksheets/make/{r["gen"].strip()}/' + (f'?{q}' if q else ''))
    return out


def field_ids(gen):
    """The setting ids a generator file declares (id: 'x' inside its fields list)."""
    src = (GEN_DIR / f'{gen}.js').read_text(encoding='utf-8')
    m = re.search(r'fields:\s*\[(.*?)\n\s*\],', src, re.S)
    return set(re.findall(r"\bid:\s*'([a-z0-9_]+)'", m.group(1) if m else src))


def problems(rows=None, built=None):
    """rows: {unit: [concept rows]} and built: {unit: {n: ...}} from the build; loaded here when not given."""
    sys.path.insert(0, str(ROOT / 'scripts'))
    import check_worksheets as cw
    import worksheets as ws
    if rows is None:
        rows = {u: r for f in cw.FILES for u, r in cw.rows(f).items()}
    if built is None:
        built = {}
        for u in ws.built_units():
            try:
                built[u] = {s['n'] for s, _ in ws.load(u)[1]}
            except ws.SheetError:
                built[u] = set()
    out, seen = [], set()
    for u, byn in load().items():
        if u not in rows:
            out.append(f'generated.csv: unknown unit {u}')
            continue
        have = {r['n'] for r in rows[u]}
        for n, g in byn.items():
            if (u, n) in seen:
                out.append(f'generated.csv: {u} #{n} listed twice')
            seen.add((u, n))
            if n not in have:
                out.append(f'generated.csv: {u} #{n} is not in the concept list')
            if n in built.get(u, ()):
                out.append(f'generated.csv: {u} #{n} already has a written sheet')
            if g['gen'] not in REG or not (GEN_DIR / f'{g["gen"]}.js').exists():
                out.append(f'generated.csv: {u} #{n} names a generator that does not exist: {g["gen"]}')
                continue
            ids = field_ids(g['gen'])
            for k in parse_qs(g['query'], keep_blank_values=True):
                if k not in ids:
                    out.append(f'generated.csv: {u} #{n}: {g["gen"]} has no setting {k!r}')
            if not g['note']:
                out.append(f'generated.csv: {u} #{n} has no note')
    return out


if __name__ == '__main__':
    ps = problems()
    for p in ps:
        print(p)
    n = sum(len(v) for v in load().values())
    print(f'{n} generator-backed rows checked, {len(ps)} problems')
    sys.exit(1 if ps else 0)

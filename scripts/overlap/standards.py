"""Standards checks for move-to-gap. Usage: python scripts/overlap/standards.py
Prints (1) planned tools whose module standards are all carried by other tools in the same band (safe to re-point),
(2) CSTA 2026 coverage by concept prefix and level, from data/standards/csta-2026-ids.txt."""
import csv, io, os, re, collections
from common import load, ROOT

rows = load()
mods = {m['module_id']: m for m in csv.DictReader(io.open(os.path.join(ROOT, 'data', 'modules.csv'), encoding='utf-8'))}
def stds(r): return {s.strip() for s in mods[r['module_id']]['standards'].split(';') if s.strip()}

print('== planned tools whose standards are all covered elsewhere in their band')
for r in rows:
    if r['live'] == 'y': continue
    S = stds(r)
    others = set()
    for o in rows:
        if o is not r and set(o['bands']) & set(r['bands']): others |= stds(o)
    if S and S <= others: print(' ', r['tool_id'], r['band'], r['subject'], sorted(S))

ids = [l.strip() for l in io.open(os.path.join(ROOT, 'data', 'standards', 'csta-2026-ids.txt'), encoding='utf-8') if l.strip()]
used = set()
for m in mods.values(): used |= {s.strip() for s in m['standards'].split(';')}
miss = [i for i in ids if i not in used]
print(f'\n== CSTA: {len(ids) - len(miss)} of {len(ids)} identifiers on a module; {len(miss)} uncovered')
grid = collections.defaultdict(lambda: [0, 0])
for i in ids:
    level, a, b = i.split('-')[:3]
    k = (f'{a}-{b}', level)
    grid[k][1] += 1
    if i in used: grid[k][0] += 1
levels = sorted({k[1] for k in grid}, key=lambda x: (x[0] != 'E', x))
print('concept'.ljust(8), *[l.ljust(6) for l in levels])
for c in sorted({k[0] for k in grid}):
    print(c.ljust(8), *[(f'{grid[(c, l)][0]}/{grid[(c, l)][1]}' if (c, l) in grid else '-').ljust(6) for l in levels])

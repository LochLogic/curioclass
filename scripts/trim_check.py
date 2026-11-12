"""Check the worksheet trim proposals in docs/agents/trim/<subject>.csv against docs/agents/trim/input/.

    python scripts/trim_check.py        per subject: cuts vs target, rule breaks, thin modules
"""
import csv, collections
from pathlib import Path
D = Path(__file__).resolve().parent.parent / 'docs/agents/trim'
units = {r['unit']: r for r in csv.DictReader(open(D / 'input/units.csv', encoding='utf8'))}
PROTECT = {'Lab', 'Map', 'Source analysis', 'Critique', 'Puzzle', 'Writing frame', 'Data and graphs'}
tot = 0
for f in sorted(p for p in D.glob('*.csv')):
    rows = list(csv.DictReader(open(D / 'input' / f.name, encoding='utf8')))
    cuts = list(csv.DictReader(open(f, encoding='utf8')))
    by = {(r['unit'], r['n']): r for r in rows}
    cutset = {(c['unit'], c['n']) for c in cuts}
    bad = [k for k in cutset if k not in by or by[k]['status'] != 'open']
    cnt = collections.Counter(u for u, _ in cutset)
    miss = [(u, cnt[u], int(units[u]['cut_target'])) for u in {r['unit'] for r in rows} if abs(cnt[u] - int(units[u]['cut_target'])) > 2]
    thin, lost = 0, []
    for u in {r['unit'] for r in rows}:
        ur = [r for r in rows if r['unit'] == u]
        kept = [r for r in ur if (u, r['n']) not in cutset]
        mods = collections.Counter(r['module'] for r in kept)
        thin += sum(1 for m in {r['module'] for r in ur} if mods[m] < 2)
        lost += [f'{u}:{t}' for t in PROTECT if any(r['type'] == t for r in ur) and not any(r['type'] == t for r in kept)]
    dash = sum('—' in (c.get('reason') or '') for c in cuts)
    tot += len(cutset)
    print(f'{f.stem}: {len(cutset)} cuts, bad {len(bad)}, off-target {miss or 0}, topics under 2: {thin}, protected lost {lost or 0}, dashes {dash}')
print('total', tot)

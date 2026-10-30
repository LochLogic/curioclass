from suite import *
from build import empty, stock
s = new_pond(); run(s, 520)
print('Af max per year', [round(max(r['Af'] for r in s['hist'][y*52:(y+1)*52])) for y in range(10)])
for y in range(10):
    h = s['hist'][y*52:(y+1)*52]
    pm = max(h, key=lambda r: r['M'])['week'] % 52; ps = max(h, key=lambda r: r['S'])['week'] % 52; pd = max(h, key=lambda r: r['Dn'])['week'] % 52
    print('  y%d peaks S %d M %d Dn %d' % (y+1, ps, pm, pd))
for wk in (13, 26, 52+13):
    g = new_pond(); run(g, wk+104); t = new_pond(); run(t, wk+104, {wk: lambda s: remove_all(s, 'Dn')})
    w = first(t, lambda r: r['week'] > wk and r['S'] >= 30)
    print('net nymphs at', yw(wk), 'snails >=60 cutouts at', yw(w), 'weeks', (w-wk) if w else None, 'max', round(max(r['S'] for r in t['hist'][wk:])/.5))
# rescue
t = new_pond(); run(t, 52*5, {0: lambda s: s.update(decomp_on=False), 78: lambda s: (s.update(decomp_on=True), add(s, 'D', 5)), 78+30: lambda s: stock(s, nymphs=6, turtles=1, snails=10, minnows=6)})
print('rescue gone at end y5', present(t), 'log', t['log'][:6])
t = new_pond(); run(t, 52*5, {0: lambda s: s.update(decomp_on=False), 78: lambda s: (s.update(decomp_on=True), add(s, 'D', 5))})
print('choke no restock y5 gone', present(t))
r = [x for x in t['hist'] if x['week'] == 78][0]; print('at decomp back: Af %.1f As %.1f S %.2f M %.2f Dn %.2f turtles %d muck%% %.0f' % (r['Af'], r['As'], r['S'], r['M'], r['Dn'], r['turtles'], 100*r['Det']/total(t)))
# heron off from netting minnows
t = new_pond(); run(t, 104, {13: lambda s: remove_all(s, 'M')}); print('net minnows log', t['log'][:5])

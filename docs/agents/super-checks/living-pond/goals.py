from suite import *
from build import empty, stock
import copy

def yearsum(s, y, k): return sum(r['acc'][k] for r in s['hist'][y*52:(y+1)*52])

print('== energy per year: caught vs heat (percent gap)')
s = new_pond(); run(s, 520)
print('  ', [round(100*(yearsum(s, y, 'resp')-yearsum(s, y, 'G'))/yearsum(s, y, 'G'), 1) for y in range(10)])
print('  sunlight caught per year %%: ', [round(100*10*yearsum(s, y, 'G')/yearsum(s, y, 'sun'), 2) for y in range(10)])
print('  plant-eaters kept as %% of algae kept: ', [round(100*(yearsum(s, y, 'prod_snail')+yearsum(s, y, 'prod_minnow')-yearsum(s, y, 'maint_snail')-yearsum(s, y, 'maint_minnow'))/(yearsum(s, y, 'G')-yearsum(s, y, 'aresp')), 1) for y in range(10)])
print('  heron catch per year (units): ', [round(yearsum(s, y, 'eat_heron'), 1) for y in range(10)])

print('== feeder settings (weeks 6-38 each year)')
def feeder(amt): return {y*52+w: (lambda s, a=amt: add(s, 'F', a)) for y in range(10) for w in range(6, 39)}
for lab, amt in (('Some 3', 3), ('Some 4', 4), ('Lots 10', 10), ('Lots 12', 12), ('Lots 15', 15)):
    s = new_pond(); run(s, 520, feeder(amt))
    g = first(s, lambda r: r['M'] == 0); o = first(s, lambda r: r['O'] < 2)
    winters = []
    for y in range(10):
        a = s['hist'][y*52+40]['M']; b = s['hist'][y*52+51]['M']
        winters.append(round(100*(1-b/a)) if a > 0 else None)
    print('  %-8s O<2 first %s, minnows gone %s, gone at end %s, Omin per yr %s, winter minnow loss %% %s' % (lab, yw(o), yw(g), present(s), [round(min(r['O'] for r in s['hist'][y*52:(y+1)*52]), 1) for y in range(10)], winters))
s = new_pond(); run(s, 520)
print('  no feeder winter minnow loss %%', [round(100*(1-s['hist'][y*52+51]['M']/s['hist'][y*52+40]['M'])) for y in range(10)])

print('== ghost comparison: net minnows y1w13; snails and turtle vs ghost')
ghost = new_pond(); run(ghost, 104)
s = new_pond(); run(s, 104, {13: lambda s: remove_all(s, 'M')})
for w in (13, 20, 26, 39, 52, 65, 78):
    print('   %s snails %.1f (ghost %.1f) As %.1f (ghost %.1f) Af %.0f (ghost %.0f) turtles %d' % (yw(w), s['hist'][w]['S'], ghost['hist'][w]['S'], s['hist'][w]['As'], ghost['hist'][w]['As'], s['hist'][w]['Af'], ghost['hist'][w]['Af'], s['hist'][w]['turtles']))
w_half = first(s, lambda r: r['week'] > 13 and r['S'] < 0.5 * ghost['hist'][r['week']]['S'])
print('  snails under half of ghost at', yw(w_half), 'weeks after netting', (w_half - 13) if w_half else None)
print('  snails gone', yw(first(s, lambda r: r['S'] == 0)))

print('== ghost: net minnows at other times (weeks to snails under half of ghost)')
for wk in (0, 13, 26, 39, 52+13, 260+13):
    gh = new_pond(); run(gh, wk + 104)
    s = new_pond(); run(s, wk + 104, {wk: lambda s: remove_all(s, 'M')})
    w_half = first(s, lambda r: r['week'] > wk and r['S'] < 0.5 * gh['hist'][r['week']]['S'])
    print('   netted at %s: snails < half ghost after %s weeks; snails gone %s' % (yw(wk), (w_half - wk) if w_half else None, yw(first(s, lambda r: r['week'] > wk and r['S'] == 0))))

print('== net half the minnows y1w13 (not all)')
s = new_pond(); run(s, 104, {13: lambda s: s.update(M=[x/2 for x in s['M']], ledger=dict(s['ledger'], removed=s['ledger']['removed']+Mt(s)/2))})
print('  Af max %.0f snails min %.1f gone %s' % (max(r['Af'] for r in s['hist'][13:104]), min(r['S'] for r in s['hist'][13:104]), present(s)))

print('== camouflage then heron removed: does shade hold?')
s = new_pond(); run(s, 520, {260: lambda s: remove_all(s, 'heron')})
print('  y5 %.2f y6 %.2f y8 %.2f y10 %.2f' % (s['hist'][259]['color'], s['hist'][311]['color'], s['hist'][415]['color'], s['hist'][519]['color']))

print('== gravel bottom: spread of shades')
def spread(r):
    m = sum(r['Mbins']); mu = sum(k*x for k, x in enumerate(r['Mbins']))/m
    return (sum((k-mu)**2*x for k, x in enumerate(r['Mbins']))/m) ** 0.5, 100*sum(r['Mbins'][3:5])/m
for b in (3.5, 1.0):
    s = new_pond(bottom=b); run(s, 520)
    print('  bottom %.1f: sd y0 %.2f y5 %.2f y10 %.2f; share in shades 3-4: %.0f%% -> %.0f%%' % (b, spread(s['hist'][0])[0], spread(s['hist'][259])[0], spread(s['hist'][519])[0], spread(s['hist'][0])[1], spread(s['hist'][519])[1]))

print('== hunters too soon (small build), when do nymphs die, and prey then')
s = empty(); run(s, 104, {0: lambda s: stock(s, algae=4, snails=6, minnows=3, nymphs=2, turtles=1, herons=1)})
w = first(s, lambda r: r['week'] > 0 and r['Dn'] == 0); r = s['hist'][w]
print('  nymphs gone', yw(w), 'snails %.1f minnows %.1f O %.1f' % (r['S'], r['M'], r['O']))
s = empty(); run(s, 520, {0: lambda s: stock(s, algae=4, snails=6, minnows=3), 52: lambda s: stock(s, nymphs=2, turtles=1, herons=1)})
print('  same stock but hunters a year later: gone at end', present(s), 'Dn y10', rng(s, 'Dn', 9))

print('== boom and bust: add 30 minnows y1w13')
s = new_pond(); run(s, 104, {13: lambda s: add(s, 'M', 60)})
m0 = s['hist'][13]['M']; pk = max(s['hist'][13:65], key=lambda r: r['M'])
low = min(s['hist'][13:65], key=lambda r: r['M'])
print('  after add %.1f (%.0f minnows), peak %.1f at %s, low %.1f at %s; start before add %.1f' % (m0, m0/2, pk['M'], yw(pk['week']), low['M'], yw(low['week']), s['hist'][12]['M']))
print('  nymphs: before %.1f, max in year %.1f' % (s['hist'][12]['Dn'], max(r['Dn'] for r in s['hist'][13:65])))

print('== choke and comeback')
s = new_pond(); run(s, 260, {0: lambda s: s.update(decomp_on=False), 78: lambda s: (s.update(decomp_on=True), add(s, 'D', 5))})
print('  muck share max %.0f%% at %s' % (max(100*r['Det']/total(s) for r in s['hist'][:78]), yw(max(s['hist'][:78], key=lambda r: r['Det'])['week'])))
w = first(s, lambda r: r['week'] > 78 and r['Af'] + r['As'] > 100)
print('  decomposers back y2w26: algae over 100 at', yw(w), 'weeks after', w - 78 if w else None)

print('== dragonflies removed y1w0: snail peak vs ghost')
g = new_pond(); run(g, 520); s = new_pond(Dn=0.0); run(s, 520)
print('  snails max per year  with:', [round(rng(g, 'S', y)[1]/0.5) for y in range(10)])
print('  snails max per year   no :', [round(rng(s, 'S', y)[1]/0.5) for y in range(10)])
print('== heron count vs catch and flying off')
for n in (1, 2, 3):
    s = new_pond(herons=n); run(s, 520)
    print('  %d herons: first flew off %s, catch y1 %.1f' % (n, yw(s['log'][0][0]) if s['log'] else None, yearsum(s, 0, 'eat_heron')))

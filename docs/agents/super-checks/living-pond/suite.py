from pond import *
import sys

def yw(w): return None if w is None else f"y{w//52+1}w{w%52}"
def first(s, c):
    for r in s['hist']:
        if c(r): return r['week']
def rng(s, k, y0, y1=None):
    h = s['hist'][y0*52:(y1 or y0+1)*52]; return (round(min(r[k] for r in h), 1), round(max(r[k] for r in h), 1))
def present(s):
    d = dict(algae=s['Af']+s['As'] > 0, snails=s['S'] > 0, minnows=Mt(s) > 0, nymphs=s['Dn'] > 0,
             turtle=s['turtles'] > 0, heron=s['herons'] > 0, decomp=s['D'] > 0)
    return [k for k, v in d.items() if not v]
def line(s, ws, keys=('N', 'Af', 'As', 'S', 'M', 'Dn', 'Det', 'O')):
    for w in ws:
        r = s['hist'][w]
        print('  ', yw(w), ' '.join(f"{k} {r[k]:.1f}" for k in keys), 'H', r['heron'], 'Tu', r['turtles'], 'col %.2f' % r['color'])
def summer_feed(amt, years=range(10), weeks=range(10, 34)):
    return {y*52+w: (lambda s, a=amt: add(s, 'F', a)) for y in years for w in weeks}

which = sys.argv[1:] or ['all']
if __name__ != '__main__': which = ['none']
def want(x): return 'all' in which or x in which

if want('A'):
    print('== A default'); s = new_pond(); run(s, 520); print(' gone:', present(s), 'log', s['log'])
    for y in (0, 1, 4, 9): print('  y%d' % (y+1), {k: rng(s, k, y) for k in ('Af', 'As', 'S', 'M', 'Dn', 'D', 'O')})
    print('  cutouts y10: snails %s minnows %s nymphs %s' % (tuple(v/0.5 for v in rng(s, 'S', 9)), tuple(v/2 for v in rng(s, 'M', 9)), tuple(v/0.5 for v in rng(s, 'Dn', 9))))
    print('  cutouts all years max: snails %.0f minnows %.0f nymphs %.0f algae clumps %.0f' % (max(r['S'] for r in s['hist'])/0.5, max(r['M'] for r in s['hist'])/2, max(r['Dn'] for r in s['hist'])/0.5, max(r['As'] for r in s['hist'])/5))
    h = s['hist'][468:520]
    print('  peak weeks y10: Af', max(h, key=lambda r: r['Af'])['week'] % 52, 'As', max(h, key=lambda r: r['As'])['week'] % 52, 'S', max(h, key=lambda r: r['S'])['week'] % 52, 'M', max(h, key=lambda r: r['M'])['week'] % 52, 'Dn', max(h, key=lambda r: r['Dn'])['week'] % 52)
    print('  color y1 end %.2f y3 %.2f y5 end %.2f y10 end %.2f' % (s['hist'][51]['color'], s['hist'][155]['color'], s['hist'][259]['color'], s['hist'][519]['color']))
    a = lambda k: sum(r['acc'][k] for r in h)
    an = a('G')-a('aresp'); gn = a('prod_snail')+a('prod_minnow')-a('maint_snail')-a('maint_minnow')
    print('  y10 energy: sun %.0f caught %.0f (%.2f%%); algae kept %.0f; plant-eaters kept %.0f (%.1f%% of algae kept); meat-eaters ate %.0f (%.1f%% of plant-eaters kept)' % (a('sun'), 10*a('G'), 100*10*a('G')/a('sun'), 10*an, 10*gn, 100*gn/an, 10*(a('eat_dragon')+a('eat_turtle')+a('eat_heron')), 100*(a('eat_dragon')+a('eat_turtle')+a('eat_heron'))/gn))
    print('  y10 heat out %.0f vs caught %.0f' % (10*a('resp'), 10*a('G')))
    E = s['energy']; print('  ten-year energy: sun %.0f caught %.0f heat %.0f' % (E['sun'], E['caught'], E['heat']))
    print('  matter: total %.4f start %.4f' % (total(s), total(new_pond())))
    print('  ice weeks', [w for w in range(52) if ice(w)])
if want('B'):
    print('== B decomposers stopped week 0'); s = new_pond(decomp_on=False); run(s, 520)
    for k, c in (('Af', lambda r: r['Af'] == 0), ('As', lambda r: r['As'] == 0), ('S', lambda r: r['S'] == 0), ('M', lambda r: r['M'] == 0), ('Dn', lambda r: r['Dn'] == 0), ('turtle', lambda r: r['turtles'] == 0)):
        print('  %s gone at' % k, yw(first(s, c)))
    line(s, (0, 13, 26, 39, 51, 64, 78))
    print('  muck share of matter at y1w51: %.0f%%, y2w51 %.0f%%' % (100*s['hist'][51]['Det']/total(s), 100*s['hist'][103]['Det']/total(s)))
    print('  log', s['log'])
    print('== B2 stopped y2 spring, back y3 spring')
    s = new_pond(); run(s, 520, {52: lambda s: s.update(decomp_on=False), 104: lambda s: (s.update(decomp_on=True), add(s, 'D', 5))})
    line(s, (51, 64, 77, 103, 116, 129, 155, 181, 259)); print('  gone at end:', present(s), s['log'])
if want('C'):
    print('== C net all minnows y1w13 (spring)'); s = new_pond(); run(s, 520, {13: lambda s: remove_all(s, 'M')})
    line(s, (12, 20, 26, 39, 51, 64, 78, 90, 103)); print('  gone at end', present(s), 'log', s['log'][:6])
    b = new_pond(); run(b, 104)
    print('  default: As min y1w26-y2w26 %.1f, snail min y1-y2 %.1f, Af max %.0f' % (min(r['As'] for r in b['hist'][26:78]), min(r['S'] for r in b['hist'][26:104]), max(r['Af'] for r in b['hist'][13:104])))
    print('  netted : As min y1w26-y2w26 %.1f, snail min y1-y2 %.1f, Af max %.0f' % (min(r['As'] for r in s['hist'][26:78]), min(r['S'] for r in s['hist'][26:104]), max(r['Af'] for r in s['hist'][13:104])))
if want('D'):
    print('== D net all snails y1w13'); s = new_pond(); run(s, 520, {13: lambda s: remove_all(s, 'S')}); line(s, (12, 26, 39, 51, 78, 103, 259, 519)); print('  gone', present(s), s['log'][:4])
if want('E'):
    print('== E overfeeding: flakes every summer week (w10-33) of year 1 only, amount per week')
    for amt in (2, 5, 8, 10, 12, 15, 20, 30):
        s = new_pond(); run(s, 104, summer_feed(amt, years=[0]))
        wk = first(s, lambda r: r['O'] < 3); g = first(s, lambda r: r['M'] == 0)
        print('  %2d/wk: Af max %.0f, O min %.1f (below 3 at %s), minnows gone %s, M min %.1f, Dn min %.1f, S min %.1f, M y2w0 %.1f y2w10 %.1f, gone@y2 %s' % (amt, max(r['Af'] for r in s['hist']), min(r['O'] for r in s['hist']), yw(wk), yw(g), min(r['M'] for r in s['hist']), min(r['Dn'] for r in s['hist']), min(r['S'] for r in s['hist']), s['hist'][52]['M'], s['hist'][62]['M'], present(s)))
if want('F'):
    print('== F trait drift')
    for lab, kw in (('sand, heron', dict(bottom=1.0)), ('mud, heron', dict(bottom=6.0)), ('gravel 3.5, heron', dict(bottom=3.5)), ('sand, no heron', dict(bottom=1.0, herons=0)), ('sand, 2 herons', dict(bottom=1.0, herons=2))):
        s = new_pond(**kw); run(s, 520)
        print('  %-18s color y1 %.2f y3 %.2f y5 %.2f y10 %.2f; minnows y10 %s; log %s' % (lab, s['hist'][51]['color'], s['hist'][155]['color'], s['hist'][259]['color'], s['hist'][519]['color'], rng(s, 'M', 9), s['log'][:3]))
    s = new_pond(bottom=1.0); run(s, 520, {260: lambda s: s.update(bottom=6.0)})
    print('  sand 5 yrs then mud: y5 %.2f y6 %.2f y7 %.2f y8 %.2f y10 %.2f' % (s['hist'][259]['color'], s['hist'][311]['color'], s['hist'][363]['color'], s['hist'][415]['color'], s['hist'][519]['color']))
    print('  shade shares y5 (sand):', [round(x/sum(s['hist'][259]['Mbins'])*100) for x in s['hist'][259]['Mbins']])
if want('G'):
    print('== G green water hides minnows: drift with summer feeding each year (sand, heron)')
    for amt in (0, 2, 4, 6):
        s = new_pond(bottom=1.0); run(s, 520, summer_feed(amt))
        print('  feed %d/wk every summer: Af summer mean y5 %.0f, clarity mean %.2f, color y5 %.2f y10 %.2f, O min %.1f, gone %s' % (amt, sum(r['Af'] for r in s['hist'][208+13:208+39])/26, sum(r['acc']['clarity'] for r in s['hist'][208+13:208+39])/26, s['hist'][259]['color'], s['hist'][519]['color'], min(r['O'] for r in s['hist']), present(s)))
if want('H'):
    print('== H turtle removed y1w0'); s = new_pond(turtles=0); run(s, 520); print('  y10', {k: rng(s, k, 9) for k in ('S', 'M', 'Dn', 'As', 'Af')}, 'gone', present(s))
    b = new_pond(); run(b, 520); print('  default y10', {k: rng(b, k, 9) for k in ('S', 'M', 'Dn', 'As', 'Af')})
if want('I'):
    print('== I herons')
    for n in (0, 2, 3):
        s = new_pond(herons=n); run(s, 520); print('  %d herons: M y1 %s y10 %s heron weeks y10 %d log %s gone %s' % (n, rng(s, 'M', 0), rng(s, 'M', 9), sum(1 for r in s['hist'][468:] if r['heron']), s['log'][:4], present(s)))
if want('J'):
    print('== J turtles 2,3')
    for n in (2, 3):
        s = new_pond(turtles=n); run(s, 520); print('  %d turtles: log %s; y10 %s gone %s' % (n, s['log'][:4], {k: rng(s, k, 9) for k in ('S', 'M', 'Dn')}, present(s)))
if want('K'):
    print('== K boom: add 40 minnows (80 units) at y1w13'); s = new_pond(); run(s, 520, {13: lambda s: add(s, 'M', 80)}); line(s, (13, 20, 26, 39, 51, 64, 78, 103), ('Af', 'As', 'S', 'M', 'Dn', 'O')); print('  gone', present(s))
    print('== K2 add 100 snails (50 units) y1w13'); s = new_pond(); run(s, 520, {13: lambda s: add(s, 'S', 50)}); line(s, (13, 20, 26, 39, 51, 78), ('Af', 'As', 'S', 'M', 'Dn', 'O')); print('  gone', present(s))
if want('L'):
    print('== L no dragonflies'); s = new_pond(Dn=0.0); run(s, 520); print('  y10', {k: rng(s, k, 9) for k in ('S', 'M', 'As', 'Af')}, 'gone', present(s))

from suite import *
import math

def empty(**kw):
    s = new_pond(Af=0.0, As=0.0, S=0.0, Dn=0.0, turtles=0, herons=0, **kw)
    s['M'] = [0.0] * BINS
    return s

def stock(s, algae=0, snails=0, minnows=0, nymphs=0, turtles=0, herons=0):
    if algae: add(s, 'algae', 5 * algae)
    if snails: add(s, 'S', 0.5 * snails)
    if minnows: add(s, 'M', 2 * minnows)
    if nymphs: add(s, 'Dn', 0.5 * nymphs)
    for i in range(turtles): add(s, 'turtle')
    s['herons'] += herons

def report(lab, s, t0):
    bad = [v for v in (s['N'], s['Af'], s['As'], s['S'], s['Dn'], s['D'], s['Det'], s['O']) + tuple(s['M']) if not math.isfinite(v) or v < 0]
    print('%-34s gone %s; first losses %s; log %s; drift %.1e; bad %s; max cutouts S %.0f M %.0f Dn %.0f clumps %.0f' % (
        lab, present(s), [(k, yw(first(s, c))) for k, c in (('S', lambda r: r['S'] == 0), ('M', lambda r: r['M'] == 0), ('Dn', lambda r: r['Dn'] == 0), ('A', lambda r: r['Af'] + r['As'] == 0)) if first(s, c) is not None],
        s['log'][:3], ident(s) - t0, bad, max(r['S'] for r in s['hist']) / .5, max(r['M'] for r in s['hist']) / 2, max(r['Dn'] for r in s['hist']) / .5, max(r['As'] for r in s['hist']) / 5))

cases = [
    ('sensible build wk0', dict(algae=10, snails=20, minnows=10, nymphs=6, turtles=1, herons=1), 0),
    ('small build wk0', dict(algae=4, snails=6, minnows=3, nymphs=2, turtles=1, herons=1), 0),
    ('two of each wk0', dict(algae=2, snails=2, minnows=2, nymphs=2, turtles=1, herons=1), 0),
    ('everything max wk0', dict(algae=40, snails=60, minnows=60, nymphs=30, turtles=3, herons=2), 0),
    ('predators first', dict(algae=5, snails=5, minnows=5, nymphs=10, turtles=3, herons=2), 0),
    ('sensible build in winter wk45', dict(algae=10, snails=20, minnows=10, nymphs=6, turtles=1, herons=1), 45),
    ('algae only', dict(algae=10), 0),
    ('animals, no algae', dict(snails=20, minnows=10, nymphs=6, turtles=1, herons=1), 0),
    ('no predators', dict(algae=10, snails=20, minnows=10), 0),
]
if __name__ == "__main__":
    for lab, kw, wk in cases:
        s = empty(); t0 = ident(s)
        run(s, 520, {wk: lambda s, kw=kw: stock(s, **kw)})
        report(lab, s, t0)

    # worst-case inputs
    s = empty(); t0 = ident(s)
    ev = {w: [lambda s: add(s, 'F', 60)] for w in range(0, 520)}; ev[0].insert(0, lambda s: stock(s, algae=40, snails=120, minnows=120, nymphs=60, turtles=3, herons=2)); run(s, 520, ev)
    report('max stock + 60 food every week', s, t0)
    print('   max Af %.0f max total matter %.0f' % (max(r['Af'] for r in s['hist']), total(s)))
    s = new_pond(); t0 = ident(s)
    run(s, 520, {w: (lambda s: add(s, 'S', 0.5 * 20)) for w in range(0, 520, 4)})
    report('default + 20 snails every 4 weeks', s, t0)

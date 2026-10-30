from suite import *
from build import stock
base = {0: lambda s: s.update(decomp_on=False), 78: lambda s: (s.update(decomp_on=True), add(s, 'D', 5))}
for lab, ev in (('all at y3w30', {108: dict(snails=20, minnows=10, nymphs=6, turtles=1)}),
                ('grazers y3w30, hunters y4w0', {108: dict(snails=20, minnows=10), 156: dict(nymphs=6, turtles=1)}),
                ('grazers y3w30, hunters y4w13', {108: dict(snails=20, minnows=10), 169: dict(nymphs=10, turtles=1)}),
                ('all at y4w0', {156: dict(snails=20, minnows=10, nymphs=6, turtles=1)})):
    e = dict(base); e.update({w: (lambda s, k=k: stock(s, **k)) for w, k in ev.items()})
    t = new_pond(); run(t, 52*8, e)
    print('%-30s gone y8 %s log %s' % (lab, present(t), [(yw(w), m) for w, m in t['log'] if w > 100][:4]))

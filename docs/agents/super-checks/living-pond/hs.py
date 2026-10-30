import sys, copy, pond
from pond import *
from build import empty, stock
from suite import present, rng, first, yw
for H,cm in ((35,0.7),(25,0.7),(25,0.6),(20,0.6)):
    P['sp']['dragon'].update(H=H,cmax=cm)
    s=new_pond(); run(s,520)
    out=['H%d c%.1f default gone %s Dn y10 %s S y10 %s M y10 %s col %.2f'%(H,cm,present(s),rng(s,'Dn',9),rng(s,'S',9),rng(s,'M',9),s['hist'][-1]['color'])]
    for lab,kw,wk in (('sensible',dict(algae=10, snails=20, minnows=10, nymphs=6, turtles=1, herons=1),0),('small',dict(algae=4, snails=6, minnows=3, nymphs=2, turtles=1, herons=1),0),('two each',dict(algae=2, snails=2, minnows=2, nymphs=2, turtles=1, herons=1),0)):
        s=empty(); run(s,520,{wk:lambda s,kw=kw:stock(s,**kw)}); out.append('%s gone %s'%(lab,present(s)))
    s=empty(); run(s,520,{0:lambda s:stock(s,algae=4,snails=6,minnows=3),52:lambda s:stock(s,nymphs=2,turtles=1,herons=1)}); out.append('late hunters gone %s'%present(s))
    s=new_pond(); run(s,104,{13:lambda s:remove_all(s,'M')}); out.append('netM snails gone %s'%yw(first(s,lambda r:r['S']==0)))
    print(' | '.join(out))

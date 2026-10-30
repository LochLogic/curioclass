from pond import *
from build import empty, stock
from suite import present, rng, first, yw
for wk in (52,52+13,52+26,52+32):
  for n in (6,10,20):
    s=empty(); run(s,520,{0:lambda s:stock(s,algae=4,snails=6,minnows=3,turtles=1,herons=1),wk:lambda s,n=n:stock(s,nymphs=n)})
    r=s['hist'][wk]
    print('nymphs',n,'added at',yw(wk),'prey then S %.1f M %.1f'%(r['S'],r['M']),'gone',present(s),'Dn y10',rng(s,'Dn',9))

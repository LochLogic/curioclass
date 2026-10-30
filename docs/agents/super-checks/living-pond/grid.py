from pond import *
from build import empty, stock
from suite import present
import itertools, collections
ok=0; tot=0; fails=collections.Counter(); rows=[]
for a,sn,mi,ny,tu in itertools.product((5,10,20),(10,20,40),(5,10,20),(4,10),(0,1)):
    s=empty(); run(s,520,{0:lambda s:stock(s,algae=a,snails=sn,minnows=mi,nymphs=ny,turtles=tu,herons=1)})
    g=present(s)
    if tu==0: g=[x for x in g if x!='turtle']
    tot+=1; ok+= (g==[])
    for x in g: fails[x]+=1
    rows.append(((a,sn,mi,ny,tu),g))
print('success',ok,'of',tot,fails)
for r in rows:
    if r[0][4]==1: print(r)

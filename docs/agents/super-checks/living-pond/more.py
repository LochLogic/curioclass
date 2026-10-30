from pond import *
from build import empty, stock
from suite import present, rng, first, yw
for n in (2,6,10):
    s=empty(); run(s,520,{0:lambda s:stock(s,algae=4,snails=6,minnows=3),52:lambda s,n=n:stock(s,nymphs=n,turtles=1,herons=1)}); print('late hunters nymphs',n,'gone',present(s),'Dn y10',rng(s,'Dn',9))
for n in (6,10,20):
    s=empty(); run(s,104,{0:lambda s,n=n:stock(s,algae=4,snails=6,minnows=3,nymphs=n,turtles=1,herons=1)}); print('early hunters nymphs',n,'nymphs gone',yw(first(s,lambda r:r['week']>0 and r['Dn']==0)))
s=new_pond(); run(s,780,{520:lambda s:remove_all(s,'heron')})
print('sand 10y then no heron 5y: y10 %.2f y15 %.2f delta %.2f'%(s['hist'][519]['color'],s['hist'][779]['color'],s['hist'][779]['color']-s['hist'][519]['color']))
s=new_pond(bottom=6.0); run(s,780,{520:lambda s:remove_all(s,'heron')})
print('mud 10y then no heron 5y: y10 %.2f y15 %.2f delta %.2f'%(s['hist'][519]['color'],s['hist'][779]['color'],s['hist'][779]['color']-s['hist'][519]['color']))
s=new_pond(herons=0); run(s,260); print('no heron from start 5y: %.3f'%s['hist'][259]['color'])
# reversal: sand 5y then mud: years to move 1 shade back
s=new_pond(); run(s,780,{260:lambda s:s.update(bottom=6.0)})
c5=s['hist'][259]['color']; w=first(s,lambda r:r['week']>260 and r['color']>=c5+1.0); print('reverse 1 shade after', (w-260)/52 if w else None,'years')
# camouflage 1 shade: years
for b in (1.0,6.0):
    s=new_pond(bottom=b); run(s,520); w=first(s,lambda r:abs(r['color']-3.5)>=1.0); print('bottom',b,'1 shade at',yw(w))
# full house: max simultaneous
s=new_pond(); run(s,520)
best=max(s['hist'],key=lambda r:min(r['S']/0.5/40,r['M']/2/40,r['Dn']/0.5/10))
print('best simultaneous S %.0f M %.0f Dn %.0f at %s'%(best['S']/0.5,best['M']/2,best['Dn']/0.5,yw(best['week'])))

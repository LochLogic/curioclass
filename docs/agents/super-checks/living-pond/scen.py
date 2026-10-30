from pond import *
from checks import stats, first, yw, present
import math
def sunsurf(w): return 0.6 + 0.4*math.cos(2*math.pi*((w%52)-16)/52)
print("\n== energy calibration")
s=new_pond(); run(s,520)
h=s['hist'][468:520]; G=sum(r['acc']['G'] for r in h); sun=70000*sum(sunsurf(r['week']) for r in h)
print('year10 sun at surface %.0f, algae caught %.0f = %.2f%%'%(sun,10*G,100*10*G/sun))

print("\n== B decomposers stopped at week 0")
s=new_pond(decomp_on=False); run(s,520)
print('A gone', yw(first(s,lambda r:r['A']==0)), 'S gone', yw(first(s,lambda r:r['S']==0)), 'M gone', yw(first(s,lambda r:r['M']==0)), 'Dn gone', yw(first(s,lambda r:r['Dn']==0)))
for wk in (0,13,26,39,52,78,104,156,260,519):
    r=s['hist'][wk]; print(' ',yw(wk),'N %.0f A %.0f S %.1f M %.1f Dn %.1f Det %.0f turtles %d'%(r['N'],r['A'],r['S'],r['M'],r['Dn'],r['Det'],r['turtles']))
print(' log', s['log'][:8])
print("\n== B2 decomposers stopped spring y1, back on spring y3")
def off(s): s['decomp_on']=False
def on(s): s['decomp_on']=True; s['D']+=5; s['ledger']['added']+=5
s=new_pond(); run(s,520,{52:off,156:on})
for wk in (51,64,77,103,129,155,168,181,207,259,519):
    r=s['hist'][wk]; print(' ',yw(wk),'N %.0f A %.0f S %.1f M %.1f Dn %.1f Det %.0f D %.1f'%(r['N'],r['A'],r['S'],r['M'],r['Dn'],r['Det'],r['D']))
print(' present end', present(s))

from pond import *
import copy
def stats(s, y0=0, y1=None):
    h=s['hist'][y0*52:(y1*52 if y1 else None)]
    f=lambda k:(min(r[k] for r in h),max(r[k] for r in h))
    return {k:tuple(round(v,1) for v in f(k)) for k in ('A','S','M','Dn','D','Det','N','O')}
def first(s,cond):
    for r in s['hist']:
        if cond(r): return r['week']
    return None
def yw(w): return None if w is None else f"y{w//52+1} w{w%52}"
def present(s):
    return dict(algae=s['A']>0,snails=s['S']>0,minnows=Mt(s)>0,dragons=s['Dn']>0,turtle=s['turtles']>0,heron=s['herons']>0,decomp=s['D']>0)

print("== A default ten winters")
s=new_pond(); t0=ident(s); run(s,520)
print(present(s), 'drift', ident(s)-t0)
print(stats(s)); print('last year', stats(s,9,10)); print('log', s['log'])
print('cutouts last year: snails %.0f-%.0f minnows %.0f-%.0f nymphs %.0f-%.0f algae clumps %.0f-%.0f'%(
   stats(s,9,10)['S']+tuple()[:0] and (stats(s,9,10)['S'][0],stats(s,9,10)['S'][1],stats(s,9,10)['M'][0]/2,stats(s,9,10)['M'][1]/2,stats(s,9,10)['Dn'][0],stats(s,9,10)['Dn'][1],stats(s,9,10)['A'][0]/5,stats(s,9,10)['A'][1]/5)))
print('color y0 %.2f y5 %.2f y10 %.2f'%(3.5, s['hist'][259]['color'], s['hist'][519]['color']))
E=s['energy']; print('energy sun %.0f captured %.0f (%.2f%%) heat %.0f'%(E['sun'],E['captured'],100*E['captured']/E['sun'],E['heat']))
# trophic production year 10
acc=lambda k: sum(r['acc'][k] for r in s['hist'][468:520])
G=acc('G'); ps=acc('prod_snail'); pm=acc('prod_minnow'); pd=acc('prod_dragon'); et=acc('eat_turtle'); eh=acc('eat_heron')
print('year10 algae made %.0f, grazers built (snail %.0f + minnow %.0f) = %.1f%%, nymphs built %.1f, turtle ate %.1f heron ate %.1f'%(G,ps,pm,100*(ps+pm)/G,pd,et,eh))
print('  grazers ate', acc('eat_snail')+acc('eat_minnow'), 'predators ate', acc('eat_dragon')+et+eh)
h=s['hist'][468:520]
a=lambda k: sum(r['acc'].get(k,0) for r in h)
algae_net=a('G')-a('aresp')
graz_net=a('prod_snail')+a('prod_minnow')-a('maint_snail')-a('maint_minnow')
pred_in=a('eat_dragon')+a('eat_turtle')+a('eat_heron')
pred_net=a('prod_dragon')-a('maint_dragon')
print('algae net %.0f grazers net %.0f (%.1f%%) predators ate %.0f (%.1f%% of grazer net) nymph net %.1f'%(algae_net,graz_net,100*graz_net/algae_net,pred_in,100*pred_in/graz_net,pred_net))

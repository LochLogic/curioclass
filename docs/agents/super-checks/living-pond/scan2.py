import pond, copy, itertools, sys
from pond import *
BASE=copy.deepcopy(P)
def setp(over):
    P.clear(); P.update(copy.deepcopy(BASE))
    for k,v in over.items():
        if isinstance(v,dict) and k in P['sp']: P['sp'][k].update(v)
        else: P[k]=v
def summ(s,y):
    h=s['hist'][y*52:(y+1)*52]
    return 'S %.0f-%.0f M %.0f-%.0f Dn %.1f-%.1f A %.0f'%(min(r['S'] for r in h),max(r['S'] for r in h),min(r['M'] for r in h),max(r['M'] for r in h),min(r['Dn'] for r in h),max(r['Dn'] for r in h),max(r['A'] for r in h))
for detw, mc in itertools.product([0.0,0.05],[(0.8,150),(1.0,120),(1.2,100)]):
    pond.MDET=detw
    setp({'minnow':{'cmax':mc[0],'H':mc[1]}})
    s=new_pond(); run(s,520); a=summ(s,9); col=s['hist'][-1]['color']
    s2=new_pond(decomp_on=False); run(s2,520); b=summ(s2,9)
    s3=new_pond(decomp_on=False); run(s3,104); c=summ(s3,1)
    print(detw,mc,'| default y10',a,'col %.2f'%col,'| nodecomp y2',c,'| y10',b)

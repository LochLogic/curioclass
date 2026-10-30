import pond, copy, itertools, sys, json
from pond import *
BASE=copy.deepcopy(P)
def setp(over):
    P.clear(); P.update(copy.deepcopy(BASE))
    for k,v in over.items():
        if isinstance(v,dict) and k in P['sp']: P['sp'][k].update(v)
        else: P[k]=v
def rng(s,k,y): h=s['hist'][y*52:(y+1)*52]; return (min(r[k] for r in h),max(r[k] for r in h))
def rep(over, label=''):
    setp(over); s=new_pond(); run(s,520)
    hw=sum(1 for r in s['hist'][468:] if r['heron'])
    S=rng(s,'S',9);M=rng(s,'M',9);D=rng(s,'Dn',9);A=rng(s,'Af',9);As=rng(s,'As',9);O=min(r['O'] for r in s['hist'])
    print(label, 'S %.0f-%.0f M %.0f-%.0f Dn %.1f-%.1f Af %.0f-%.0f As %.0f-%.0f Omin %.1f heronwk %d col %.2f tu %d'%(S+M+D+A+As+(O,hw,s['hist'][-1]['color'],s['turtles'])))
    return s
if __name__=='__main__':
    for dc,hh in itertools.product([(0.6,50),(0.7,35),(0.8,30)],[25,15,10]):
        rep({'dragon':{'cmax':dc[0],'H':dc[1]},'heron_H':hh}, str((dc,hh)))

import pond, copy, itertools, json, sys
from pond import *
BASE=copy.deepcopy(P)
def setp(over):
    P.clear(); P.update(copy.deepcopy(BASE))
    for k,v in over.items():
        if isinstance(v,dict): P['sp'][k].update(v)
        else: P[k]=v
def yearly(s):
    out=[]
    for y in range(len(s['hist'])//52):
        rows=s['hist'][y*52:(y+1)*52]
        out.append(dict(Smin=min(r['S'] for r in rows),Smax=max(r['S'] for r in rows),
          Mmin=min(r['M'] for r in rows),Mmax=max(r['M'] for r in rows),
          Dmin=min(r['Dn'] for r in rows),Dmax=max(r['Dn'] for r in rows),
          Amax=max(r['A'] for r in rows),Omin=min(r['O'] for r in rows),col=rows[-1]['color']))
    return out
base={"po":0.05,"co":0.05,"decomp":{"eff":0.2,"mort":0.1}}
for sc,dc in itertools.product([(0.9,150),(1.0,120),(1.1,100)],[(0.7,40),(0.6,50),(0.7,60)]):
    over=copy.deepcopy(base); over['snail']={'cmax':sc[0],'H':sc[1]}; over['dragon']={'cmax':dc[0],'H':dc[1]}
    setp(over); s=new_pond(); run(s,520); y=yearly(s)
    print(sc,dc,'end S %.1f M %.1f Dn %.1f tu %d'%(s['S'],Mt(s),s['Dn'],s['turtles']),
      'Srange y9 %.0f-%.0f Mrange %.0f-%.0f Dn %.1f-%.1f Omin %.1f col %.2f'%(y[9]['Smin'],y[9]['Smax'],y[9]['Mmin'],y[9]['Mmax'],y[9]['Dmin'],y[9]['Dmax'],min(v['Omin'] for v in y),y[9]['col']))

import json,math,numpy as np
D=json.load(open('pc3d.json'))
def ang(at,c,a,b):
    p=np.array(at[c][1]);u=np.array(at[a][1])-p;v=np.array(at[b][1])-p
    return math.degrees(math.acos(np.dot(u,v)/np.linalg.norm(u)/np.linalg.norm(v)))
for n in ['water','hydrogen sulfide','ammonia','methane','carbon dioxide','ethylene','acetylene','hydrogen peroxide','urea','caffeine','benzene','formic acid']:
    d=D[n]; at=d['atoms']; nb={i:[] for i in range(len(at))}
    for a,b,o in d['bonds']: nb[a].append(b); nb[b].append(a)
    out=[]
    for c in nb:
        if at[c][0]!='H' and len(nb[c])>1:
            angs=[ang(at,c,nb[c][i],nb[c][j]) for i in range(len(nb[c])) for j in range(i+1,len(nb[c]))]
            out.append(f"{at[c][0]}{c}:{min(angs):.1f}-{max(angs):.1f} sum{sum(angs):.0f}")
    print(n,'; '.join(out))

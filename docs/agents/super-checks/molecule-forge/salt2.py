import itertools, collections, numpy as np, math
O6=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def run(budget=600, rule='max'):
    filled={(0,0,0),(1,0,0)}; steps=[2]
    while True:
        front=collections.Counter()
        for p in filled:
            for o in O6:
                q=(p[0]+o[0],p[1]+o[1],p[2]+o[2])
                if q not in filled: front[q]+=0
        for q in front: front[q]=sum((q[0]+o[0],q[1]+o[1],q[2]+o[2]) in filled for o in O6)
        m=max(front.values())
        add=[q for q,c in front.items() if c==m] if rule=='max' else [q for q,c in front.items() if c>=min(m,3)]
        if len(filled)+len(add)>budget: break
        filled|=set(add); steps.append(len(filled))
    P=np.array(sorted(filled)); ext=P.max(0)-P.min(0)+1
    return len(filled), steps, ext, len(filled)/np.prod(ext)
n,steps,ext,fill=run()
print("salt greedy most-neighbors growth: ions",n,"steps",len(steps),"box",ext,"box filled",round(fill,3))
print("first steps",steps[:12])
# charges: parity

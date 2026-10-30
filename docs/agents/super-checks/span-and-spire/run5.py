from designs import *
def envelope(tr,deck,trucks):
    W=np.zeros(len(tr.M))
    for t in trucks:
        r=tr.crossing(deck,t,step=0.5)
        if r is None: return None
        W=np.maximum(W,r[0])
    return W
def autosize(tr,deck,trucks,limit,ladder=('T','TH','S','SH')):
    for it in range(40):
        W=envelope(tr,deck,trucks)
        if W is None: return None
        bad=[i for i in range(len(tr.M)) if W[i]>limit and not MT[tr.M[i][2]]['cable']]
        if not bad: return W
        for i in bad:
            m=tr.M[i]; k=ladder.index(m[2])
            if k+1<len(ladder): tr.M[i]=(m[0],m[1],ladder[k+1])
            else: return None
    return None
for panels in (6,8):
  for h in (2,3,4,5):
    tr,deck=build(panels=panels,h=h); tr.abut={0,panels}
    W=autosize(tr,deck,['Grain truck','Semi'],0.667)
    if W is None: print(panels,h,'none'); continue
    cnt={k:sum(1 for m in tr.M if m[2]==k) for k in MT}
    print(f'panels {panels} h {h}: cost ${tr.cost():,.0f} max {W.max()*100:.1f}% members {len(tr.M)} {cnt}')

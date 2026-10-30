from truss import *
def build(panels=6,h=4.0,top='T',bot='T',vert='T',diag='T',kind='pratt',L=24):
    p=L/panels; J=[(i*p,0) for i in range(panels+1)]
    top_idx={}
    for i in range(1,panels):
        top_idx[i]=len(J); J.append((i*p,h))
    M=[]
    for i in range(panels): M.append((i,i+1,bot))
    for i in range(1,panels-1): M.append((top_idx[i],top_idx[i+1],top))
    # end posts
    M.append((0,top_idx[1],top)); M.append((panels,top_idx[panels-1],top))
    for i in range(1,panels): M.append((i,top_idx[i],vert))
    mid=panels/2
    for i in range(1,panels-1):
        # diagonal in panel between i and i+1 (top i..i+1)
        if kind=='pratt':  # diagonals slope down toward center -> tension
            if i+1<=mid: M.append((top_idx[i],i+1,diag))
            else: M.append((i,top_idx[i+1],diag))
        else: # howe -> compression diagonals
            if i+1<=mid: M.append((i,top_idx[i+1],diag))
            else: M.append((top_idx[i],i+1,diag))
    deck=list(range(panels+1))
    return Truss(J,M,{0:'pin',panels:'roller'}),deck
def report(tr,deck,name,trucks=TRUCKS):
    tr.abut={0,deck[-1]} if not hasattr(tr,'abut') else tr.abut
    print(f'== {name}: {len(tr.J)} joints {len(tr.M)} members cost ${tr.cost():,.0f}')
    for t in trucks:
        r=tr.crossing(deck,t)
        if r is None: print('  ',t,'MECHANISM'); continue
        w,wp,d=r; i=int(np.argmax(w)); m=tr.M[i]
        L,_,_=tr.geom(m); ten,comp=tr.cap(m)
        f0='buckle' if comp<ten else 'crush'
        print(f'   {t:12s} {tw(t):5.1f} t max use {w[i]*100:6.1f}% member {i} {MT[m[2]]["name"]} {tr.J[m[0]]}-{tr.J[m[1]]} L={L:.2f} at front={wp[i]} defl {d*1000:.0f} mm {"PASS" if w[i]<=1 else "FAIL"}')

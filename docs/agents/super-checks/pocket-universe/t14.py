from pu import *
m=300; L=200; t0=math.sqrt(L**3/(G*m)); V=L/t0; P=6.32591398*t0
out('figure-eight scale: period s',round(P,3),'speed unit',round(V,2))
x1=np.array([0.97000436,-0.24308753]); v3=np.array([-0.93240737,-0.86473146])
def make(nudge=(0,0),idx=2):
    b=[dict(kind='dwarf',x=x1[0]*L,y=x1[1]*L,vx=-v3[0]/2*V,vy=-v3[1]/2*V),
       dict(kind='dwarf',x=-x1[0]*L,y=-x1[1]*L,vx=-v3[0]/2*V,vy=-v3[1]/2*V),
       dict(kind='dwarf',x=0,y=0,vx=v3[0]*V,vy=v3[1]*V)]
    b[idx]['vx']+=nudge[0]; b[idx]['vy']+=nudge[1]
    return Sim(b)
def test(nudge,rounds=20):
    s=make(nudge); dmin=[1e9]; rmax=[0]; broke=[None]
    def cb(q):
        if not q.alive.all():
            if broke[0] is None: broke[0]=('crash',round(q.t/P,1))
            return
        for i in range(3):
            for j in range(i+1,3): dmin[0]=min(dmin[0],math.hypot(*(q.x[i]-q.x[j])))
        com=(q.x*q.m[:,None]).sum(0)/q.m.sum()
        r=max(math.hypot(*(q.x[i]-com)) for i in range(3)); rmax[0]=max(rmax[0],r)
        if r>3*L and broke[0] is None: broke[0]=('flung out',round(q.t/P,1))
    s.run(rounds*P,cb,every=4)
    # return-to-start error after 1 period isn't tracked; report
    return round(dmin[0],1), round(rmax[0]), broke[0]
out('exact: min sep, max r from center, broke?',test((0,0)))
s=make(); s.run(P); out('exact: return error after 1 period px',np.round(np.hypot(*(s.x[2]-0).T),2) if False else round(float(math.hypot(*s.x[2])),2))
spd=math.hypot(*v3)*V
for pct in [1,2,5,10,20]:
    out('nudge middle dancer +%d%% speed (%.1f px/s)'%(pct,spd*pct/100), test(tuple(v3*V*pct/100)))
for pct in [5,10,20]:
    perp=np.array([-v3[1],v3[0]])/np.hypot(*v3)*spd*pct/100
    out('sideways nudge %d%%'%pct, test(tuple(perp)))

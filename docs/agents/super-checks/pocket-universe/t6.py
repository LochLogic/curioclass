from pu import *
m=500
def run(d,extra,T):
    vb=math.sqrt(G*m/(2*d))
    b=[dict(kind='star',m=m,r=18,x=-d/2,y=0,vx=0,vy=-vb),dict(kind='star',m=m,r=18,x=d/2,y=0,vx=0,vy=vb)]+extra
    s=Sim(b); acc=[0,None,1e9]
    def cb(q):
        if not q.alive[2]: return
        c=(q.x[0]*q.m[0]+q.x[1]*q.m[1])/(q.m[0]+q.m[1]) if q.alive[0] and q.alive[1] else q.x[0]
        dd=q.x[2]-c; a=math.atan2(dd[1],dd[0]); acc[2]=min(acc[2],math.hypot(*dd))
        if acc[1] is not None: acc[0]+=(a-acc[1]+math.pi)%(2*math.pi)-math.pi
        acc[1]=a
    s.run(T,cb,every=4)
    far=math.hypot(*s.x[2]) if s.alive[2] else None
    return round(acc[0]/2/math.pi,2), round(acc[2]), s.merges, None if far is None else round(far)
d=100
out('sep 100 binary speed',round(math.sqrt(G*m/(2*d)),1),'period',round(2*math.pi*(d/2)/math.sqrt(G*m/(2*d)),2))
for R in [150,200,230,260,300,350]:
    v=circ(1010,R); out('P-type sep100 R',R,'ratio',R/d, run(d,[dict(kind='planet',x=0,y=R,vx=-v,vy=0)],120))
# S-type: wide binary sep 400, planet around star B at r
d=400; vb=math.sqrt(G*m/(2*d))
for r in [50,80,120,160]:
    v=circ(510,r)
    s=Sim([dict(kind='star',m=m,r=18,x=-d/2,y=0,vx=0,vy=-vb),dict(kind='star',m=m,r=18,x=d/2,y=0,vx=0,vy=vb),dict(kind='planet',x=d/2+r,y=0,vx=0,vy=vb+v)])
    L=Laps(2,1); bound=[True]
    def cb(q):
        L(q)
        if q.alive[2] and q.alive[1] and twobody_E(q,2,1)>0: bound[0]=False
    s.run(60,cb,every=4); out('S-type sep400 r',r,'ratio',r/d,'laps',round(L.laps,1),'stays bound',bound[0],s.merges)

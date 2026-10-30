from pu import *
import sys
random.seed(int(sys.argv[1]))
def setup():
    b=[dict(kind='star',x=0,y=0,vx=0,vy=0)]
    for R,th in [(180,0.3),(300,2.2),(450,4.0)]:
        v=circ(1010,R); b.append(dict(kind='planet',x=R*math.cos(th),y=R*math.sin(th),vx=-v*math.sin(th),vy=v*math.cos(th)))
    return b
hits=0;N=int(sys.argv[2]);ex=[];visits2=0
for k in range(N):
    r=random.uniform(60,500); th=random.uniform(0,2*math.pi); sp=random.uniform(50,450); ph=random.uniform(0,2*math.pi)
    b=setup()+[dict(kind='comet',x=r*math.cos(th),y=r*math.sin(th),vx=sp*math.cos(ph),vy=sp*math.sin(ph))]
    s=Sim(b); seen=set()
    def cb(q):
        if not q.alive[4]: return
        for j in (1,2,3):
            if q.alive[j] and math.hypot(*(q.x[4]-q.x[j]))<60: seen.add(j)
    s.run(30,cb,every=4)
    ok = s.alive[4]
    if len(seen)>=2 and ok: visits2+=1
    if len(seen)==3 and ok:
        hits+=1; ex.append((round(r),round(math.degrees(th)),round(sp),round(math.degrees(ph))))
out('seed',sys.argv[1],'trials',N,'passed 2 planets',visits2,'grand tour (all 3, within 60 px, no crash, 30 s)',hits,ex[:3])

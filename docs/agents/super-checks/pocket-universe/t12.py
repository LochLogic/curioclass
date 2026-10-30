from pu import *
import sys
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 1)
NEED=int(sys.argv[3]); m=500; d=float(sys.argv[4]); vb=math.sqrt(G*m/(2*d))
def run(x,y,vx,vy,T=40):
    s=Sim([dict(kind='star',m=m,r=18,x=-d/2,y=0,vx=0,vy=-vb),dict(kind='star',m=m,r=18,x=d/2,y=0,vx=0,vy=vb),dict(kind='comet',x=x,y=y,vx=vx,vy=vy)])
    st={'near':None,'sweep':0,'prev':None,'loops':[],'eights':0,'t8':None}
    def cb(q):
        if not q.alive[2] or st['t8']: return
        da_=[math.hypot(*(q.x[2]-q.x[k])) for k in (0,1)]
        n=0 if da_[0]<da_[1] else 1
        if n!=st['near']:
            if st['near'] is not None and abs(st['sweep'])>=math.radians(270):
                st['loops'].append((st['near'],1 if st['sweep']>0 else -1))
            elif st['near'] is not None: st['loops'].append((st['near'],0))
            st['near']=n; st['sweep']=0; st['prev']=None
        dd=q.x[2]-q.x[n]; a=math.atan2(dd[1],dd[0])
        if st['prev'] is not None: st['sweep']+=(a-st['prev']+math.pi)%(2*math.pi)-math.pi
        st['prev']=a
        L=st['loops']
        if len(L)>=NEED:
            w=L[-NEED:]
            if all(z[1]!=0 for z in w) and all(w[i][0]!=w[i+1][0] and w[i][1]==-w[i+1][1] for i in range(NEED-1)):
                st['t8']=q.t
    s.run(T,cb,every=2)
    return st['t8'], st['loops'][:8], s.merges
found=[];N=int(sys.argv[2]) if len(sys.argv)>2 else 150
for k in range(N):
    x=random.uniform(-300,300); y=random.uniform(-250,250); sp=random.uniform(50,400); ph=random.uniform(0,2*math.pi)
    t8,L,mg=run(x,y,sp*math.cos(ph),sp*math.sin(ph))
    if t8: found.append((round(x),round(y),round(sp),round(math.degrees(ph)),round(t8,1)))
out('seed',sys.argv[1:],'trials',N,'two-eight found',len(found),found[:5])

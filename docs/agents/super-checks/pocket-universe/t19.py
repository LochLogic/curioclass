from pu import *
random.seed(5)
vg=circ(1100,300)
def puff(cx,cy,vx,vy,n=30,rad=10,spread=0.05):
    X=[];Vv=[]
    for i in range(n):
        rr=rad*math.sqrt(random.random()); t=random.uniform(0,2*math.pi)
        X.append([cx+rr*math.cos(t),cy+rr*math.sin(t)]); f=1+random.uniform(-spread,spread)
        Vv.append([vx*f,vy*f])
    return X,Vv
for d in [30,40,55]:
    vm=circ(100,d)
    s=Sim([dict(kind='star',x=0,y=0,vx=0,vy=-100*vg/1000),dict(kind='giant',x=300,y=0,vx=0,vy=vg)],dust=puff(300+d,0,0,vg+vm))
    P=2*math.pi*d/vm
    s.run(3*P)
    rel=s.dx-s.x[1]; relv=s.dv-s.v[1]
    E=0.5*(relv**2).sum(1)-G*100/np.hypot(*rel.T)
    bound=int(((E<0)&s.dalive).sum())
    ang=np.degrees(np.arctan2(rel[:,1],rel[:,0]))[s.dalive&(E<0)]
    # how spread around the ring: count 30-degree sectors occupied
    sec=len(set((ang//30).astype(int)))
    out('puff at %d px from giant: after 3 laps (%.1f s) bound %d/30, ring sectors filled %d/12, eaten %d'%(d,3*P,bound,sec,int((~s.dalive).sum())))
    s.run(7*P); rel=s.dx-s.x[1]; relv=s.dv-s.v[1]; E=0.5*(relv**2).sum(1)-G*100/np.hypot(*rel.T)
    ang=np.degrees(np.arctan2(rel[:,1],rel[:,0]))[s.dalive&(E<0)]
    out('   after 10 laps bound %d sectors %d'%(int(((E<0)&s.dalive).sum()),len(set((ang//30).astype(int)))))

from pu import *
random.seed(7)
vg=circ(1100,300)
hits=[];bound0=0
for trial in range(300):
    r=random.uniform(120,550); th=random.uniform(0,2*math.pi); sp=random.uniform(0,450); ph=random.uniform(0,2*math.pi)
    b=[dict(kind='star',x=0,y=0,vx=0,vy=-100*vg/1000),dict(kind='giant',x=300,y=0,vx=0,vy=vg),
       dict(kind='comet',x=r*math.cos(th),y=r*math.sin(th),vx=sp*math.cos(ph),vy=sp*math.sin(ph))]
    s=Sim(b)
    if twobody_E(s,2,0)>=0: continue
    bound0+=1; st={'close':1e9,'esc':None}
    def cb(q):
        if st['esc'] or not q.alive[2]: return
        st['close']=min(st['close'],math.hypot(*(q.x[2]-q.x[1])))
        if math.hypot(*(q.x[2]-q.x[0]))>1500 and twobody_E(q,2,0)>0: st['esc']=q.t
    s.run(40,cb,every=4)
    if st['esc']: hits.append((round(r),round(math.degrees(th)),round(sp),round(math.degrees(ph)),round(st['close']),round(st['esc'],1)))
out('bound flings',bound0,'later escaped to 1500px',len(hits))
for h in hits: out('  ',h)

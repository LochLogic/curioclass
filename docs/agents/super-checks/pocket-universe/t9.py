from pu import *
random.seed(7)
vg=circ(1100,300)
hits=0;tot=0;ex=None;crash=0;escaped_plain=0;bound0=0;gains=[]
for trial in range(300):
    r=random.uniform(120,550); th=random.uniform(0,2*math.pi); sp=random.uniform(0,450); ph=random.uniform(0,2*math.pi)
    b=[dict(kind='star',x=0,y=0,vx=0,vy=-100*vg/1000),dict(kind='giant',x=300,y=0,vx=0,vy=vg),
       dict(kind='comet',x=r*math.cos(th),y=r*math.sin(th),vx=sp*math.cos(ph),vy=sp*math.sin(ph))]
    s=Sim(b)
    if twobody_E(s,2,0)>=0: continue
    bound0+=1
    st={'close':1e9,'tclose':None,'done':False}
    def cb(q):
        if st['done'] or not q.alive[2]: return
        dg=math.hypot(*(q.x[2]-q.x[1]))
        if dg<st['close']: st['close']=dg; st['tclose']=q.t
        if st['close']<100 and twobody_E(q,2,0)>0 and q.t-st['tclose']<3:
            st['done']=True; st['t']=q.t
    s.run(30,cb,every=4)
    if s.merges: crash+=1
    if st['done']:
        hits+=1
        if ex is None: ex=(round(r),round(math.degrees(th)),round(sp),round(math.degrees(ph)),round(st['close']),round(st['t'],2))
out('random bound flings',bound0,'slingshot escapes',hits,'crashes',crash,'example (r,theta,speed,dir,closest,t)',ex)

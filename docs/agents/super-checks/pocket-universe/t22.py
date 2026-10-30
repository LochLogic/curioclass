from pu import *
gm=100;R=300;vg=circ(1100,R);d=40
for n in [0,2,4,6,8,10,14,20,30]:
    f=1.15*0.99**n; vm=circ(gm+0.3,d)*f
    s=Sim([dict(kind='star',x=0,y=0,vx=0,vy=-gm*vg/1000),dict(kind='giant',x=R,y=0,vx=0,vy=vg),dict(kind='moon',x=R+d,y=0,vx=0,vy=vg+vm)])
    L=Laps(2,1); t10=[None]
    def cb(q):
        if not q.alive[2]: return
        L(q)
        if t10[0] is None and L.laps>=10 and twobody_E(q,2,1)<0: t10[0]=round(q.t,1)
    s.run(40,cb,every=2)
    out('Slower x%d (speed %.3f of circular): crash %s, 10 laps at %s, laps in 40 s %.1f'%(n,f,s.merges[:1],t10[0],L.laps))

from pu import *
def moon(R,d,gm,f,T=60,retro=False):
    vg=circ(1000+gm,R); vm=circ(gm+0.1,d)*f*(-1 if retro else 1)
    s=Sim([dict(kind='star',x=0,y=0,vx=0,vy=0),dict(kind='giant',m=gm,x=R,y=0,vx=0,vy=vg),dict(kind='moon',x=R+d,y=0,vx=0,vy=vg+vm)])
    Lm=Laps(2,1); fate=['ok',None]
    def cb(q):
        Lm(q)
        if fate[0]=='ok' and q.alive[2] and twobody_E(q,2,1)>0: fate[0]='lost';fate[1]=round(q.t,1)
    s.run(T,cb,every=4)
    if s.merges: fate=['crash',s.merges[0][0]]
    return '%s%s %.1fL'%(fate[0],'' if fate[1] is None else '@'+str(fate[1]),Lm.laps)
for gm in [30]:
  for R in [300,400]:
    for d in [16,20,25,30,35]:
        out('gm',gm,'R',R,'d',d,'hill%.2f'%(d/(R*(gm/3000)**(1/3))),[moon(R,d,gm,f) for f in (0.85,1,1.15)])

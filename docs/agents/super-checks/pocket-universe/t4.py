from pu import *
def moon(R,d,gm,f,T=60,retro=False,kind='giant'):
    vg=circ(1000+gm,R); vm=circ(gm+0.3,d)*f*(-1 if retro else 1)
    s=Sim([dict(kind='star',x=0,y=0,vx=-gm*vg/1000,vy=0) if False else dict(kind='star',x=0,y=0,vx=0,vy=-gm*vg/1000),dict(kind=kind,m=gm,x=R,y=0,vx=0,vy=vg),dict(kind='moon',x=R+d,y=0,vx=0,vy=vg+vm)])
    Lm=Laps(2,1); Lg=Laps(1,0); fate=['ok',None]
    def cb(q):
        Lm(q); Lg(q)
        if fate[0]=='ok' and q.alive[2] and twobody_E(q,2,1)>0: fate[0]='lost';fate[1]=round(q.t,1)
    s.run(T,cb,every=4)
    if s.merges: fate=['crash',s.merges[0][0]]
    return '%s%s %.1f/%.1fL'%(fate[0],'' if fate[1] is None else '@'+str(fate[1]),Lm.laps,Lg.laps)
H=lambda R,m:R*(m/3000)**(1/3)
for R in [300]:
  out('hill giant',round(H(R,100),1),'planet',round(H(R,10),1))
  for d in [20,25,30,40,50,60]:
    out('R',R,'d',d,'hill%.2f'%(d/H(R,100)),[moon(R,d,100,f) for f in (0.85,1,1.15)])
  for d in [50,60,70]:
    out(' retro d',d,[moon(R,d,100,f,retro=True) for f in (0.85,1,1.15)])
  for d in [12,15,18]:
    out(' planet10 d',d,[moon(R,d,10,f,kind='planet') for f in (0.9,1,1.1)])

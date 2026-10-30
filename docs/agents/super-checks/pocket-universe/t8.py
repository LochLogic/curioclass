from pu import *
v=circ(1010,250)
def base(kind='star'):
    return Sim([dict(kind=kind,x=0,y=0,vx=0,vy=-10*v/1000),dict(kind='planet',x=250,y=0,vx=0,vy=v)])
a=base(); b=base('hole'); a.run(20); b.run(20)
out('star vs hole same mass after 20s, planet position diff px', round(float(np.hypot(*(a.x[1]-b.x[1]))),6))
# halve star mass at t=0
s=base(); s.m[0]=500; E=twobody_E(s,1,0); out('halve: E rel',round(E,2))
t=0
while math.hypot(*(s.x[1]-s.x[0]))<1500 and s.t<120: s.step()
out(' halve: reaches 1500 px at t',round(s.t,1))
s=base(); s.m[0]=500
s.run(120); out(' halve: dist after 120 s', round(math.hypot(*(s.x[1]-s.x[0]))), 'E',round(twobody_E(s,1,0),2))
# halve from circular at r=250 with star mass precisely 2x? planet orbit factor: vis viva
s=base(); s.m[0]=2000; rr=[]
s.run(10,lambda q: rr.append(math.hypot(*(q.x[1]-q.x[0]))))
out('double star: r range',round(min(rr),1),round(max(rr),1))
s=base(); s.m[0]=3000; rr=[]
s.run(10,lambda q: rr.append(math.hypot(*(q.x[1]-q.x[0]))))
out('x3 star: r range',round(min(rr),1),round(max(rr),1),s.merges)
# gravity off
s=base(); s.g=0; s.run(3); out('gravity off 3 s: planet at',np.round(s.x[1],2),'(straight line x=250, y=',round(v*3,2),')')
# gravity x2 at circular
s=base(); s.g=2; rr=[]; s.run(10,lambda q: rr.append(math.hypot(*(q.x[1]-q.x[0])))); out('gravity x2: r',round(min(rr),1),round(max(rr),1))
s=base(); s.g=0.5; s.run(60); out('gravity x0.5: E',round(twobody_E(s,1,0),3),'dist',round(math.hypot(*(s.x[1]-s.x[0]))))
# black hole 3000, plunging comet: energy error adaptive vs not
for peri in [8,12,20,40]:
    M=3000; r0=600; # find speed at r0 sideways giving periapsis peri
    mu=G*M; # h = r0*v, peri from energy: solve v such that peri: v^2 = 2mu(1/peri-1/r0)/( (r0/peri)^2 -1 )
    vv=math.sqrt(2*mu*(1/peri-1/r0)/((r0/peri)**2-1))
    res=[]
    for ad in (False,True):
        s=Sim([dict(kind='hole',m=M,x=0,y=0,vx=0,vy=0),dict(kind='comet',x=r0,y=0,vx=0,vy=vv)])
        E0=twobody_E(s,1,0)
        n=int(8/DT)
        for k in range(n): s.step(adaptive=ad)
        res.append((round((twobody_E(s,1,0)-E0)/abs(E0),5) if s.alive[1] else 'eaten', s.substeps_used))
    out('hole 3000 peri',peri,'speed at peri',round(math.sqrt(2*mu/peri)),'px/s, rel energy error (fixed, adaptive):',res)

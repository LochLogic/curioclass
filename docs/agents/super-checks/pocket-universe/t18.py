from pu import *
AU=100.0; KM_AU=149597870.7
P=[('Mercury',0.38709927,0.20563593,252.25032350,77.45779628,0.330,4879),
   ('Venus',0.72333566,0.00677672,181.97909950,131.60246718,4.87,12104),
   ('Earth',1.00000261,0.01671123,100.46457166,102.93768193,5.97,12756),
   ('Mars',1.52371034,0.09339410,-4.55343205,-23.94362959,0.642,6792),
   ('Jupiter',5.20288700,0.04838624,34.39644051,14.72847983,1898,142984),
   ('Saturn',9.53667594,0.05386179,49.95424423,92.59887831,568,120536),
   ('Uranus',19.18916464,0.04725744,313.23810451,170.95427630,86.8,51118),
   ('Neptune',30.06992276,0.00859048,-55.12002969,44.96476227,102,49528)]
MSUN=1988500.0
YR=2*math.pi*math.sqrt(AU**3/(G*1000))
out('1 year at x1 = %.4f s'%YR)
def kep(a,e,L,w,mu):
    M=math.radians(L-w); E=M
    for _ in range(50): E=E-(E-e*math.sin(E)-M)/(1-e*math.cos(E))
    x=a*(math.cos(E)-e); y=a*math.sqrt(1-e*e)*math.sin(E)
    n=math.sqrt(mu/a**3); r=a*(1-e*math.cos(E))
    vx=-a*n*math.sin(E)/(1-e*math.cos(E)); vy=a*n*math.sqrt(1-e*e)*math.cos(E)/(1-e*math.cos(E))
    c,s=math.cos(math.radians(w)),math.sin(math.radians(w))
    return x*c-y*s, x*s+y*c, vx*c-vy*s, vx*s+vy*c
bodies=[dict(kind='star',m=1000,r=695700/KM_AU*AU,x=0,y=0,vx=0,vy=0)]
for n,a,e,L,w,mkg,dkm in P:
    m=mkg/MSUN*1000
    x,y,vx,vy=kep(a*AU,e,L,w,G*(1000+m))
    bodies.append(dict(kind='planet',m=m,r=dkm/2/KM_AU*AU,x=x,y=y,vx=vx,vy=vy))
    out('%-8s mass %.6f  a %.1f px  period %.3f s at x1 (%.2f yr)  drawn radius true %.5f px'%(n,m,a*AU,YR*a**1.5,a**1.5,dkm/2/KM_AU*AU))
# fix sun momentum
pt=sum(b['m']*np.array([b['vx'],b['vy']]) for b in bodies[1:]); bodies[0]['vx'],bodies[0]['vy']=-pt/1000
out('sun recoil speed px/s',np.round(-pt/1000,4))
s=Sim(bodies)
Ls=[Laps(i,0) for i in range(1,9)]
# Mars as seen from Earth: apparent longitude
prev=[None]; app=[0]; retro=[]; inretro=[False]; lastang=[None]
def cb(q):
    for l in Ls: l(q)
    d=q.x[4]-q.x[3]; a=math.atan2(d[1],d[0])
    if lastang[0] is not None:
        da=(a-lastang[0]+math.pi)%(2*math.pi)-math.pi
        r=da<0
        if r and not inretro[0]: retro.append(round(q.t/YR,3))
        inretro[0]=r
    lastang[0]=a
E0=s.energy()
s.run(12*YR,cb,every=4)
out('after 12 years: laps',[round(l.laps,3) for l in Ls])
out('expected',[round(12/p[1]**1.5,3) for p in P])
out('energy drift',(s.energy()-E0)/abs(E0),'merges',s.merges)
out('Mars retrograde starts (years from J2000):',retro)

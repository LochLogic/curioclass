from pu import *
# Binary: two stars 500 each, separation 200 -> each v
m=500; d=200; vb=math.sqrt(G*m/(2*d)); Pb=2*math.pi*(d/2)/vb
out('binary each speed',round(vb,2),'drag',round(vb/2,1),'period',round(Pb,3))
def binary(extra=[],T=60):
    b=[dict(kind='star',m=m,x=-d/2,y=0,vx=0,vy=-vb),dict(kind='star',m=m,x=d/2,y=0,vx=0,vy=vb)]+extra
    return Sim(b)
s=binary(); L=Laps(1,0); s.run(30,L); out('binary 30s laps',round(L.laps,2),s.merges)
# circumbinary planet at R from COM
class LapCOM:
    def __init__(s,i): s.i=i; s.acc=0; s.prev=None; s.rmin=1e9
    def __call__(s,q):
        c=(q.m[0]*q.x[0]+q.m[1]*q.x[1])/(q.m[0]+q.m[1]); dd=q.x[s.i]-c; a=math.atan2(dd[1],dd[0]); s.rmin=min(s.rmin,math.hypot(*dd))
        if s.prev is not None:
            da=(a-s.prev+math.pi)%(2*math.pi)-math.pi; s.acc+=da
        s.prev=a
for R in [150,200,300,400,500,600]:
    v=circ(1000+10,R)
    s=binary([dict(kind='planet',x=0,y=R,vx=-v,vy=0)])
    L=LapCOM(2); fate='ok'
    def cb(q):
        L(q)
    s.run(60,cb,every=4)
    E=None
    if s.alive[2]:
        c=(s.m[0]*s.x[0]+s.m[1]*s.x[1]+0)/(s.m[0]+s.m[1]); cv=(s.m[0]*s.v[0]+s.m[1]*s.v[1])/(s.m[0]+s.m[1])
        dd=s.x[2]-c; dv=s.v[2]-cv; E=0.5*dv@dv-G*1000/math.hypot(*dd)
    out('circumbinary R',R,'R/sep',R/d,'laps',round(L.acc/2/math.pi,2),'rmin',round(L.rmin),'merges',s.merges,'E',None if E is None else round(E))

import numpy as np, math
g=9.81
# member types: A m2, I m4, E kN/m2, strength kN/m2, kg/m, $/m, tension_only
MT={
 'T': dict(name='Timber',A=0.0225,I=0.15**4/12,E=12e6,f=20e3,kgm=11.25,cost=50,cable=False),
 'TH':dict(name='Big timber',A=0.0625,I=0.25**4/12,E=12e6,f=20e3,kgm=31.25,cost=120,cable=False),
 'S': dict(name='Steel tube',A=0.15**2-0.134**2,I=(0.15**4-0.134**4)/12,E=200e6,f=250e3,kgm=7850*(0.15**2-0.134**2),cost=150,cable=False),
 'SH':dict(name='Big steel',A=0.25**2-0.23**2,I=(0.25**4-0.23**4)/12,E=200e6,f=250e3,kgm=7850*(0.25**2-0.23**2),cost=320,cable=False),
 'C': dict(name='Cable',A=7.54e-4,I=0,E=160e6,f=1.0e3/7.54e-4*1,kgm=6.0,cost=40,cable=True),
}
MT['C']['f']=1000/7.54e-4  # 1000 kN breaking
JOINT_COST=300; FOOT_COST=2000
DECK_W=2.0 # kN/m per side truss (slab)
TRUCKS={ # name: total t, axles list (offset from front m, tonnes)
 'Pickup':[(0,1.4),(3.7,1.6)],
 'School bus':[(0,4.6),(6.1,9.0)],
 'Fire engine':[(0,8.2),(5.0,5.9),(6.3,5.9)],
 'Grain truck':[(0,8.0),(5.5,7.71),(6.8,7.71)],
 'Semi':[(0,5.44),(5.5,7.71),(6.8,7.71),(17.0,7.71),(18.3,7.71)],
}
def tw(n): return sum(a for _,a in TRUCKS[n])

class Truss:
    def __init__(s,joints,members,supports):
        s.J=[tuple(map(float,j)) for j in joints]; s.M=members; s.S=supports  # supports: {ji:'pin'|'roller'}
    def geom(s,m):
        a,b,t=m; (x1,y1),(x2,y2)=s.J[a],s.J[b]; L=math.hypot(x2-x1,y2-y1); return L,(x2-x1)/L,(y2-y1)/L
    def cap(s,m):
        t=MT[m[2]]; L,_,_=s.geom(m)
        ten=t['A']*t['f']
        if t['cable']: return ten,0.0
        eul=math.pi**2*t['E']*t['I']/L**2
        return ten,min(ten,eul)
    def cost(s):
        c=sum(MT[m[2]]['cost']*s.geom(m)[0] for m in s.M)+JOINT_COST*len(s.J)
        c+=FOOT_COST*sum(1 for j in s.S if j not in s.abut)
        return c
    def selfload(s,deck):
        n=len(s.J); F=np.zeros(2*n)
        for m in s.M:
            L,_,_=s.geom(m); w=MT[m[2]]['kgm']*L*g/1000/2  # kN per side? member weight is one member
            F[2*m[0]+1]-=w/2; F[2*m[1]+1]-=w/2
        # deck slab tributary
        xs=sorted(deck,key=lambda j:s.J[j][0])
        for a,b in zip(xs,xs[1:]):
            L=s.J[b][0]-s.J[a][0]; F[2*a+1]-=DECK_W*L/2; F[2*b+1]-=DECK_W*L/2
        return F
    def axleload(s,deck,x,kN):
        n=len(s.J); F=np.zeros(2*n)
        xs=sorted(deck,key=lambda j:s.J[j][0])
        for a,b in zip(xs,xs[1:]):
            xa,xb=s.J[a][0],s.J[b][0]
            if xa<=x<=xb:
                t=(x-xa)/(xb-xa); F[2*a+1]-=kN*(1-t); F[2*b+1]-=kN*t; return F
        return F
    def solve(s,F,active=None):
        n=len(s.J); 
        if active is None: active=[True]*len(s.M)
        for it in range(60):
            K=np.zeros((2*n,2*n))
            for i,m in enumerate(s.M):
                if not active[i]: continue
                t=MT[m[2]]; L,c,sn=s.geom(m); k=t['E']*t['A']/L
                v=np.array([-c,-sn,c,sn]); d=[2*m[0],2*m[0]+1,2*m[1],2*m[1]+1]
                K[np.ix_(d,d)]+=k*np.outer(v,v)
            fixed=set()
            for j,ty in s.S.items():
                fixed.add(2*j+1)
                if ty=='pin': fixed.add(2*j)
            free=[i for i in range(2*n) if i not in fixed]
            Kf=K[np.ix_(free,free)]
            # mechanism check via smallest eigenvalue relative
            w=np.linalg.eigvalsh(Kf)
            if w[0] < 1e-9*w[-1]:
                return None,None
            u=np.zeros(2*n); u[free]=np.linalg.solve(Kf,F[free])
            forces=[]
            for i,m in enumerate(s.M):
                t=MT[m[2]]; L,c,sn=s.geom(m)
                du=(u[2*m[1]]-u[2*m[0]])*c+(u[2*m[1]+1]-u[2*m[0]+1])*sn
                forces.append(t['E']*t['A']/L*du if active[i] else 0.0)
            # cables: re-add slack ones that would stretch; else drop the most compressed one
            changed=False
            for i,m in enumerate(s.M):
                if MT[m[2]]['cable'] and not active[i]:
                    L,c,sn=s.geom(m)
                    du=(u[2*m[1]]-u[2*m[0]])*c+(u[2*m[1]+1]-u[2*m[0]+1])*sn
                    if du>1e-12: active[i]=True; changed=True
            if not changed:
                worst=None
                for i,m in enumerate(s.M):
                    if MT[m[2]]['cable'] and active[i] and forces[i]<-1e-9 and (worst is None or forces[i]<forces[worst]): worst=i
                if worst is not None: active[worst]=False; changed=True
            if not changed: return np.array(forces),u
        return np.array(forces),u
    def use(s,f):
        out=[]
        for i,m in enumerate(s.M):
            ten,comp=s.cap(m)
            if f[i]>=0: out.append(f[i]/ten)
            else: out.append(-f[i]/comp if comp>0 else float('inf'))
        return np.array(out)
    def crossing(s,deck,truck,step=0.25,half=True,span=(0,24)):
        ax=TRUCKS[truck]; length=ax[-1][0]
        worst=np.zeros(len(s.M)); worstpos=[None]*len(s.M); maxdefl=0
        Fd=s.selfload(deck)
        x=span[0]
        pos=np.arange(span[0],span[1]+length+step,step)
        for front in pos:
            F=Fd.copy()
            for off,t in ax:
                xa=front-off
                if span[0]<=xa<=span[1]: F+=s.axleload(deck,xa,t*g*(0.5 if half else 1))
            f,u=s.solve(F)
            if f is None: return None
            us=s.use(f)
            for i in range(len(s.M)):
                if us[i]>worst[i]: worst[i]=us[i]; worstpos[i]=front
            maxdefl=max(maxdefl,-u[1::2].min())
        return worst,worstpos,maxdefl

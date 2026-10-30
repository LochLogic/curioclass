import numpy as np, math
from scipy.linalg import eigh
from truss import MT
g=9.81; RHO=1.225; CD_MEM=2.0
WIDTH={'T':0.15,'TH':0.25,'S':0.15,'SH':0.25,'C':0.04}
PAY={'none':(0,0,0),'bell':(2000,1.5,1.2),'tank':(8000,9.0,0.8)}  # kg, area m2, Cd
class Tower:
    def __init__(s,J,M,payload='tank'):
        s.J=[tuple(map(float,p)) for p in J]; s.M=M; s.pay=payload
        s.base=[i for i,p in enumerate(s.J) if abs(p[1])<1e-9]
        n=len(s.J); fixed=set()
        for i in s.base: fixed|={2*i,2*i+1}
        s.free=[d for d in range(2*n) if d not in fixed]
        top=max(p[1] for p in s.J); s.top=[i for i,p in enumerate(s.J) if abs(p[1]-top)<1e-9]
    def geom(s,m):
        (x1,y1),(x2,y2)=s.J[m[0]],s.J[m[1]]; L=math.hypot(x2-x1,y2-y1); return L,(x2-x1)/L,(y2-y1)/L
    def cap(s,m):
        t=MT[m[2]]; L,_,_=s.geom(m); ten=t['A']*t['f']
        if t['cable']: return ten,0.0
        return ten,min(ten,math.pi**2*t['E']*t['I']/L**2)
    def K(s,active=None):
        n=len(s.J); K=np.zeros((2*n,2*n))
        for i,m in enumerate(s.M):
            if active is not None and not active[i]: continue
            t=MT[m[2]]; L,c,sn=s.geom(m); k=t['E']*t['A']/L*1000  # N/m
            v=np.array([-c,-sn,c,sn]); d=[2*m[0],2*m[0]+1,2*m[1],2*m[1]+1]
            K[np.ix_(d,d)]+=k*np.outer(v,v)
        return K[np.ix_(s.free,s.free)]
    def masses(s):
        n=len(s.J); m=np.zeros(n)
        for mm in s.M:
            L,_,_=s.geom(mm); w=MT[mm[2]]['kgm']*L; m[mm[0]]+=w/2; m[mm[1]]+=w/2
        for i in s.top: m[i]+=PAY[s.pay][0]/len(s.top)
        return m
    def Mmat(s):
        m=s.masses(); return np.diag(np.repeat(m,2)[s.free])
    def forces(s,u_free,active=None):
        n=len(s.J); u=np.zeros(2*n); u[s.free]=u_free; out=[]
        for i,m in enumerate(s.M):
            t=MT[m[2]]; L,c,sn=s.geom(m)
            du=(u[2*m[1]]-u[2*m[0]])*c+(u[2*m[1]+1]-u[2*m[0]+1])*sn
            out.append(t['E']*t['A']/L*du*1000/1000 if (active is None or active[i]) else 0)  # kN
        return np.array(out)
    def static_load(s,v10=0.0,gust=1.0):
        n=len(s.J); F=np.zeros(2*n); m=s.masses()
        F[1::2]-=m*g
        if v10>0:
            for mm in s.M:
                (x1,y1),(x2,y2)=s.J[mm[0]],s.J[mm[1]]; dy=abs(y2-y1)
                if dy==0: continue
                zc=max((y1+y2)/2,2.0); v=v10*(zc/10)**(1/7)*gust
                f=0.5*RHO*v*v*CD_MEM*WIDTH[mm[2]]*dy
                F[2*mm[0]]+=f/2; F[2*mm[1]]+=f/2
            mass,A,cd=PAY[s.pay]
            if A>0:
                zt=max(s.J[s.top[0]][1],2.0); v=v10*(zt/10)**(1/7)*gust
                for i in s.top: F[2*i]+=0.5*RHO*v*v*cd*A/len(s.top)
        return F[s.free]
    def solve_static(s,F):
        K=s.K(); w=np.linalg.eigvalsh(K)
        if w[0]<1e-9*w[-1]: return None
        return s.forces(np.linalg.solve(K,F))
    def use(s,f):
        out=[]
        for i,m in enumerate(s.M):
            ten,comp=s.cap(m)
            out.append(f[i]/ten if f[i]>=0 else (-f[i]/comp if comp>0 else 99))
        return np.array(out)
    def modes(s):
        K=s.K(); M=s.Mmat(); w2,phi=eigh(K,M); return np.sqrt(np.maximum(w2,0)),phi
    def shake(s,A_g,f_hz,T=20.0,dt=0.001,zeta=0.05,nmodes=6,ramp=2.0):
        w,phi=s.modes(); w=w[:nmodes]; phi=phi[:,:nmodes]
        M=s.Mmat(); r=np.zeros(len(s.free))
        n=len(s.J)
        for k,d in enumerate(s.free):
            if d%2==0: r[k]=1.0
        gamma=phi.T@M@r  # participation (phi mass-normalized)
        q=np.zeros(nmodes); qd=np.zeros(nmodes)
        F0=s.static_load(); f_static=s.solve_static(F0)
        if f_static is None: return None
        maxuse=0; maxdrift=0; tfail=None
        t=0.0
        while t<T:
            a=A_g*g*math.sin(2*math.pi*f_hz*t)*min(1,t/ramp)
            qdd=-gamma*a-2*zeta*w*qd-w*w*q
            qd+=qdd*dt; q+=qd*dt; t+=dt
            if int(t/dt)%10==0:
                u=phi@q; f=f_static+s.forces(u)
                us=s.use(f).max()
                if us>maxuse: maxuse=us
                drift=abs(u[s.free.index(2*s.top[0])])
                maxdrift=max(maxdrift,drift)
                if us>1 and tfail is None: tfail=t
        return maxuse,maxdrift,tfail
def braced(h=20,base=2,typ='T',brace='T',panel=2,xb=False,taper_top=None):
    # two legs from (0,0),(base,0) to height h, rungs every panel, one diagonal per panel (alternating)
    J=[];M=[]; levels=int(h/panel)
    for k in range(levels+1):
        y=k*panel
        if taper_top is None: xl,xr=0,base
        else:
            w=base+(taper_top-base)*y/h; xl=(base-w)/2; xr=xl+w
        J+= [(xl,y),(xr,y)]
    for k in range(levels):
        a,b,c,d=2*k,2*k+1,2*k+2,2*k+3
        M+=[(a,c,typ),(b,d,typ),(c,d,brace)]
        if brace is not None:
            if xb: M+=[(a,d,brace),(b,c,brace)]
            else: M+= [(a,d,brace)] if k%2==0 else [(b,c,brace)]
    return J,M

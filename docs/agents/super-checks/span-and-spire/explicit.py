import numpy as np, math
from tower import *
JOINT_KG=20.0
def explicit(t,A_g,f_hz,T=15,dt=None,zeta=0.05,ramp=2.0,pretension=100.0,v10=0.0,fail=True,record=False):
    n=len(t.J); X0=np.array(t.J); X=X0.copy(); V=np.zeros_like(X)
    m=t.masses()+JOINT_KG
    a=np.array([mm[0] for mm in t.M]); b=np.array([mm[1] for mm in t.M])
    EA=np.array([MT[mm[2]]['E']*MT[mm[2]]['A']*1000 for mm in t.M])  # N
    L0=np.linalg.norm(X0[b]-X0[a],axis=1); k=EA/L0
    cable=np.array([MT[mm[2]]['cable'] for mm in t.M])
    cap_t=np.array([t.cap(mm)[0] for mm in t.M])*1000; cap_c=np.array([t.cap(mm)[1] for mm in t.M])*1000
    # cables: rest length shortened to give pretension
    Lr=L0.copy(); Lr[cable]=L0[cable]/(1+pretension*1000/EA[cable])
    alive=np.ones(len(t.M),bool)
    base=np.zeros(n,bool); base[t.base]=True
    w,_=t.modes(); w1,w2=w[0],w[1]
    # Rayleigh: zeta at w1 and w2
    beta=2*zeta/(w1+w2); alpha=beta*w1*w2
    if dt is None:
        wmax=np.sqrt((2*k[:,None]/np.minimum(m[a],m[b])[:,None]).max())*2
        dt=min(0.9*2/wmax*(math.sqrt(1+(beta*wmax/2)**2)-beta*wmax/2),2e-4)
    Fext=np.zeros_like(X); Fext[:,1]=-m*g
    Fw=t.static_load(v10) if v10 else None
    if v10:
        full=np.zeros(2*n); full[t.free]=Fw; full[1::2]+=m[:]*g-JOINT_KG*g*0  # remove gravity part added in static_load
        # static_load includes gravity from t.masses(); rebuild wind-only
        full=np.zeros(2*n); F=t.static_load(v10)-t.static_load(0); full[t.free]=F
        Fext[:,0]+=full[0::2]*1000*0+full[0::2]  # static_load in N? masses*g -> N; wind f in N
    steps=int(T/dt); maxuse=0; tfail=None; maxdrift=0; failed=[]
    top=t.top[0]
    for s in range(steps):
        tt=s*dt
        ag=A_g*g*math.sin(2*math.pi*f_hz*tt)*min(1,tt/ramp)
        d=X[b]-X[a]; L=np.linalg.norm(d,axis=1); e=d/L[:,None]
        dv=np.sum((V[b]-V[a])*e,axis=1)
        N=k*(L-Lr)+beta*k*dv
        N[cable]=np.maximum(N[cable],0)
        N[~alive]=0
        F=Fext.copy()
        F[:,0]-=m*ag  # base-relative frame: inertial force
        F-= alpha*m[:,None]*V
        np.add.at(F,a,N[:,None]*e); np.add.at(F,b,-N[:,None]*e)
        F[base]=0
        V+=F/m[:,None]*dt; V[base]=0; X+=V*dt
        if s%20==0:
            Ns=k*(L-Lr)  # kN check without damping part
            use=np.where(Ns>=0,Ns/cap_t,np.where(cap_c>0,-Ns/np.maximum(cap_c,1e-9),0))
            use[~alive]=0
            if tt>0.05: maxuse=max(maxuse,use.max())
            maxdrift=max(maxdrift,abs(X[top,0]-X0[top,0]))
            if fail and use.max()>1 and tt>0.05:
                i=int(use.argmax()); alive[i]=False; failed.append((round(tt,2),i))
                if tfail is None: tfail=tt
    return dict(maxuse=maxuse,drift=maxdrift,tfail=tfail,failed=failed,dt=dt,final_top=X[top]-X0[top])

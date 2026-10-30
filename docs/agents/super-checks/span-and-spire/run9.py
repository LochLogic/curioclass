from designs import *
from tower import *
# 13: crossed cable pratt: cables going slack during semi crossing
tr,deck=build(h=4,diag='C'); tr.abut={0,6}
n=7; top={i:n+i-1 for i in range(1,6)}
for i in range(1,5):
    for m in ((top[i],i+1,'C'),(i,top[i+1],'C')):
        if not any({m[0],m[1]}=={x[0],x[1]} for x in tr.M): tr.M.append(m)
cab=[i for i,m in enumerate(tr.M) if m[2]=='C']
Fd=tr.selfload(deck); prev=None; events=0; slackset=set()
for front in np.arange(0,24+18.3,0.25):
    F=Fd.copy()
    for off,t in TRUCKS['Semi']:
        xa=front-off
        if 0<=xa<=24: F+=tr.axleload(deck,xa,t*g*0.5)
    f,u=tr.solve(F); s=tuple(i for i in cab if abs(f[i])<1e-9)
    if prev is not None and s!=prev: events+=1
    prev=s; slackset|=set(s)
print('crossed cables semi: slack switches',events,'cables ever slack',len(slackset),'of',len(cab))
# Snap: pratt h2 with top chord + end posts big timber -> which fails first
tr,deck=build(h=2,top='TH'); tr.abut={0,6}
report(tr,deck,'pratt h2 big-timber top chord',['Grain truck','Semi'])
w,wp,d=tr.crossing(deck,'Semi'); i=int(np.argmax(w)); print(' semi governing',tr.J[tr.M[i][0]],tr.J[tr.M[i][1]])
# pressure
for top_h in (10,20,26,28,30):
    hw=top_h+3; p=1000*9.81*hw; print(f'tank on {top_h} m, water surface {hw} m: {p/1000:.0f} kPa {p/6894.76:.1f} psi')
# pluck: timber b2 tank, free vibration
J,M=braced(h=20,base=2,typ='T',brace='T'); t=Tower(J,M,'tank'); w,phi=t.modes()
print('f1 %.3f Hz period %.2f s; sways in 10 s %.1f; amplitude after 5 cycles %.2f'%(w[0]/2/math.pi,2*math.pi/w[0],10*w[0]/2/math.pi,math.exp(-0.05*w[0]*5*2*math.pi/w[0])))
# sweep 0.4->5 Hz linear over 20 s, record peak drift and freq
def sweep(t,A=0.1,f0=0.4,f1=5.0,T=20.0,dt=0.001,zeta=0.05):
    w,phi=t.modes(); w=w[:6]; phi=phi[:,:6]; M=t.Mmat()
    r=np.array([1.0 if d%2==0 else 0 for d in t.free]); gam=phi.T@M@r
    q=np.zeros(6); qd=np.zeros(6); ph=0; best=(0,0); tt=0
    k=t.free.index(2*t.top[0])
    while tt<T:
        f=f0+(f1-f0)*tt/T; ph+=2*math.pi*f*dt
        a=A*g*math.sin(ph); qdd=-gam*a-2*zeta*w*qd-w*w*q; qd+=qdd*dt; q+=qd*dt; tt+=dt
        u=phi[k]@q
        if abs(u)>best[0]: best=(abs(u),f)
    return best
for name,kw,pay in [('timber b2 tank',dict(h=20,base=2,typ='T',brace='T'),'tank'),('timber b4 tank',dict(h=20,base=4,typ='T',brace='T'),'tank'),('steel b2 tank',dict(h=20,base=2,typ='S',brace='S'),'tank')]:
    J,M=braced(**kw); t=Tower(J,M,pay); w,_=t.modes()
    for T in (20,40):
        b=sweep(t,T=T); print(f'{name} f1 {w[0]/2/math.pi:.2f} sweep {T}s peak at {b[1]:.2f} Hz drift {b[0]*100:.0f} cm')

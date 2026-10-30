from pu import *
random.seed(3)
# dust disk 240 motes on circular orbits 150..450 around star; giant at 300
def disk(n=240,r0=150,r1=450,M=1000):
    X=[];Vv=[]
    for i in range(n):
        r=random.uniform(r0,r1); th=random.uniform(0,2*math.pi); v=circ(M,r)
        X.append([r*math.cos(th),r*math.sin(th)]); Vv.append([-v*math.sin(th),v*math.cos(th)])
    return X,Vv
X,Vv=disk()
vg=circ(1100,300)
s=Sim([dict(kind='star',x=0,y=0,vx=0,vy=-100*vg/1000),dict(kind='giant',x=300,y=0,vx=0,vy=vg)],dust=(X,Vv))
def census(s):
    r=np.hypot(*(s.dx-s.x[0]).T)[s.dalive]
    gap=((r>250)&(r<350)).sum(); inner=(r<250).sum(); outer=((r>=350)&(r<600)).sum(); far=(r>=600).sum()
    return dict(alive=int(s.dalive.sum()),gap250_350=int(gap),inner=int(inner),outer350_600=int(outer),flung600plus=int(far))
out('t=0',census(s))
P=2*math.pi*300/vg
for k in range(1,6):
    s.run(2*P); out('after %d giant orbits'%(2*k), census(s))
# eaten by

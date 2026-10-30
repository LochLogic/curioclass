from pu import *
def lum(h):
    h=h.lstrip('#'); c=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    c=[x/12.92 if x<=0.03928 else ((x+0.055)/1.055)**2.4 for x in c]; return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
def cr(a,b):
    A,B=lum(a),lum(b); return round((max(A,B)+0.05)/(min(A,B)+0.05),2)
for fg,bg in [('#ff8fd8','#12131f'),('#ff8fd8','#1a1b2b'),('#ff8fd8','#05060d'),('#1a0a17','#ff8fd8'),('#eef0ff','#12131f'),('#a3a8c8','#12131f'),('#a3a8c8','#1a1b2b'),('#eef0ff','#05060d'),('#7fe3ff','#05060d'),('#ffd166','#05060d')]:
    out(fg,'on',bg,cr(fg,bg))
# star wobble radius
out('star wobble radius with giant 100 at 300:',round(300*100/1100,1),'px')
# lane clearing giant band +-10%
random.seed(3)
X=[];Vv=[]
for i in range(240):
    r=random.uniform(150,450); th=random.uniform(0,2*math.pi); v=circ(1000,r); X.append([r*math.cos(th),r*math.sin(th)]); Vv.append([-v*math.sin(th),v*math.cos(th)])
for gm,kind in [(100,'giant'),(10,'planet')]:
    vg=circ(1000+gm,300); P=2*math.pi*300/vg
    s=Sim([dict(kind='star',x=0,y=0,vx=0,vy=-gm*vg/1000),dict(kind=kind,x=300,y=0,vx=0,vy=vg)],dust=(np.array(X),np.array(Vv)))
    def band(s):
        r=np.hypot(*(s.dx-s.x[0]).T)[s.dalive]; return int(((r>270)&(r<330)).sum())
    b0=band(s); res=[]
    for k in range(10): s.run(P); res.append(band(s))
    out(kind,'band 270-330 start',b0,'after each lap',res)

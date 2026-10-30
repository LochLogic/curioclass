from pu import *
vr=circ(1010,250); out('starter: planet vy',round(vr*1000/1010,3),'star vy',round(-vr*10/1010,3),'period',round(2*math.pi*250/vr,3))
s=Sim([dict(kind='star',x=0,y=0,vx=0,vy=-vr*10/1010),dict(kind='planet',x=250,y=0,vx=0,vy=vr*1000/1010)]); rr=[]
s.run(30,lambda q: rr.append(math.hypot(*(q.x[1]-q.x[0])))); out(' starter separation range',round(min(rr),3),round(max(rr),3))
vr=circ(1100,300); gv=vr*1000/1100; sv=-vr*100/1100
out('giant: giant vy',round(gv,3),'star vy',round(sv,3),'period',round(2*math.pi*300/vr,3),'star wobble radius',round(300*100/1100,2))
vm=circ(100.3,40)
for n in [0,2,4,6,8,10,14]:
    f=1.15*0.99**n
    s=Sim([dict(kind='star',x=0,y=0,vx=0,vy=sv),dict(kind='giant',x=300,y=0,vx=0,vy=gv),dict(kind='moon',x=340,y=0,vx=0,vy=gv+vm*f)])
    Lm=Laps(2,1); t10=[None]
    def cb(q):
        if not q.alive[2]: return
        Lm(q)
        if t10[0] is None and Lm.laps>=10: t10[0]=round(q.t,1)
    s.run(40,cb,every=2)
    out(' rescue Slower x%d f=%.3f crash %s 10 laps at %s'%(n,f,s.merges[:1],t10[0]))
# lane with correct split
random.seed(3); X=[];Vv=[]
for i in range(240):
    r=random.uniform(150,450); th=random.uniform(0,2*math.pi); v=circ(1000,r); X.append([r*math.cos(th),r*math.sin(th)]); Vv.append([-v*math.sin(th),v*math.cos(th)])
s=Sim([dict(kind='star',x=0,y=0,vx=0,vy=sv),dict(kind='giant',x=300,y=0,vx=0,vy=gv)],dust=(np.array(X),np.array(Vv)))
def band(s):
    r=np.hypot(*(s.dx-s.x[0]).T)[s.dalive]; return int(((r>270)&(r<330)).sum())
P=2*math.pi*300/vr; b=[band(s)]
for k in range(5): s.run(P); b.append(band(s))
out('lane (giant, correct split): band count at 0..5 laps',b)
# trojan with correct split, planet 10
vr=circ(1010,300); pv=vr*1000/1010; sv2=-vr*10/1010
for f,ang in [(1,60),(1.03,60),(0.97,60),(1,45),(1,75)]:
    a=math.radians(ang); vt=vr*f  # trojan moves with rotating frame speed
    s=Sim([dict(kind='star',x=0,y=0,vx=0,vy=sv2),dict(kind='planet',x=300,y=0,vx=0,vy=pv),dict(kind='comet',x=300*math.cos(a),y=300*math.sin(a),vx=-vt*math.sin(a),vy=vt*math.cos(a))])
    lead=[999,-999]
    def cb(q):
        p=q.x[1]-q.x[0]; c=q.x[2]-q.x[0]; d=math.degrees((math.atan2(c[1],c[0])-math.atan2(p[1],p[0])+math.pi)%(2*math.pi)-math.pi); lead[0]=min(lead[0],d); lead[1]=max(lead[1],d)
    s.run(5*2*math.pi*300/vr,cb,every=8); out(' trojan speed x%.2f at %d deg: lead range %.1f..%.1f'%(f,ang,*lead))

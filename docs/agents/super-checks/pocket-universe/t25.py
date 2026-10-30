from pu import *
v=circ(1010,250); out('starter planet v',round(v,2),'star v',round(-10*v/1000,3),'period',round(2*math.pi*250/v*1000/1010*1,3))
L=200;m=300;t0=math.sqrt(L**3/(G*m));V=L/t0
x1=np.array([0.97000436,-0.24308753]); v3=np.array([-0.93240737,-0.86473146])
out('dance pos1',np.round(x1*L,2),'pos2',np.round(-x1*L,2),'v1=v2',np.round(-v3/2*V,2),'v3',np.round(v3*V,2),'period',round(6.32591398*t0,3))
vg=circ(1100,300); out('giant vg',round(vg,2),'star v',round(-100*vg/1000,3),'giant period around star', round(2*math.pi*300/vg,2))
vm=circ(100.3,40); out('rescue moon rel circ',round(vm,2),'x1.15',round(1.15*vm,2),'abs vy',round(vg+1.15*vm,2), 'moon period about giant',round(2*math.pi*40/vm,3))
out('two suns sep100 v',round(math.sqrt(G*500/200),2))
# black hole whirl circular speeds and gravity thresholds
for r in (80,450): out('whirl r',r,'v',round(circ(3000,r),1),'period',round(2*math.pi*r/circ(3000,r),2))
for g in (0.4,0.5,0.6,0.8,1.5,2.0):
    if g<=0.5: out('gravity',g,': circular orbits become unbound (E>=0)')
    else:
        a=1/(2-1/g); out('gravity',g,': circle at r becomes ellipse r..%.2fr'%(2*a-1) if g<1 else ': circle at r becomes ellipse %.3fr..r'%(2*a-1))
# whirl sim check at g=0.45 and 0.6
random.seed(9); X=[];Vv=[]
for i in range(240):
    r=random.uniform(80,450); th=random.uniform(0,2*math.pi); vv=circ(3000,r); X.append([r*math.cos(th),r*math.sin(th)]); Vv.append([-vv*math.sin(th),vv*math.cos(th)])
for g in (0.45,0.6,1.0):
    s=Sim([dict(kind='hole',m=3000,x=0,y=0,vx=0,vy=0)],dust=(np.array(X),np.array(Vv)),gscale=g); s.run(20)
    r=np.hypot(*s.dx.T)[s.dalive]; out('whirl gravity',g,'after 20 s: motes beyond 1500 px',int((r>1500).sum()),'max r',round(r.max()),'eaten',int((~s.dalive).sum()))
# halve star date: E
out('escape speed ratio check sqrt2:',round(math.sqrt(2),4))

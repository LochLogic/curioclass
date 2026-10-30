from pu import *
def trojan(pm,pk,f=1.0,ang=60,T=None,R=300):
    M=1000; vp=circ(M+pm,R); P=2*math.pi*R/vp; T=T or 5*P
    # star moves to keep COM at rest
    a=math.radians(ang); vt=circ(M+pm,R)*f
    b=[dict(kind='star',x=0,y=0,vx=0,vy=-pm*vp/M),dict(kind=pk,m=pm,x=R,y=0,vx=0,vy=vp),
       dict(kind='comet',x=R*math.cos(a),y=R*math.sin(a),vx=-vt*math.sin(a),vy=vt*math.cos(a))]
    s=Sim(b); lead=[1e9,-1e9]
    def cb(q):
        if not q.alive[2]: return
        p=q.x[1]-q.x[0]; c=q.x[2]-q.x[0]
        da=math.degrees((math.atan2(c[1],c[0])-math.atan2(p[1],p[0])+math.pi)%(2*math.pi)-math.pi)
        lead[0]=min(lead[0],da); lead[1]=max(lead[1],da)
    s.run(T,cb,every=8)
    return 'T=%.1fs lead angle %.1f..%.1f merges %s'%(T,lead[0],lead[1],s.merges)
out('planet10 exact', trojan(10,'planet'))
out('planet10 +3% speed', trojan(10,'planet',1.03))
out('planet10 -3% speed', trojan(10,'planet',0.97))
out('planet10 at 70 deg', trojan(10,'planet',1,70))
out('planet10 at 45 deg', trojan(10,'planet',1,45))
out('planet10 behind -60', trojan(10,'planet',1,-60))
out('giant100 exact', trojan(100,'giant'))
out('giant30 exact (ratio .03)', trojan(30,'giant'))

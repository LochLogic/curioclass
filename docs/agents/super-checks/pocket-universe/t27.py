from pu import *
import sys
vr=circ(1100,300); gv=vr*1000/1100; sv=-vr*100/1100
d=float(sys.argv[1])
vm=circ(100.3,d); row=[]
for f in [0.75,0.8,0.85,0.9,0.95,1.0,1.05,1.1,1.15,1.2,1.25,1.3]:
    s=Sim([dict(kind='star',x=0,y=0,vx=0,vy=sv),dict(kind='giant',x=300,y=0,vx=0,vy=gv),dict(kind='moon',x=300+d,y=0,vx=0,vy=gv+vm*f)])
    Lm=Laps(2,1); t10=[None]
    def cb(q):
        if not q.alive[2]: return
        Lm(q)
        if t10[0] is None and Lm.laps>=10: t10[0]=round(q.t,1)
    s.run(30,cb,every=2)
    row.append('%.2f:%s'%(f,('ok10@%s'%t10[0]) if t10[0] and not s.merges else ('crash@%.1f'%s.merges[0][0] if s.merges else 'nolaps')+('(10L)' if t10[0] else '')))
out('d',d,'moon period',round(2*math.pi*d/vm,2),row)

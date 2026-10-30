exec(open('t14.py').read().split("out('exact")[0])
a=make(); b=make(tuple(v3*V*0.01)); c=make(tuple(v3*V*0.02))
n=int(20*P/DT); first={};firstc={}
for k in range(n):
    a.step(); b.step(); c.step()
    if k%48==0:
        for s,f in ((b,first),(c,firstc)):
            if s.alive.all() and a.alive.all():
                dd=max(math.hypot(*(s.x[i]-a.x[i])) for i in range(3))
                for th in (10,50,100):
                    if dd>th and th not in f: f[th]=round(a.t/P,2)
out('1% nudge: rounds until a dancer is >10/50/100 px from its old ghost',first)
out('2% nudge:',firstc)
# Also a planet: how fast does a 1% nudge diverge in a simple star+planet orbit (not chaotic)?
from pu import Sim as S2
v=circ(1010,250)
p=S2([dict(kind='star',x=0,y=0,vx=0,vy=0),dict(kind='planet',x=250,y=0,vx=0,vy=v)]); q=S2([dict(kind='star',x=0,y=0,vx=0,vy=0),dict(kind='planet',x=250,y=0,vx=0,vy=v*1.01)])
p.run(10*7.8); q.run(10*7.8); out('simple orbit +1%: gap after 10 laps px',round(math.hypot(*(p.x[1]-q.x[1])),1))

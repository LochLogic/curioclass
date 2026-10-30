from explicit import *
import time
for name,kw,pay,fh in [('timber b2 tank',dict(h=20,base=2,typ='T',brace='T'),'tank',1.4),
                       ('timber b2 tank',dict(h=20,base=2,typ='T',brace='T'),'tank',0.8),
                       ('steel b2 tank',dict(h=20,base=2,typ='S',brace='S'),'tank',1.4)]:
    J,M=braced(**kw); t=Tower(J,M,pay)
    t0=time.time(); r=explicit(t,0.3,fh,T=12,fail=False)
    mu,dr,tf=t.shake(0.3,fh,T=12)
    print(name,fh,'explicit use %.0f%% drift %.0f cm dt %.1e (%.0fs) | modal use %.0f%% drift %.0f cm'%(r['maxuse']*100,r['drift']*100,r['dt'],time.time()-t0,mu*100,dr*100))

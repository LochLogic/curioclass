from tower import *
import time
cases=[('timber b2 tank',dict(h=20,base=2,typ='T',brace='T'),'tank'),
       ('steel b2 tank',dict(h=20,base=2,typ='S',brace='S'),'tank'),
       ('timber b4 tank',dict(h=20,base=4,typ='T',brace='T'),'tank'),
       ('timber b2 none',dict(h=20,base=2,typ='T',brace='T'),'none')]
for name,kw,pay in cases:
    J,M=braced(**kw); t=Tower(J,M,pay); w,_=t.modes(); f1=w[0]/2/math.pi
    row=[]
    for fh in (0.8,1.4,2.5,4.3):
        mu,dr,tf=t.shake(0.3,fh,T=15)
        row.append(f'{fh}Hz {mu*100:4.0f}% {dr*100:4.0f}cm{" X@%.1fs"%tf if tf else ""}')
    print(f'{name:16s} f1 {f1:.2f} | '+' | '.join(row))

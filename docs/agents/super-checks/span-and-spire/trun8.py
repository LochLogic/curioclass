from trun7 import *
print('==== search')
opts=[]
for name,hwf in [('straight2',lambda y:1),('straight3',lambda y:1.5),('straight4',lambda y:2),('stepped',hw26),('step 4/2',lambda y:2 if y<=12 else 1),('step 6/2',lambda y:3 if y<=12 else 1)]:
    for typ in ('T','TH','S','SH'):
        for br in ('T','S'):
            J,M=sched(26,hwf,typ,br); t=Tower(J,M,'tank'); w,_=t.modes()
            wu=t.use(t.solve_static(t.static_load(50))).max()
            mu,dr,tf=t.shake(0.3,1.2,T=15)
            if wu<=1 and mu<=1: print(f'PASS {name} legs {typ} brace {br} f1 {w[0]/2/math.pi:.2f} wind {wu*100:.0f}% quake {mu*100:.0f}%')

from tower import *
for kw in [dict(h=30,base=2),dict(h=30,base=4),dict(h=30,base=6,taper_top=2),dict(h=30,base=4,taper_top=2),dict(h=10,base=2),dict(h=30,base=2,typ='TH',brace='T')]:
    kw2=dict(typ='T',brace='T'); kw2.update(kw)
    J,M=braced(**kw2); t=Tower(J,M,'tank'); w,_=t.modes()
    s=f"{kw} members {len(M)} joints {len(J)} f1 {w[0]/2/math.pi:.2f}Hz gravity {t.use(t.solve_static(t.static_load())).max()*100:.0f}%"
    for v in (30,40,50,60,70): s+=f" w{v}:{t.use(t.solve_static(t.static_load(v))).max()*100:.0f}%"
    print(s)

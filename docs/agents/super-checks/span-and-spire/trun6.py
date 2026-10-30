from tower import *
cands=[('26 m tapered 6->2 timber',dict(h=26,base=6,taper_top=2,typ='T',brace='T')),
       ('26 m straight 2 timber',dict(h=26,base=2,typ='T',brace='T')),
       ('26 m straight 4 timber',dict(h=26,base=4,typ='T',brace='T')),
       ('26 m tapered 6->2 big timber legs',dict(h=26,base=6,taper_top=2,typ='TH',brace='T')),
       ('26 m tapered 6->2 steel',dict(h=26,base=6,taper_top=2,typ='S',brace='S')),
       ('20 m straight 2 timber',dict(h=20,base=2,typ='T',brace='T'))]
for name,kw in cands:
    J,M=braced(**kw); t=Tower(J,M,'tank'); w,_=t.modes()
    s=f'{name:36s} m{len(M)} f1 {w[0]/2/math.pi:.2f} w50 {t.use(t.solve_static(t.static_load(50))).max()*100:.0f}%'
    for fh in (0.6,0.8,1.0,1.2,1.5,2.0):
        mu,dr,tf=t.shake(0.3,fh,T=15); s+=f' | {fh}:{mu*100:.0f}'
    print(s)

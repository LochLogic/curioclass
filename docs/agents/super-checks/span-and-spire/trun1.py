from tower import *
J,M=braced(h=20,base=2,brace=None); M=[m for m in M if m[2] is not None]
t=Tower(J,M); print('ladder no diagonals static:', t.solve_static(t.static_load()) is None and 'MECHANISM')
for pay in ['none','bell','tank']:
  for typ,br in [('T','T'),('S','S')]:
    for base in [2,4]:
        J,M=braced(h=20,base=base,typ=typ,brace=br)
        t=Tower(J,M,pay); w,_=t.modes()
        f=t.solve_static(t.static_load()); 
        print(f'h20 base{base} {typ} pay {pay}: mass {t.masses().sum():.0f} kg f1 {w[0]/2/math.pi:.2f} Hz f2 {w[1]/2/math.pi:.2f} gravity use {t.use(f).max()*100:.0f}%', end='')
        for v in (30,50,70):
            fw=t.solve_static(t.static_load(v)); print(f' | wind {v}: {t.use(fw).max()*100:.0f}%',end='')
        print()

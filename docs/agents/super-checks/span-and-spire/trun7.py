from tower import *
from explicit import explicit
def sched(h,halfw,typ='T',brace='T',panel=2):
    J=[];M=[]
    for k in range(h//panel+1):
        y=k*panel; w=halfw(y); J+=[(-w,y),(w,y)]
    for k in range(h//panel):
        a,b,c,d=2*k,2*k+1,2*k+2,2*k+3
        M+=[(a,c,typ),(b,d,typ),(c,d,brace)]
        M+= [(a,d,brace)] if k%2==0 else [(b,c,brace)]
    return J,M
def hw30(y): return 3 if y<=10 else (2 if y<=20 else 1)
def hw26(y): return 3 if y<=8 else (2 if y<=18 else 1)
def rep(name,J,M,pay='tank',winds=(50,60,70),shakes=()):
    t=Tower(J,M,pay); w,_=t.modes()
    s=f'{name:34s} m{len(M)} j{len(J)} top {max(p[1] for p in J):.0f} f1 {w[0]/2/math.pi:.2f}Hz grav {t.use(t.solve_static(t.static_load())).max()*100:.0f}%'
    for v in winds: s+=f' w{v}:{t.use(t.solve_static(t.static_load(v))).max()*100:.0f}%'
    for A,fh in shakes:
        mu,dr,tf=t.shake(A,fh,T=15); s+=f' | {A}g {fh}Hz:{mu*100:.0f}%'+(f' fail@{tf:.1f}s' if tf else '')
    print(s); return t
rep('30 m stepped 6/4/2 timber',*sched(30,hw30),winds=(50,60,70))
rep('30 m straight 4 timber',*sched(30,lambda y:2),winds=(50,60,70))
rep('30 m straight 2 timber',*sched(30,lambda y:1),winds=(40,50))
print('-- town tower: 26 m, wind 50, 0.3 g 1.2 Hz')
for name,args in [('26 straight 2 timber',(26,lambda y:1)),('26 stepped timber',(26,hw26)),('26 stepped big-timber legs',(26,hw26,'TH','T')),('26 straight 4 timber',(26,lambda y:2))]:
    rep(name,*sched(*args),winds=(50,),shakes=((0.3,1.2),))
print('-- 20 m towers')
for name,hwf,typ,pay in [('20 m 2 wide timber tank',lambda y:1,'T','tank'),('20 m 4 wide timber tank',lambda y:2,'T','tank'),('20 m 2 wide steel tank',lambda y:1,'S','tank'),('20 m 2 wide timber empty',lambda y:1,'T','none'),('20 m 2 wide timber bell',lambda y:1,'T','bell')]:
    J,M=sched(20,hwf,typ,typ); rep(name,J,M,pay,winds=(50,70),shakes=((0.3,0.8),(0.3,1.4)))
J,M=sched(10,lambda y:1); rep('10 m 2 wide timber tank',J,M,winds=(50,70))

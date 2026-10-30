from pu import *
gm=100; R=300; vg=circ(1100,R)
for d,f in [(50,1.0),(60,1.0),(40,1.15)]:
    vm=circ(gm+0.3,d)*f
    s=Sim([dict(kind='star',x=0,y=0,vx=0,vy=-gm*vg/1000),dict(kind='giant',x=R,y=0,vx=0,vy=vg),dict(kind='moon',x=R+d,y=0,vx=0,vy=vg+vm)])
    Lg=Laps(2,1); st={'lost':None,'Ls':None,'cap':None}
    def cb(q):
        if not q.alive[2]: return
        Lg(q)
        Eg=twobody_E(q,2,1); Es=twobody_E(q,2,0)
        if st['lost'] is None and Eg>0: st['lost']=round(q.t,1); st['Ls']=Laps(2,0)
        if st['Ls'] is not None:
            st['Ls'](q)
            if Es<0 and Eg>0 and abs(st['Ls'].laps)>=2 and st['cap'] is None: st['cap']=round(q.t,1)
    s.run(120,cb,every=4)
    out('moon d',d,'f',f,'laps around giant before loss',round(Lg.laps,1),'lost at',st['lost'],'2 laps around star alone at',st['cap'],'merges',s.merges)

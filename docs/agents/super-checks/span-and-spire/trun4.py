from explicit import *
J,M=braced(h=20,base=2,typ='S',brace='S'); t=Tower(J,M,'tank')
r=explicit(t,0.3,1.4,T=8,fail=True); print('steel b2 tank 1.4Hz collapse: first fail %.2fs, %d members failed, top moved'%(r['tfail'],len(r['failed'])),np.round(r['final_top'],1))
# guyed: timber ladder b2 h20 + guys from top to table edges
J,M=braced(h=20,base=2,typ='T',brace='T')
J=J+[(-5,0),(7,0)]; top=[i for i,p in enumerate(J) if p[1]==20]
M=M+[(len(J)-2,top[0],'C'),(len(J)-1,top[1],'C')]
t=Tower(J,M,'tank'); w,_=t.modes(); print('guyed f1 %.2f Hz'%(w[0]/2/math.pi))
for fh in (0.8,1.4,w[0]/2/math.pi):
    r=explicit(t,0.3,fh,T=10,fail=False,pretension=100)
    print('guyed %.2f Hz use %.0f%% drift %.0f cm'%(fh,r['maxuse']*100,r['drift']*100))
for v in (50,70):
    fw=t.solve_static(t.static_load(v)); print('guyed wind',v, '%.0f%%'%(t.use(fw).max()*100))

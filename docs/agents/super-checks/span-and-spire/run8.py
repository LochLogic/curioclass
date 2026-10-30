from designs import *
import time
T5=['Pickup','School bus','Fire engine','Grain truck','Semi']
tr,deck=build(h=2); tr.abut={0,6}
report(tr,deck,'pratt h2 no pier',T5)
tr.J.append((12.0,-5.0)); k=len(tr.J)-1
tr.M.append((3,k,'T')); tr.S[k]='pin'
report(tr,deck,'pratt h2 + timber pier in stream',T5)
# big design near the limit: 12 panels of 2 m, h3, crossed cables
tr,deck=build(panels=12,h=3,diag='T')
n=13; top={i:n+i-1 for i in range(1,12)}
for i in range(1,11):
    for m in ((top[i],i+1,'C'),(i,top[i+1],'C')):
        if not any({m[0],m[1]}=={x[0],x[1]} for x in tr.M): tr.M.append(m)
tr.abut={0,12}
t0=time.time(); report(tr,deck,'12 panels crossed',['Semi']); print('time',round(time.time()-t0,2),'s for',int((24+18.3)/0.25),'positions')

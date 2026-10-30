from designs import *
T5=['Pickup','School bus','Fire engine','Grain truck','Semi']
def addX(tr,panels=6,typ='C'):
    # add the opposite diagonal in every interior panel
    n=panels+1
    top={i:n+i-1 for i in range(1,panels)}
    for i in range(1,panels-1):
        a=(top[i],i+1,typ); b=(i,top[i+1],typ)
        for m in (a,b):
            if not any({m[0],m[1]}=={x[0],x[1]} for x in tr.M): tr.M.append(m)
tr,deck=build(h=4,diag='C'); addX(tr); report(tr,deck,'pratt h4 crossed cables')
# C4: h6 failing; fix A: end posts big timber; fix B: brace end posts at midpoint
tr,deck=build(h=6); report(tr,deck,'pratt h6 timber (fails)',['Fire engine','Semi'])
tr,deck=build(h=6); 
for i,m in enumerate(tr.M):
    if {tr.J[m[0]],tr.J[m[1]]} in ({(0.0,0.0),(4.0,6.0)},{(24.0,0.0),(20.0,6.0)}): tr.M[i]=(m[0],m[1],'TH')
report(tr,deck,'pratt h6, end posts Big timber',['Fire engine','Semi'])
# brace: split end post at (2,3), add member (2,3)-(4,0)
tr,deck=build(h=6)
J=tr.J; M=tr.M
def split(a,b,pt,brace_to):
    J.append(pt); k=len(J)-1
    for i,m in enumerate(M):
        if {m[0],m[1]}=={a,b}: t=m[2]; del M[i]; break
    M.append((a,k,t)); M.append((k,b,t)); M.append((k,brace_to,'T'))
ji=lambda p: J.index(p)
split(ji((0.0,0.0)),ji((4.0,6.0)),(2.0,3.0),ji((4.0,0.0)))
split(ji((24.0,0.0)),ji((20.0,6.0)),(22.0,3.0),ji((20.0,0.0)))
report(tr,deck,'pratt h6, end posts braced at middle',['Fire engine','Semi'])

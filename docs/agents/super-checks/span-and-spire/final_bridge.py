from designs import *
from run6 import warren
T5=['Pickup','School bus','Fire engine','Grain truck','Semi']
def table(name,tr,deck):
    tr.abut={deck[0],deck[-1]} if not hasattr(tr,'abut') else tr.abut
    out=[]
    for t in T5:
        r=tr.crossing(deck,t,step=0.05)
        out.append('MECH' if r is None else f'{r[0].max()*100:.1f}')
    print(f'{name:34s} ${tr.cost():>7,.0f} m{len(tr.M):2d} j{len(tr.J):2d} | '+' '.join(f'{x:>6s}' for x in out))
print(' '*34,'cost      mem jnt |  Pick   Bus  Fire Grain  Semi')
tr,deck=build(h=4); table('A Pratt h4 timber',tr,deck)
tr,deck=build(h=5); table('B Pratt h5 timber',tr,deck)
tr,deck=build(h=6); table('C Pratt h6 timber',tr,deck)
tr,deck=build(h=2); table('D Pratt h2 timber',tr,deck)
tr,deck=build(h=2,kind='howe'); table('E Howe h2 timber (old bridge)',tr,deck)
tr,deck=build(h=4,diag='C'); table('F Pratt h4 cable diagonals',tr,deck)
tr,deck=build(h=4,diag='C',kind='howe'); table('G Howe h4 cable diagonals',tr,deck)
tr,deck=build(h=4,diag='C'); n=7; top={i:n+i-1 for i in range(1,6)}
for i in range(1,5):
    for m in ((top[i],i+1,'C'),(i,top[i+1],'C')):
        if not any({m[0],m[1]}=={x[0],x[1]} for x in tr.M): tr.M.append(m)
table('H Pratt h4 crossed cables',tr,deck)
tr,deck=warren(6,4); table('I Warren 6x4 h4 timber',tr,deck)
tr,deck=warren(6,4)
for i in (0,1,2,3,4,5,12,14,19,21): tr.M[i]=(tr.M[i][0],tr.M[i][1],'C')
table('J Warren shoestring (10 cables)',tr,deck)
tr,deck=build(h=2); tr.J.append((12.0,-5.0)); k=len(tr.J)-1; tr.M.append((3,k,'T')); tr.S[k]='pin'; tr.abut={0,6}
table('K Pratt h2 + pier in stream',tr,deck)
tr,deck=build(h=1,top='TH')
for i,m in enumerate(tr.M):
    if tr.J[m[0]][1]!=tr.J[m[1]][1] and tr.J[m[0]][0]!=tr.J[m[1]][0]: tr.M[i]=(m[0],m[1],'TH')
table('L Pratt h1 big top+diag (snap)',tr,deck)
tr,deck=build(h=6)
for i,m in enumerate(tr.M):
    if {tr.J[m[0]],tr.J[m[1]]} in ({(0.0,0.0),(4.0,6.0)},{(24.0,0.0),(20.0,6.0)}): tr.M[i]=(m[0],m[1],'TH')
table('M Pratt h6, end posts Big timber',tr,deck)
tr,deck=build(h=6); J=tr.J; M=tr.M
def split(a,b,pt,brace_to):
    J.append(pt); k=len(J)-1
    for i,m in enumerate(M):
        if {m[0],m[1]}=={a,b}: t=m[2]; del M[i]; break
    M.append((a,k,t)); M.append((k,b,t)); M.append((k,brace_to,'T'))
ji=lambda p: J.index(p)
split(ji((0.0,0.0)),ji((4.0,6.0)),(2.0,3.0),ji((4.0,0.0))); split(ji((24.0,0.0)),ji((20.0,6.0)),(22.0,3.0),ji((20.0,0.0)))
table('N Pratt h6, end posts braced',tr,deck)
tr,deck=build(panels=12,h=3); n=13; top={i:n+i-1 for i in range(1,12)}
for i in range(1,11):
    for m in ((top[i],i+1,'C'),(i,top[i+1],'C')):
        if not any({m[0],m[1]}=={x[0],x[1]} for x in tr.M): tr.M.append(m)
table('O 12 panels h3 crossed (big)',tr,deck)
J=[(i*4,0) for i in range(7)]; M=[(i,i+1,'T') for i in range(6)]; tr=Truss(J,M,{0:'pin',6:'roller'}); table('P bare deck',tr,list(range(7)))

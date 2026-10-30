from run5 import *
def warren(panels=6,h=4,L=24,verts=False):
    p=L/panels; J=[(i*p,0) for i in range(panels+1)]
    tops=[]
    for i in range(panels): tops.append(len(J)); J.append((i*p+p/2,h))
    M=[(i,i+1,'T') for i in range(panels)]
    for i in range(panels-1): M.append((tops[i],tops[i+1],'T'))
    for i in range(panels): M.append((i,tops[i],'T')); M.append((tops[i],i+1,'T'))
    tr=Truss(J,M,{0:'pin',panels:'roller'}); tr.abut={0,panels}; return tr,list(range(panels+1))
for panels in (4,6,8):
  for h in (2,3,4,5):
    tr,deck=warren(panels,h)
    W=autosize(tr,deck,['Grain truck','Semi'],0.667)
    if W is None: print('warren',panels,h,'none'); continue
    cnt={k:v for k in MT if (v:=sum(1 for m in tr.M if m[2]==k))}
    print(f'warren panels {panels} h {h}: cost ${tr.cost():,.0f} max {W.max()*100:.1f}% members {len(tr.M)} joints {len(tr.J)} {cnt}')

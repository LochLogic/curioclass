from designs import *
# deck only
J=[(i*4,0) for i in range(7)]; M=[(i,i+1,'T') for i in range(6)]
tr=Truss(J,M,{0:'pin',6:'roller'}); tr.abut={0,6}
print('deck only', tr.crossing(list(range(7)),'Pickup'))
for k in ['pratt','howe']:
  for h in [3,4,6]:
    tr,deck=build(h=h,kind=k); report(tr,deck,f'{k} timber h{h}')

from run6 import warren, envelope, autosize
from designs import *
import itertools
tr,deck=warren(6,4)
W=envelope(tr,deck,['Grain truck','Semi'])
print('warren6 h4 timber cost',round(tr.cost()),'max',round(W.max()*100,1))
for i,m in enumerate(tr.M): print(i,tr.J[m[0]],tr.J[m[1]],round(W[i]*100,1))
best=tr.cost()
for i in range(len(tr.M)):
    old=tr.M[i]; tr.M[i]=(old[0],old[1],'C')
    W=envelope(tr,deck,['Grain truck','Semi'])
    if W is not None and W.max()<=0.667: best=tr.cost(); print('cable ok at',i,'cost',round(best))
    else: tr.M[i]=old
W=envelope(tr,deck,['Pickup','School bus','Fire engine','Grain truck','Semi'])
print('final cost',round(tr.cost()),'max',round(W.max()*100,1), 'cables',sum(1 for m in tr.M if m[2]=='C'))

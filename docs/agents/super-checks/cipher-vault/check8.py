exec(open('check7.py').read().split("t=time.time(); s=survivors([P")[0])
for cl in [2,3,4,5]:
    c=crib[:cl]; ps=[i for i in range(len(L)-cl+1) if all(L[i+j]!=c[j] for j in range(cl))]
    s=survivors(ps[:12],c); print('crib',c,'at first 12 allowed positions: settings that fit',len(s))
# six rotor orders, full crib at true position
s=survivors([P.index(crib)],crib,orders=list(itertools.permutations(['I','II','III']))); print('6 orders x 17576, full crib:',s)

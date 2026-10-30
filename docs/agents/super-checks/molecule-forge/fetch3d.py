import json,urllib.request,time,math
P=json.load(open('pubchem.json'))
res={}
for n in P['book']:
    cid=P['data'][n]['CID']
    u=f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/SDF?record_type=3d"
    try:
        s=urllib.request.urlopen(u,timeout=20).read().decode()
        L=s.splitlines(); na,nb=int(L[3][:3]),int(L[3][3:6])
        at=[(L[4+i].split()[3],tuple(map(float,L[4+i].split()[:3]))) for i in range(na)]
        bd=[(int(L[4+na+j][:3])-1,int(L[4+na+j][3:6])-1,int(L[4+na+j][6:9])) for j in range(nb)]
        res[n]={'atoms':at,'bonds':bd}
    except Exception as e: res[n]={'err':str(e)[:60]}
    print(n, 'ok' if 'atoms' in res[n] else res[n]['err']); time.sleep(.25)
json.dump(res,open('pc3d.json','w'))

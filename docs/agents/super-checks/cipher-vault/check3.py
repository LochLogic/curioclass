from solver2 import *
import json,time
D=json.load(open('rooms.json')); R={int(k):v for k,v in D['R'].items()}
T=[R[3],R[4],
 'MY DOG WAITS BY THE DOOR EVERY DAY AFTER SCHOOL. WHEN THE BUS STOPS HE RUNS DOWN THE STREET AND JUMPS SO HIGH THAT HE ALMOST KNOCKS ME OVER. THEN WE WALK TO THE PARK AND HE CHASES EVERY BIRD HE SEES, BUT HE HAS NEVER CAUGHT ONE AND I DO NOT THINK HE EVER WILL. AT NIGHT HE SLEEPS AT THE END OF MY BED.',
 'MEET ME AT THE LIBRARY AFTER LUNCH ON FRIDAY. BRING THE MAP AND THE RED NOTEBOOK. WE NEED TO FINISH THE PROJECT BEFORE THE WEEKEND, SO DO NOT BE LATE. IF THE LIBRARY IS CLOSED, WAIT FOR ME UNDER THE BIG TREE BY THE GYM. I WILL BRING SNACKS FOR BOTH OF US AND A SPARE PENCIL IN CASE YOURS BREAKS AGAIN.',
 'THE STORM ROLLED IN FROM THE WEST JUST AS THE GAME BEGAN. FIRST CAME THE WIND, THEN A FEW HEAVY DROPS, AND THEN SO MUCH RAIN THAT NOBODY COULD SEE THE OTHER END OF THE FIELD. THE COACH CALLED EVERYONE INTO THE GYM, WHERE WE PLAYED CARDS AND WAITED FOR THE THUNDER TO PASS OVER THE HILLS.']
def prefix(t,n):
    c=0
    for i,ch in enumerate(t):
        if ch.isalpha(): c+=1
        if c==n: return t[:i+1]
    return t
res={}
t0=time.time()
for n in [25,40,60,80,100,120,150,200,250]:
    ok=0;tot=0;accs=[]
    for ti,t in enumerate(T):
        for s in range(2):
            p=prefix(t,n); key=list(A); random.Random(ti*10+s+n).shuffle(key); key=''.join(key)
            d=solve(sub(p,key),iters=2000,restarts=8,seed=s)
            a=sum(x==y for x,y in zip(letters(d),letters(p)))/len(letters(p)); accs.append(a)
            ok+=a>=0.9; tot+=1
    print(n,'letters: cracked',ok,'/',tot,'mean acc',round(sum(accs)/len(accs),2), round(time.time()-t0))

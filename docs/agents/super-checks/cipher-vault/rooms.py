from ciphers import *
rng=random.Random(1794)
FINAL='NOW GO STUMP YOUR PARTNER'
pad=''.join(rng.choice(A) for _ in range(len(letters(FINAL))))
pieces=[pad[0:5],pad[5:9],pad[9:13],pad[13:17],pad[17:21]]
print('PAD',pad,pieces)
R={}
R[1]=('THE DIE IS CAST. PAD '+pieces[0])
R[2]=('THE GRID IS THE KEY. PAD '+pieces[1])
R[3]=('WHEN A QUEEN WRITES IN SECRET SHE TRUSTS HER SYMBOLS, BUT EVERY SYMBOL STAYS THE SAME LETTER ALL THE WAY THROUGH. '
      'COPY THE LETTER AND COUNT THE SYMBOLS. IN ENGLISH THE MOST COMMON LETTER IS E, THEN T, A AND O. '
      'LOOK FOR SHORT WORDS NEXT: A ONE LETTER WORD IS A OR I, AND A COMMON THREE LETTER WORD IS THE. '
      'A CODEBREAKER NEEDS NO KEY WHEN THE MESSAGE IS LONG ENOUGH TO COUNT. PAD '+pieces[2])
R[4]=('FOR THREE HUNDRED YEARS PEOPLE CALLED THIS CIPHER UNBREAKABLE. THE SAME LETTER TURNS INTO DIFFERENT LETTERS, '
      'SO COUNTING SEEMS USELESS. BUT THE KEY REPEATS. WHEN THE SAME WORDS MEET THE SAME PART OF THE KEY, '
      'THE SAME LETTERS COME OUT AGAIN. MEASURE THE GAPS BETWEEN THE REPEATS AND THE LENGTH OF THE KEY APPEARS. PAD '+pieces[3])
R[5]=('KEEPER HERE. WEATHER REPORT: FOG AT DAWN, CLEAR BY NOON. PAD '+pieces[4])
for k,v in R.items(): print(k,len(letters(v)),'letters')
# Room 3 key alphabet (plain A..Z -> cipher symbols indexed 0..25); generate derangement
r3=list(A); random.Random(1586).shuffle(r3); r3=''.join(r3)
VKEY='RAVEN'; ESTART='BOX'
C={1:caesar(R[1],3),2:R[2],3:sub(R[3],r3),4:vig(R[4],VKEY),5:enigma(R[5],start=ESTART)}
for k in C: print('\nROOM',k,'\nPT:',R[k],'\nCT:',C[k])
print('R3 key plain->cipher:',r3)
# round trips
assert caesar(C[1],-3)==R[1]
assert unsub(C[3],r3)==R[3]
assert vig(C[4],VKEY,-1)==R[4]
assert enigma(C[5],start=ESTART)==R[5]
otp=''.join(A[(A.index(p)+A.index(k))%26] for p,k in zip(letters(FINAL),pad))
print('\nFINAL PT',letters(FINAL),'\nPAD',pad,'\nCT',otp)
assert ''.join(A[(A.index(c)-A.index(k))%26] for c,k in zip(otp,pad))==letters(FINAL)
print('round trips OK')
import json; json.dump(dict(R=R,C=C,r3=r3,pad=pad,otp=otp),open('rooms.json','w'))

from ciphers import *
import json
D=json.load(open('rooms.json')); pad=D['pad']; otp=D['otp']
def keyfor(ct,pt): return ''.join(A[(A.index(c)-A.index(p))%26] for c,p in zip(ct,letters(pt)))
for alt in ['NOW GO STUMP YOUR PARTNER','TURN BACK THE VAULT IS EMPTY','LUNCH IS PIZZA ON FRIDAY TOO','THE CAT SLEEPS ON MY BOOKS']:
    a=letters(alt); print(alt,len(a))
    if len(a)==21: k=keyfor(otp,alt); print('  key that gives it:',k, ' check', ''.join(A[(A.index(c)-A.index(x))%26] for c,x in zip(otp,k)))
# combos
p='MEET ME AT THE OLD BRIDGE'
print('caesar 3 then 5 == caesar 8:',caesar(caesar(p,3),5)==caesar(p,8))
print('rot13 twice is identity:',caesar(caesar(p,13),13)==p.upper())
print('vigenere key K == caesar 10:',vig(p,'K')==caesar(p,10))
print('vigenere ABAB == AB:',vig(p,'ABAB')==vig(p,'AB'))
print('vigenere twice RAVEN+CAT equals key length lcm 15:', vig(vig(p,'RAVEN'),'CAT')==vig(p,''.join(A[(A.index('RAVEN'[i%5])+A.index('CAT'[i%3]))%26] for i in range(15))))
print('caesar of English keeps counter shape (sorted counts same):',sorted(collections.Counter(letters(p)).values())==sorted(collections.Counter(letters(caesar(p,7))).values()))
# Enigma: same letter typed 10x gives different letters, never A
print('enigma AAAAA... at BOX:',enigma('A'*26,start='BOX'))
# key AAAAA
print('vigenere key A changes nothing:',vig(p,'AAA')==p)
# Lipogram: text without E: rank mapping fails at E
lip='A MAN WALKS INTO A SHOP TO BUY A HAT FOR HIS SON. HIS SON IS SIX AND LIKES TO PLAY OUTSIDE ALL DAY LONG IN THE SUN'
lip='A MAN WALKS INTO A SHOP TO BUY A HAT FOR HIS SON. HIS SON IS SIX AND LIKES TO PLAY OUT IN THE SUN'
print('lipogram check E count',letters(lip).count('E'))

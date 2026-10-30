from ciphers import *
assert enigma('AAAAA')=='BDZGO', enigma('AAAAA')
# double step check: start ADU -> positions after 3 keys: ADV, AEW, BFX
print('enigma test vector AAAAA->',enigma('AAAAA'))
print('double step sample', enigma('AAA',start='ADU'))

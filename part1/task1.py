import autokey
import quadgram
import decipher
import numpy as np

# input ciphertext
fhand=open('task1_ct.txt')
s=fhand.read()
s=autokey.del_sp(s)

key='AAAAAA'
for i in range(0,6):
    count=decipher.f(s,key,i)

    # sort
    


    key=max[0]
    print(max)

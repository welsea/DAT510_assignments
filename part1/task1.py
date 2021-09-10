import autokey
import quadgram
import decipher
import numpy as np

# input ciphertext
fhand=open('testct.txt')
s=fhand.read()
s=autokey.del_sp(s)

s=s[:20]

key='AAAA'

decipher.f(s,key)
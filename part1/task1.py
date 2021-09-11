import autokey
import decipher

# input ciphertext
fhand=open('task1_ct.txt')
s=fhand.read()
s=autokey.del_sp(s)

ss=decipher.f(s[:12])
print(ss)

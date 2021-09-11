import autokey
import decipher

# input ciphertext
fhand=open('task1_ct.txt')
s=fhand.read()
s=autokey.del_sp(s)

result=decipher.f(s)
for i in range(0,len(result)):
    print(result[i])

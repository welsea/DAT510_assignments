import autokey
import decipher
import time

# input ciphertext
fname1='task1_ct_shorter.txt'
print("Decrypt task1_ct.txt")

fhand=open('task1_ct.txt')
s=fhand.read()
s=autokey.del_sp(s)

print("The ciphertext is:",s)
# print out the keyword, number of quadgrams and plaintext
start=time.time()
result=decipher.f(s)
end=time.time()
print('The keyword is:',result[0])
print('The plaintext is:',result[2])
print('time:',(end-start)/3600)


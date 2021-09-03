# part1-task1:polyalphabetic substitution cipher
# kasiski attack

from sys import argv
import re
# import math
import kasiski
import divide


# delete space
def del_sp(ct):
    ct=re.sub(r'[^A-Z]+','',ct)
    return ct

## turn letter into number
def turn2num(ct):
    num=[]
    for i in range(0,len(ct)):
        x=ord(ct[i])-65
        num.append(x)
    return num
    


# input ciphertext
fhand=open('task1_ct.txt')
s=fhand.read()
s=del_sp(s)

# kasiski attach
# print('Four letters:')
# kasiski.kasiski(s,4)

num=turn2num(s)
print(num[2])

# # divide ct into group
# group=divide.d(s,7)
# for i in range(0,len(group)):
#     print(group[i])

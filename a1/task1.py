# part1-task1:polyalphabetic substitution cipher
import re

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

# turn number in to letter:
def turn2char(s):
    char=[]     
    for i in range(0,len(s)):
        if s[i] > 25:
            s[i]=s[i]-25
        char.append(chr(s[i]+65))
    return char

# match
def match(ct,key):
    ll=[]
    ml=[]
    start=0
    for r in [ct[i:i + 3] for i in range(start, len(ct), 3)]:
        ll.append(r)
    for i in range(0,len(ll)):
        for k in range(0,3):
            ml[i][k]=ll[i][k]+key[k]
    return ml
    
        

# input ciphertext
fhand=open('task1_ct.txt')
s=fhand.read()
s=del_sp(s)

num=turn2num(s)
the=turn2num('THE')

# ll=match(num,the)
# print(ll[1])
# x=[0,0,0]
# print(turn2char(x))
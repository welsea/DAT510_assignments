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

# turn number into letter:
def turn2char(s):
    char=[]     
    for i in range(0,len(s)):
        if s[i] > 25:
            s[i]=s[i]-25
        char.append(chr(s[i]+65))
    return char

        




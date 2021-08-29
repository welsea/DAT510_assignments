# part1-task1:polyalphabetic substitution cipher
# kasiski attack

from sys import argv
import re
# import math


# delete space
def del_sp(ct):
    ct=re.sub(r'[^A-Z]+','',ct)
    return ct

# count the time that words appearance 
def word_count(ct,n):
    word=''
    count=''
    group={}

    for i in range(0,len(ct)-1):
        word=ct[i:i+n]
        count=len(re.findall(word,ct))
        if count>=3:
            group[word]=count

    return group

def find_location(g,ct):
    location={}
    keys=list(g.keys())
    for i in range(0,len(keys)):
        word=keys[i]
        it=re.finditer(word,ct)
        index=[]
        for t in it:
            index.append(t.start())
        location[word]=index
        i+=1
    return location

# kasiski attack
def kasiski(ct,num):
    ct=del_sp(ct)
    group=word_count(ct,num)
    location=find_location(group,ct)


    print("word    count    location")
    for i in group:
        print(i,end='     ')
        print(group[i],end='         ')
        print(','.join(str(x) for x in location[i]))


    

# input ciphertext
fhand=open('task1_ct.txt')
s=fhand.read()
print('two letters:')
kasiski(s,2)
print('three letters:')
kasiski(s,3)
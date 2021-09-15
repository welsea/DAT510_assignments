
import autokey

fhand=open('testct2.txt')
s=fhand.read()
s=autokey.del_sp(s)
ct=autokey.turn2num(s)
key='DAT'
key=autokey.turn2num(key)
pt=[]
addkey=key.copy()
for j in range(0,2):
    pt=[]
    addkey=key.copy()
    for i in range(0,len(ct)):
        if ct[i]<addkey[i]:
            ptt=ct[i]+26-addkey[i]
        else:
            ptt=ct[i]-addkey[i]
        addkey.append(ptt)
        pt.append(ptt)
    ct=pt.copy()

# p=''.join(autokey.turn2char(pt))
# print(p)

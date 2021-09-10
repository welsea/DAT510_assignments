import autokey

fhand=open('testpt.txt')
s=fhand.read()
s=autokey.del_sp(s)
ct=autokey.turn2num(s)
key='DATF'
key=autokey.turn2num(key)
key=key+ct[:len(ct)-len(key)]
pt=[]
for i in range(0,len(ct)):
    ptt=ct[i] + key[i]
    if ptt > 25:
        pt.append(ptt-26)
    else:
        pt.append(ptt)
pt=autokey.turn2char(pt)
pt=''.join(pt)
f = open("testct.txt", "a")
f.write(pt)
f.close()

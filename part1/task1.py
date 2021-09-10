import autokey
import quadgram
import match

# input ciphertext
fhand=open('task1_ct.txt')
s=fhand.read()
s=autokey.del_sp(s)

quad=quadgram.quad()

# turn quadgram into number
quadgramNum=[]
for i in range(0,len(quad)):
    quadgramNum.append(autokey.turn2num(quad[i]))


max=match.f(s[:10])
print(max)

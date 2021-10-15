import autokey
import quadgram

quad=quadgram.quad()

# divide ct/pt into quadgram
def genQuad(t):
    quadPt=set()
    for i in range(0,len(t)):
        if i+3 < len(t):
            x=t[i:i+4]
            x=''.join(autokey.turn2char(x))
            quadPt.add(x)
    return quadPt

def match(pt):
    num=0
    ptQuad=genQuad(pt)
    # print('len ptquad:',len(ptQuad))
    x=ptQuad.intersection(quad)
    num=len(x)
    return num

def genPossiblePt(key,ct):
    pt=[]
    addKey=key.copy()
    for i in range(0,len(ct)):
        if ct[i]<addKey[i]:
            ptt=ct[i]+26-addKey[i]
        else:
            ptt=ct[i]-addKey[i]
        pt.append(ptt)
        addKey.append(ptt)
    return pt


def f(ct):
    ct=s[:30]
    ct=autokey.turn2num(ct)

    result=['key',0,'plaintext1',"plaintext2"]
    # generate plaintext
    childKey=[]
    for i in range(0,26):
        for j in range(0,26):
            for k in range(0,26):
                for l in range(0,26):
                    for z in range(0,26):
                        for d in range(0,26):
                            ct2=[]
                            ct2.append(ct)
                            # making the plaintext of fist round to the ciphertex of second reound
                            for x in range(0,2):                   
                                childKey=[i,j,k,l,z,d]
                                pt=genPossiblePt(childKey,ct2[x])
                                ct2.append(pt)
                            
                            # plaintext match to quadgram
                            num=match(pt)
                            if num>result[1]:
                                pt=''.join(autokey.turn2char(pt))
                                key=''.join(autokey.turn2char(childKey))
                                result[0]=key
                                result[1]=num
                                result[2]=''.join(autokey.turn2char(ct2[1]))
                                result[3]=pt

    p=genPossiblePt(autokey.turn2num(s),result[3])
    result[2]=''.join(autokey.turn2char(p))

    return result


fhand=open('task3_ct.txt')
s=fhand.read()
result=f(s)
print("The first round plaintext: \n",result[2])
print("The second round plaintext: \n",result[3])


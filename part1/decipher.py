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
    ct=autokey.turn2num(ct)

    result=['key',0,'plaintext']
    # generate plaintext
    childKey=[]
    for i in range(0,26):
        for j in range(0,26):
            for k in range(0,26):
                for l in range(0,26):
                    for z in range(0,26):
                        for d in range(0,26):
                            # print([i,j,k,l,z,d])
                            childKey=[i,j,k,l,z,d]
                            key=''.join(autokey.turn2char(childKey))

                            pt=genPossiblePt(childKey,ct)

                            # plaintext match to quadgram
                            num=match(pt)
                            if num>result[1]:
                                pt=''.join(autokey.turn2char(pt))
                                key=''.join(autokey.turn2char(childKey))
                                result[0]=key
                                result[1]=num
                                print(num)
                                result[2]=pt

    
    return result
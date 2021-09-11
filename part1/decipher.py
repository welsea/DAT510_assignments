import autokey
import quadgram

quad=quadgram.quad()

def genChildKey():
    all=[]
    for i in range(0,26):
        for j in range(0,26):
            for k in range(0,26):
                for l in range(0,26):
                    for z in range(0,26):
                        for d in range(0,26):
                            # print([i,j,k,l,z,d])
                            all.append([i,j,k,l,z,d])
    return all

# divide ct/pt into quadgram
def genQuad(t):
    quadPt=set()
    for i in range(0,len(t)):
        if i+3 < len(t):
            quadPt.add(t[i:i+4])
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
    addKey=key
    for i in range(0,len(ct)):
        if i < len(key):
            if ct[i]<key[i]:
                ptt=ct[i]+26-key[i]
            else:
                ptt=ct[i]-key[i]
            addKey.append(ptt)
            pt.append(ptt)
        else:
            if ct[i]<addKey[i]:
                ptt=ct[i]+26-key[i]
            else:
                ptt=ct[i]-key[i]
            pt.append(ptt)
            addKey.append(ptt)
    return pt


def f(ct):
    ct=autokey.turn2num(ct)

    # generate all keys
    childKey=genChildKey()

    all={}
    # generate plaintext
    for i in range(0,len(childKey)):
        pt=genPossiblePt(childKey[i],ct)
        pt=''.join(autokey.turn2char(pt))
        key=''.join(autokey.turn2char(childKey[i]))
        all[key]=pt

    # match quadgram and count
    allPt=list(all.values())
    allKey=list(all.keys())

    count={}
    for i in range(0,len(allKey)):
        key=allKey[i]
        num=match(all[key])
        count[key]=num
        # snum='num:  '+str(num)
        # print(skey)
        print(num)
    

    # max
    countNum=list(count.values())
    countKeys=list(count.keys())
    m=max(countNum)
    maxIndex=countNum.index(m)
    maxKey=countKeys[maxIndex]
    maxPt=all[maxKey]

    ss='key:'+maxKey+'  num:'+str(m)+'\n'+maxPt
    return ss
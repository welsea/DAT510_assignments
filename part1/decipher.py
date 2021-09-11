import autokey
import quadgram

quad=quadgram.quad()

def genChildKey():
    all=[]
    # for i in range(0,length):
    #     for j in range(0,26):
    #         child[i]=j
    #         all.append(child)

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
    # for i in range(0,len(ptQuad)):
    #     if ptQuad[i] in quad:
    #         num+=1
    #         # print(ptQuad[i],'----',quad.index(ptQuad[i]))
    #     else:
    #         num+=0
    # print(num)
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


def f(ct,length):
    ct=autokey.turn2num(ct)

    # generate all keys
    childKey=genChildKey(length)

    all={}
    # generate plaintext
    for i in range(0,len(childKey)):
        pt=genPossiblePt(childKey[i],ct)
        pt=''.join(autokey.turn2char(pt))
        key=''.join(autokey.turn2char(childKey[i]))
        all[key]=pt
        print('key---------------------------------------',key)
        print('plaintext--===============================',pt)

    # match quadgram and count
    allPt=list(all.values())
    allKey=list(all.keys())
    # fa=open('textct.txt','a')
    count={}
    for i in range(0,len(allKey)):
        key=allKey[i]
        num=match(all[key])
        count[key]=num

        # write in textct.txt
        # skey='key:  '+key
        snum='num:  '+str(num)
        # print(skey)
        print(snum)
        # s=skey+'\n'+snum+'\n'
        # fa.write(s)
    

    # max
    countNum=list(count.values())
    countKeys=list(count.keys())
    m=max(countNum)
    maxIndex=countNum.index(m)
    maxKey=countKeys[maxIndex]
    maxPt=all[maxKey]

    ss='key:'+maxKey+'  num:'+str(m)+'\n'+maxPt
    return ss
    # fa.write(ss)
    # fa.close()


# pt='CRYPTOGRAPHYCANBESTRONGORWEAKCRYPTOGRAPHICSTRENG'
# match(pt)

# fhand=open('testct.txt')
# s=fhand.read()
# s=autokey.del_sp(s)

# ss=f(s,6)
# print(ss)

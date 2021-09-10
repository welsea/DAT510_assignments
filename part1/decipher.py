import autokey
import quadgram


def genChildKey(parentKey):
    child=parentKey
    childKey=[]
    for i in range(0,26):
        child[0]=i
        for j in range(0,26):
            child[1]=j
            for k in range(0,26):
                child[2]=k
                for l in range(0,26):
                    child[3]=l
                    childKey.append(child)
    return childKey





# divide ct/pt into quadgram
def genQuad(t):
    quadPt=[]
    for i in range(0,len(t)):
        if i+3 < len(t):
            quadPt.append(t[i:i+4])
    return quadPt


def match(pt):
    quad=quadgram.quad()
    num=0
    ptQuad=genQuad(pt)
    for i in range(0,len(ptQuad)):
        if ptQuad[i] in quad:
            num+=1
        else:
            num+=0
    return num

def genPossiblePt(key,ct):
    pt=[]
    addKey=key
    for i in range(0,len(ct)):
        if i < len(key):
            for j in range(0,len(key)):
                if ct[j]<key[j]:
                    ptt=ct[j]+26-key[j]
                    
                else:
                    ptt=ct[j]-key[j]
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


def f(ct,parentKey):
    ct=autokey.turn2num(ct)
    # print('ciphertext------',ct)
    #define first parent key
    firstParent=parentKey
    firstParent=autokey.turn2num(firstParent)

    childKey=genChildKey(firstParent)

    all={}
    # generate plaintext
    for i in range(0,len(childKey)):
        pt=genPossiblePt(childKey[i],ct)
        pt=''.join(autokey.turn2char(pt))
        all[''.join(autokey.turn2char(childKey[i]))]=pt

    # match quadgram and count
    allPt=list(all.values())
    allKey=list(all.keys())
    count={}
    for i in range(0,len(allKey)):
        key=allKey[i]
        num=match(all[key])
        count[key]=num


    # for i in range(0,len(childKey)):
    #     child=childKey[i]
    #     for j in range(0,len(ct)):
    #         for k in range(0,len(child)):
    #                 # print('key--------------------',child)
    #                 ptSameChild=[]
    #                 for j in range(0,len(ct)-len(child)+1):
    #                     pt=[]
    #                     for k in range(0,len(child)):
    #                         if ct[j+k] < child[k]:
    #                             pt.append(ct[j+k]+26 - child[k])
    #                         else:
    #                             pt.append(ct[j+k] - child[k])
    #                     ptSameChild.append(pt)
    #                     # print(i,'---------',''.join(autokey.turn2char(pt)))
    #                 result[''.join(autokey.turn2char(child))]=ptSameChild                

    # # count
    # f = open("textct.txt", "a")

    # count={}
    # resultNum=list(result.values())
    # resultKeys=list(result.keys())

    # f.write(resultKeys)
    
    # num=0
    # for i in range(0,len(resultNum)):
    #     childkey=[]
    #     key=resultKeys[i]
    #     for k in range(0,len(result[key])):
            
    #         for j in range(0,len(result[key])):
    #             #into quadgram:
    #             if j+4 > len(result[key][k]):
    #                 break
    #             else:
    #                 # s=''.join(autokey.turn2char(result[key][k][j:j+4]))+'\n'
    #                 # f.write(s)
    #                 num+=match(result[key][k][j:j+4],quad)
    #                 # print('len num                  ',num)
            
    #         childkey.append(num)
    #         num=0
    #     # print('key              ',key)
    #     # print('match num                ',sum(childkey))
        
    #     # ss=key+'-----'+str(sum(childkey))+'\n'
    #     # f.write(ss)
        
    #     count[key]=sum(childkey)
    # f.close()              


print('test gen quad')
print(genQuad('ABCDEF'))
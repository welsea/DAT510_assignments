import autokey
import quadgram


def match(pt,quad):
    num=0
    # pt turn to letter
    pt=''.join(autokey.turn2char(pt))
    if pt in quad:
        num=1
    else:
        num=0
        
    return num


def f(ct,parentKey,x):
    ct=autokey.turn2num(ct)
    # print('ciphertext------',ct)
    #define first parent key
    firstParent=parentKey
    firstParent=autokey.turn2num(firstParent)

    result=[]
    child=firstParent

    quad=quadgram.quad()
    # quadNum=[]

    # for i in range(len(quad)):
    #     quadNum.append(autokey.turn2num(quad[i]))


    result={}
    for i in range(0,26):
        # print('key--------------------',child)
        ptSameChild=[]
        for j in range(0,len(ct)-len(child)+1):
            pt=[]
            for k in range(0,len(child)):
                if ct[j+k] < child[k]:
                    pt.append(ct[j+k]+26 - child[k])
                else:
                    pt.append(ct[j+k] - child[k])
            ptSameChild.append(pt)
            # print(i,'---------',''.join(autokey.turn2char(pt)))
        result[''.join(autokey.turn2char(child))]=ptSameChild
        # move to next key
        child[x]+=1

    #match
    count=[]
    rKeys=list(result.keys())
    for i in range(0,26):
        childkey=[]
        key=rKeys[i]
        for k in range(0,len(result[key])):
            num=[]
            for j in range(0,len(result[key])):
                #into quadgram:
                if j+4 > len(result[key][k]):
                    break
                else:
                    num.append(match(result[key][k][j:j+4],quad))
            childkey.append(sum(num))
        print('key-------------------------------',key)
        print('match num-------------------------',sum(childkey))
        count.append([key,childkey])

    return count
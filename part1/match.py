import autokey
import quadgram


def match(result,quad):
    count=0
    print('match: result------',result)
    for i in range(len(result)):
        for j in range(len(result[i])):
            for x in range(len(quad)):
                print(quad[x],'--------',result[i])
                if quad[x]==result[i][j]:
                    count+=1 
    return count

def f(ct):
    ct=autokey.turn2num(ct)
    # print('ciphertext------',ct)
    #define first parent key
    firstParent='DATFAA'
    firstParent=autokey.turn2num(firstParent)

    result=[]
    child=firstParent

    quad=quadgram.quad()
    quadNum=[]

    for i in range(len(quad)):
        quadNum.append(autokey.turn2num(quad[i]))


    result=[]
    for i in range(0,26):
        ptSameChild=[]
        for j in range(0,len(ct)-len(child)):
            pt=[]
            for k in range(0,len(child)):
                if ct[j+k] < child[k]:
                    pt.append(ct[j+k]+26 - child[k])
                else:
                    pt.append(ct[j+k] - child[k])
            ptSameChild.append(pt)
        result.append(ptSameChild)
        # move to next key
        child[4]+=1



    for i in range(0,26):
        pt=[]
        print('child key------------',child)
        for j in range(0,len(ct)-7):
            ptt=[]
            for k in range(0,len(child)):
                # try:
                if j+k < len(ct):
                    if ct[j+k] < child[k]:
                        ptt.append((ct[j+k]+26)-child[k])
                        # print((ct[j+k]+26)-child[k],end=' ')
                    else:
                        ptt.append(ct[j+k]-child[k])
                        # print(ct[j+k]-child[k],end=' ')
                print('ciphertext----------',ct[j+k:])    
                    
            print()
                # except IndexError:
                #     print('j+k:',j+k)
                #     print(ct[7])
                #     exit()
            # pt.append(ptt)
            print('plaintext------------',ptt)
            pt.append(ptt)
        child[4]=firstParent[0]+1
        # print('!!!pt---------',pt)
    result.append(pt)
    print(result[0])


    # result_char=[]
    # # # count=[]
    match
        

    # for i in range(0,len(result)):
    #     # count_c=[]
    #     result_quad=[]
    #     print('result[]-----------',result[i])

    #     for k in range(len(result[i])):
    #     # turn result into quadgram
    #         if j+4 > len(result[i]):
    #             break
    #         else:
    #             result_quad.append(result[i][j:j+4])
    #             print('quad-----------',result[i][j:j+4])
    #             # result_char.append(''.join(autokey.turn2char(result[i][j:j+4])))
    #     count.append(match(result_quad,quadNum))
        # count.append(sum(count))
    # return max(count)
import permutation
import fK
import genKeys

def f(t,raw_key,type,triple=False):
    orderIP=[2,6,3,1,4,8,5,7]
    orderIP_1=[4,1,3,5,7,2,8,6]  

    keys=genKeys.gen2keys(raw_key)

    if type==1:
        key1=keys['key1']
        key2=keys['key2']
    else:
        key2=keys['key1']
        key1=keys['key2']

    ip=permutation.p(t,orderIP)
    left=ip[0:4]
    right=ip[4:]

    fk1=fK.f(left,right,key1)
    sw=fk1[1]+fk1[0]

    re=fK.f(sw[:4],sw[4:],key2)
    fk2=re[0]+re[1]

    result=permutation.p(fk2,orderIP_1)

    return result
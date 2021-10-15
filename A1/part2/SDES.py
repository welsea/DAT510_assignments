import permutation
import fK


# use raw key to generate subkeys
def leftShift(l,n):
    for i in range(0,n):
        x=l.pop(0)
        l.insert(4,x)
    return l


# divide the binary string in two part
def divide(key,n):
    left_l=key[0:5]
    right_l=key[5:]
    # left shift
    left=leftShift(left_l,n)
    right=leftShift(right_l,n)
    p8=left+right
    return p8


# generate two keys
def gen2keys(key):
    keys={}
    order=[3,5,2,7,4,10,1,9,8,6]
    p10=permutation.p(key,order)

    order2=[6,3,7,4,8,5,10,9]

    p8_1=divide(p10,1)
    key1=permutation.p(p8_1,order2)
    
    p8_2=divide(p8_1,2)
    key2=permutation.p(p8_2,order2)

    keys['key1']=key1
    keys['key2']=key2

    return keys    


# SDES
def f(t,raw_key,type):
    orderIP=[2,6,3,1,4,8,5,7]
    orderIP_1=[4,1,3,5,7,2,8,6]  

    keys=gen2keys(raw_key)

    # type=1:encrypt
    # type=0:decrypt
    if type==1:
        key1=keys['key1']
        key2=keys['key2']
    else:
        key2=keys['key1']
        key1=keys['key2']
    # IP
    ip=permutation.p(t,orderIP)
    left=ip[0:4]
    right=ip[4:]

    #fK
    fk1=fK.f(left,right,key1)
    sw=fk1[1]+fk1[0]

    re=fK.f(sw[:4],sw[4:],key2)
    fk2=re[0]+re[1]

    # IP-1
    result=permutation.p(fk2,orderIP_1)

    return result
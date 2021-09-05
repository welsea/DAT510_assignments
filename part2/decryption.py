import permutation
import fK

def decrypt(ct,keys):
    orderIP=[2,6,3,1,4,8,5,7]
    orderIP_1=[4,1,3,5,7,2,8,6]
    ip=permutation.p(ct,orderIP)
    left=ip[0:4]
    right=ip[4:]
    fk1=fK.f(left,right,keys['key2'])
    sw=fk1[1]+fk1[0]
    re=fK.f(sw[:4],sw[4:],keys['key1'])
    fk2=re[0]+re[1]
    pt=permutation.p(fk2,orderIP_1)

    print('pt:',pt)
    
    return pt
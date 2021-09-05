import permutation

# def permutation(key,n):
#     p_key=[]
#     order=[]
#     if n == 10:
#         #p10
#         order=[3,5,2,7,4,10,1,9,8,6]
#     else:
#         #p8
#         order=[6,3,7,4,8,5,10,9]
#     for i in range(0,len(order)):
#         p_key.append(key[order[i]-1])
#     return p_key


def leftShift(l,n):
    for i in range(0,n):
        x=l.pop(0)
        l.insert(4,x)
        i=+1
    return l


def divide(key,n):
    left_l=key[0:5]
    right_l=key[5:]
    # left shift
    left=leftShift(left_l,n)
    right=leftShift(right_l,n)
    # print('left ',left)
    # print('right ',right)
    p8=left+right
    return p8



def gen2keys(key):
    keys={}
    order=[3,5,2,7,4,10,1,9,8,6]
    p10=permutation.p(key,order)
    # print(p10)

    order2=[6,3,7,4,8,5,10,9]
    p8_1=divide(p10,1)
    key1=permutation.p(p8_1,order2)
    
    p8_2=divide(p8_1,2)
    key2=permutation.p(p8_2,order2)

    keys['key1']=key1
    keys['key2']=key2

    # print('key1 ',key1)
    # print('key2 ',key2)

    return keys    
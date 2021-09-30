import permutation
def cal(t1,t2):
    t=[]
    for i in range(0,len(t1)):
        x=int(t1[i],2) ^ int(t2[i],2)
        t.append(str(x))
    # print('t: ',t)
    return t

def locate(l,s):
    p1_row=int(l[0]+l[3],2)
    p1_col=int(l[1]+l[2],2)
    p1=s[p1_row][p1_col]
    return p1

def f(left,right,key):
    result=[]
    s0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    s1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

    ep=permutation.p(right,[4,1,2,3])+permutation.p(right,[2,3,4,1])
    t=cal(ep,key)

    p1=locate(t[:4],s0)
    p2=locate(t[4:],s1)
    sp1=list(bin(p1))[2:]
    sp2=list(bin(p2))[2:]
    add='0'
    while len(sp1)<2:
        sp1.insert(0,add)
    while len(sp2)<2:
        sp2.insert(0,add)
        
    p1p2=sp1+sp2

    p4=permutation.p(p1p2,[2,4,3,1])
    result.append(cal(p4,left))
    result.append(right)
    return result
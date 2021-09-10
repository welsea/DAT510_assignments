
def d(ct,n):
    ll=[]
    g_num=0
    # if len(ct)%n != 0:
    #     g_num=len(ct)//n +1
    # for i in range(0,g_num):
    #     l=[]
    #     for j in range(0,len(ct)-1):
    #         l.append(ct[j])
    #         j+=n
    #     group[i]=l

    # for i in range(0,len(ct),n):
    #     for 

    for r in [ct[i:i + n] for i in range(0, len(ct), n)]:
        ll.append(r)

    return ll
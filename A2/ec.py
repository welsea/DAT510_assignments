import ecc
import random
import tinyec


def DHexchange(n,cy):
    #alic choose a private key
    print("Alice choose a private key.")
    pA=int(input())
    # pA=random.randint(0,n)
    #bob choose a private key
    print("Bob choose a private key.")
    pB=int(input())
    # pB=random.randint(0,n)

    print(pA,pB)
    #calculate the public key
    pbA=cy[pA-1][0]
    pbB=cy[pB-1][0]
    print("Alice\'s public key:",pbA)
    print("Bob\'s public key:",pbB)

    #calculate the K
    if pA*pB > n:
        k=cy[(pA*pB)%n-1][0]
    else:
        k=cy[pA*pB-1][0]
    print(k)



# ## get p,a,b,G,n and cyclic group
# a=int(input("Enter the a for Elliptic Curve (default:2) :") or "2")
# b=int(input("Enter the b for Elliptic Curve (default:2) :") or "2")
# p=int(input("Enter the p (default:17) :") or "17")

# print("E(x,y): y^2=x^3+%dx+%d(mod %d)" % (a,b,p))

# gl=list()
# gs=str(input("Enter the G(generator) (default:5,1) :" ) or "5,1")
# gl=list(gs.split(','))
# gl[0]=int(gl[0])
# gl[1]=int(gl[1])

# print(gl)

# g=tuple(gl)

# calculate cyclic group
# cy=ecc.f(a,p,g)
g=(2,2)
cy=ecc.f(0,211,g)
n=len(cy)
print("Clyclic group:")
for i in range(0,len(cy)):
    print(i+1,":",cy[i])
# the number of sub-sequence of cyclic group
print("n=",n)

# key exchange:
# DHexchange(n,cy)

#CSPRNG

#encrypt

#decrypt




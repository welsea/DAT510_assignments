import DH
import CSPRNG

# c=curve()
c=(0,-4,211,(2,2))
print("Curve: y^2 = x^3 + %dx + %d (mod %d)" % (c[0],c[1],c[2]))
print("Generator:",c[3])
cy=DH.CyclicGroup(c[0],c[2],c[3])
# print("Clyclic group:")
# for i in range(0,len(cy)):
#     print(i+1,":",cy[i])

n=len(cy)
# the number of sub-sequence of cyclic group
print("n=",n)
DH.exchange(n,cy)

#CSPRNG

#encrypt

#decrypt




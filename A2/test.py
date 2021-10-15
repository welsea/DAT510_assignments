from tinyec.ec import SubGroup, Curve
import ecc

field = SubGroup(p=211, g=(2, 2), n=241, h=1)
curve = Curve(a=0, b=-4, field=field, name='p1707')
print('curve:', curve)

# for k in range(0, 242):
#     p = k * curve.g
#     print(f"{k} * G = ({p.x}, {p.y})")

print("ecc:")
cy=ecc.f(2,17,(5,1))
print("Clyclic group:")
for i in range(0,len(cy)):
    print(i+1,":",cy[i])

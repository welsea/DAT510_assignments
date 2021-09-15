import autokey
import de2round

fhand=open('testct2.txt')
s=fhand.read()
s=autokey.del_sp(s)



result=de2round.f(s)
# for j in range(0,len(result)):
#     print(result[i])
print(result[2])


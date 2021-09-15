# import decipher
import de2
import time

start_time = time.time()
# keyword length four
fhand=open('testct.txt')
s=fhand.read()

# result=decipher.f(s)
result=de2.f(s)
for i in range(0,len(result)):
    print(result[i])

end_time = time.time()

print('time:',end_time-start_time)
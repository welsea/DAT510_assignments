import SDES
import tripleSDES

# crack SDES
def de1(ct):
    for i in range(0,1024):
        pt=''
        key='{0:010b}'.format(i)

        for j in range(0,len(ct)):
            result=SDES.f(ct[j],key,0)
            result=''.join(result) 
            result=int(result,2)
            #A:65 to Z:90, a:97 to z:122
            if 65<=result<=90 or 97<=result<=122:
                result=chr(result)
                pt+=result
            else:
                continue
        if len(pt)==len(ct):
            result=[key,pt]
            return result

# crack triple SDES
def de3(ct):
    for i in range(0,1024):
        for j in range(0,1024):
            pt=''
            key1='{0:010b}'.format(i)
            key2='{0:010b}'.format(j)
            for k in range(0,len(ct)):
                result=tripleSDES.f(ct[k],key1,key2,0)
                result=''.join(result) 
                result=int(result,2)
                if 65<=result<=90 or 97<=result<=122:
                    result=chr(result)
                    pt+=result
                else:
                    continue
            if len(pt)==len(ct):
                result=[key1,key2,pt]
                return result

# task3-1
file = open('ctx1.txt', 'r')
text = file.read()  
ct=[]
# divided ciphertext in groups of 8 bit
for i in range(0,len(text),8):
    ct.append(text[i:i+8])
result=de1(ct)
# print out result, result[0]:raw key, reasult[1]:plaintext
for i in range(0,2):
    print(result[i])


# task3-2
file = open('ctx2.txt', 'r')
text = file.read()  
ct=[]
for i in range(0,len(text),8):
    ct.append(text[i:i+8])
result=de3(ct)
# print out result, result[0]:raw key 1,  result[1]:raw key 2, reasult[2]:plaintext
for i in range(0,3):
    print(result[i])


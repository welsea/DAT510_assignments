import SDES
import re

def de(ct):
    file=open('task3.txt','a')
    for i in range(0,1024):
        pt=[]
        key='{0:010b}'.format(i)
        # key=key.zfill(10)
        # key.append(key)
        # print('key:',key)
        for j in range(0,len(ct)):
            result=SDES.f(ct[j],key,0)
            result=''.join(result)
            result=chr(int(result,2))
            pt.append(result)
        ptt=''.join(pt)
        ptt=re.sub(r'[^A-Z]+','',ptt)
        if len(ptt)>5:
            s=key+'[['+str(i)+']]'+ptt+'\n'
            file.write(s)
        # if i>2:
        #     break
    file.close()
        
file = open('ctx1.txt', 'r')
text = file.read()  
ct=[]
for i in range(0,len(text),8):
    ct.append(text[i:i+8])
de(ct)
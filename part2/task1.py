import genKeys
import algoSDES

#task 1
table=[]

# row1 to row4: encrypt
raw_key=['0000000000','0000011111','0010011111','0010011111']
pt=['00000000','11111111','11111100','10100101']
for i in range(0,len(raw_key)):
    tt=[]
    tt.append(raw_key[i])
    tt.append(pt[i])
    re=algoSDES.f(tt[1],genKeys.gen2keys(tt[0]),1)
    tt.append(''.join(re))
    table.append(tt)

# row5 to row8: decrypt
raw_key2=['1111111111','0000011111','1000101110','1000101110']
ct=['00001111','01000011','00011100','11000010']
for i in range(0,len(raw_key2)):
    tt=[]
    tt.append(raw_key2[i])
    tt.append(ct[i])
    re=algoSDES.f(tt[1],genKeys.gen2keys(tt[0]),0)
    tt.insert(1,''.join(re))
    table.append(tt)



print('raw key          plaintext        ciphertext')
print('-------------------------------------------')
for i in table:
    for j in i:
        print(j,end='        ')
    print()   



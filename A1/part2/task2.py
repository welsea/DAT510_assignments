import tripleSDES

table=[]

#row1 to row4: encrypt
raw_key1=['1000101110','1000101110','1111111111','0000000000']
raw_key2=['0110101110','0110101110','1111111111','0000000000']
pt=['11010111','10101010','00000000','01010010']
for i in range(0,len(raw_key1)):
    tt=[]
    tt.append(raw_key1[i])
    tt.append(raw_key2[i])
    tt.append(pt[i])
    re=tripleSDES.f(tt[2],tt[0],tt[1],1)
    tt.append(''.join(re))
    table.append(tt)

#row5 to row8:decrypt
raw_key3=['1000101110','1011101111','1111111111','0000000000']
raw_key4=['0110101110','0110101110','1111111111','0000000000']
ct=['11100110','01010000','00000100','11110000']
for i in range(0,len(raw_key3)):
    tt=[]
    tt.append(raw_key3[i])
    tt.append(raw_key4[i])
    tt.append(ct[i])
    re=tripleSDES.f(tt[2],tt[0],tt[1],0)
    tt.insert(2,''.join(re))
    table.append(tt)



print('raw key 1         raw key 2         plaintext       ciphertext')
print('--------------------------------------------------------------')
for i in table:
    for j in i:
        print(j,end='        ')
    print()   

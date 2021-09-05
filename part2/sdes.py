import genKeys
import encryption
import decryption
import algo


key='1010000010'
keys=genKeys.gen2keys(key)
pt='10010111'
# encryption

# algo needs three args: t,keys,type
# t=plaintext/cipertext
# type=1 encryption, type=0 decryption
ct=algo.f(pt,keys,1)

# encryption.encrypt(pt,keys)
re=algo.f(ct,keys,0)

print('pt: ',pt)
print('ct: ',''.join(ct))
print('re: ',''.join(re))



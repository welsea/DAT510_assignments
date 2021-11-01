import CSPRNG
import DES
import ecdh


# Diffie-hellman key exchange
A = ecdh.DH('Alice')
B = ecdh.DH('Bob')
A.show()
B.show()
# Alice calculate the shared key
k = A.sharedKey(B.getPub())
# Bob calculate the shared key
k2 = B.sharedKey(A.getPub())
# the shared key is the same key
if k == k2:
    print("The shared key is:", k)


seed = k
k = CSPRNG.rc4(seed)  # CSPRNG-RC4
print("The key that will be used for encryption and decryption:", k)
pt = "Hi,Bob!"
print("Alice send:",pt)
# use DES to encrypt
des = DES.CIPHER(k, pt, 0)
ct = des.getCT()
print("Bod recieved:", ct[2:])
# decrypt
des2 = DES.CIPHER(k, ct, 1)
print("After decryption:", des2.getPT())

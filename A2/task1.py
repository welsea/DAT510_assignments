from types import CellType
import DH
import CSPRNG
from Crypto.Cipher import DES
import sys


def des(type, text, key):
    key = key.to_bytes(8, byteorder="big")

    result = ''
    d = DES.new(key, DES.MODE_ECB)
    # type = 0 encrypt, type=1 decrypt
    if type == 0:
        while len(text) % 8 != 0:
            text += ' '
        result = d.encrypt(text.encode('utf-8'))
    else:
        result = d.decrypt(text).decode()
        result.rstrip(' ')
    return result


def convert(ct):
    ctb = int.from_bytes(ct, byteorder=sys.byteorder)
    ctb = bin(ctb)
    return ctb


seed = DH.dh()  # Diffie-hellman key exchange
k = CSPRNG.rc4(seed)  # CSPRNG-RC4
print("The key that will be used for encryption and decryption:", k)
pt = input("Alice send:")
ct = des(0, pt, k)
ctb = convert(ct)
print("Bod recieved:", ctb[2:])
ppt = des(1, ct, k)
print("After decrypt:", ppt)

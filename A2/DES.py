import sys
from Crypto.Cipher import DES


class CIPHER:
    def __init__(self, key, msg, type):
        self.key = key.to_bytes(8, byteorder="big")
        self.result = ''
        self.d = DES.new(self.key, DES.MODE_ECB)
        self.type = type

        # type=0 encrypt
        # type=1 decrypt
        if self.type == 0:
            self.msg = msg
            CIPHER.encrypt(self)
            CIPHER.convert2Bi(self)
        else:
            self.msg = msg
            CIPHER.convert2Bytes(self)
            CIPHER.decrypt(self)

    # turn cipher text into binary
    def convert2Bi(self):
        # convert to binary
        i = int.from_bytes(self.ct, byteorder=sys.byteorder)
        self.ctbi = bin(i)

    # turn cipher text into bytes
    def convert2Bytes(self):
        i = int(self.msg, 2)
        self.ctby = (i).to_bytes(8, byteorder='little')

    def encrypt(self):
        while len(self.msg) % 8 != 0:
            self.msg += ' '
        self.ct = self.d.encrypt(self.msg.encode('utf-8'))

    def decrypt(self):
        try:
            self.pt = self.d.decrypt(self.ctby).decode()
            self.pt.rstrip(' ')
        except:
            self.pt = 'Refresh the website please.'

    # return the cipher text

    def getCT(self):
        return self.ctbi

    # return the plaintext
    def getPT(self):
        return self.pt

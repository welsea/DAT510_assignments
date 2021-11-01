import ec
import random


class DH:
    'Elliptic Curve Diffie-Hellman Key Exchange'
    cy = ec.CyclicGroup()
    n = len(cy)

    def __init__(self, name):
        self.name = name
        # private key
        self.pr = random.randint(0, DH.n)
        # public key
        self.pu = DH.cy[self.pr-1]

    def getPub(self):
        # return public key
        return self.pu

    def show(self):
        print(self.name+" choose a private key.")
        print(self.name+"\'s public key is ", self.pu)

    def sharedKey(self, opu):
        # shared key=private key(pr) * other user's public key(opu)
        opr = self.cy.index(opu)+1
        if self.pr*opr > self.n:
            k = self.cy[(self.pr*opr) % self.n-1]
        else:
            k = self.cy[self.pr*opr-1]
        return k

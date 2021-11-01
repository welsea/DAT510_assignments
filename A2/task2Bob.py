# app.py
from flask import Flask, request
import ecdh
import requests
import CSPRNG
import DES

app = Flask(__name__)
name = 'Bob'
# create Bob's key pair
B = ecdh.DH(name)
pu = B.getPub()
r = 0
k = 0
sk = 0


def get():
    global r, k, sk
    # get the public key from Alice
    r = requests.get('http://127.0.0.1:80/getpub').text
    # calculate the shared key
    k = B.sharedKey(int(r))
    # use rc4 to generate secret key
    sk = CSPRNG.rc4(k)


# demo msg
msg = "Hi!"


@app.route("/")
def bob():
    re = getmsg()
    ct = sendmsg()
    br = '<br>'
    get()
    opt = name+' choose a private key.' + br \
        + name+"\'s public key is "+str(pu)+br \
        + name+" get the public key from Alice: "+r+br \
        + "Calculate the shared key:"+str(k) + br\
        + "Calculate the secret key use RC4."+br+br\
        + "Recive the massge from Alice:" + str(re[1][2:]) + br\
        + "After decrtpt: "+re[0]+br+br\
        + "Send the message: "+msg + br\
        + "message after encrypt: "+str(ct[2:])
    return opt


@app.route("/getpub")
def getPub():
    return str(pu)


# send the encrypt message
@app.route("/sendmsg")
def sendmsg():
    des = DES.CIPHER(sk, msg, 0)
    ct = des.getCT()
    return ct


@app.route("/getmsg")
def getmsg():
    # get the encrypt message from Alice
    ct = requests.get('http://127.0.0.1:80/sendmsg').text
    # decrypt the message
    des = DES.CIPHER(sk, ct, 1)
    pt = des.getPT()
    return pt, ct


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

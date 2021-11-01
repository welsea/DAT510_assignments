from flask import Flask, request
import ecdh
import requests
import CSPRNG
import DES


app = Flask(__name__)


name = "Alice"
# create Alice's key pair
A = ecdh.DH(name)
pu = A.getPub()
r = 0
k = 0
sk = 0


def get():
    global r, k, sk
    # get the public key from Bob
    r = requests.get('http://127.0.0.1:5000/getpub').text
    # calculate the shared key
    k = A.sharedKey(int(r))
    # use rc4 to generate secret key
    sk = CSPRNG.rc4(k)


# demo msg
msg = 'Hi, Bob!'


@app.route("/")
def alice():
    br = '<br>'
    ct = sendmsg()
    re = getmsg()
    get()
    opt = name+' choose a private key.' + br \
        + name+"\'s public key is "+str(pu) + br\
        + name+" get the public key from Bob: "+r + br\
        + "Calculate the shared key: "+str(k)+br\
        + "Calculate the secret key use RC4."+br+br\
        + "Send the message: "+msg + br\
        + "message after encrypt: "+str(ct[2:])+br+br \
        + "Alice get the message from Bob: "+re[1][2:]+br\
        + "After decrypt: "+re[0]
    return opt


# send the publick key
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
    # get the encrypt message
    ct = requests.get('http://127.0.0.1:5000/sendmsg').text
    # decrypt the message
    des = DES.CIPHER(sk, ct, 1)
    pt = des.getPT()
    return pt, ct


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

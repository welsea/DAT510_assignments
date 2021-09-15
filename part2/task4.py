# app.py
from flask import Flask,request  
import tripleSDES      
import binascii

app = Flask(__name__)             

@app.route("/")                   
def decrypt():
    rawKey1='1000101110'
    rawKey2='0110101110'
    cipher=request.args.get('cipher')
    # decryption
    re=tripleSDES.f(cipher,rawKey1,rawKey2,0)
    re=''.join(re)
    re=chr(int(re,2))

    return 'Output: '+re
    
if __name__ == "__main__":        
    app.run(debug=True)
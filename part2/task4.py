# app.py
from flask import Flask,request  
import tripleSDES      

app = Flask(__name__)             

@app.route("/")  

# 0101110101010111110111001101110001010100:Hello
# http://127.0.0.1:5000/?cipher=0101110101010111110111001101110001010100
# or use test4.py to generate new ciphertext
def decrypt():
    rawKey1='1000101110'
    rawKey2='0110101110'
    cipher=request.args.get('cipher')
    # decryption
    pt=''
    for i in range(0,len(cipher),8):
        result=tripleSDES.f(cipher[i:i+8],rawKey1,rawKey2,0)
        result=''.join(result)
        result=chr(int(result,2))
        pt+=result

    return 'Output: '+pt
    
if __name__ == "__main__":        
    app.run(debug=True)
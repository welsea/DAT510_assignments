import SDES

# type=1, encrtpt. type=0, decrypt.
def f(t,raw_key1,raw_key2,type):

    if type==1:
        #encrypt with key1
        interM=SDES.f(t,raw_key1,1)
        #decrypt with key2
        interM2=SDES.f(interM,raw_key2,0)
        #encrpt with key1
        re=SDES.f(interM2,raw_key1,1)
    else:
        #decrypt with key1
        interM=SDES.f(t,raw_key1,0)
        #encrypt with key2
        interM2=SDES.f(interM,raw_key2,1)
        #decryprt with key1
        re=SDES.f(interM2,raw_key1,0)

    return re
import DH
import CSPRNG


# Diffie-hellman key exchange
seed=DH.dh()

# CSPRNG-RC4
k=CSPRNG.rc4(seed)
print("The key that will be used for encryption and decryption:",k)

#encrypt

#decrypt




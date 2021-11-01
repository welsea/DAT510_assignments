# rc4
def initialS():
    # S contain 256 items, from 0 to 255.
    S = list()
    i = 0
    for i in range(256):
        S.append(i)
    return S


def initialT(K):
    # T contain 256 items.
    n = len(K)
    T = list()
    for i in range(256):
        # Repeat of seed.
        T.append(K[i % n])
    return T


def scheduling(S, T):
    j = 0
    for i in range(256):
        j = (j+S[i]+T[i]) % 256
        # swap S[i], S[j]
        S[i], S[j] = S[j], S[i]
    return S


def keyStream(S, n):
    i = 0
    j = 0
    for r in range(n):
        i = (i+1) % 256
        j = (j+S[i]) % 256
        # swap S[i], S[j]
        S[i], S[j] = S[j], S[i]
        t = (S[i]+S[j]) % 256
        k = S[t]
    return k


def rc4(Kab):
    seed = list()
    for i in str(Kab):
        seed.append(int(i))

    # initialization S array and Key array
    S = initialS()
    T = initialT(seed)

    # Initial permutation of S
    S = scheduling(S, T)

    # Stream generation
    k = keyStream(S, Kab)
    return k

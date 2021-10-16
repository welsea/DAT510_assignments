
# rc4
def initialS():
    s = list()
    i = 0
    while i < 255:
        i += 1
        s.append(i)
    return s


def initialT(seed):
    t = list()
    i = j = 0
    while i < 255:
        if j == len(seed):
            j = 0
        t.append(int(seed[j]))
        i += 1
        j += 1
    return t


def scheduling(s, t):
    j = 0
    for i in range(0, 255):
        j = (j+s[i]+t[i]) % 256
        # swap s[i], s[j]
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
    return s


def stream(s, n):
    i = j = 0
    x = 0
    while x < n:
        x += 1
        i = (i+1) % 256
        j = (j+s[i]) % 256
        # swap s[i], s[j]
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        t = (s[i]+s[j]) % 256
        k = s[t]
    return k


def rc4(Kab):
    seed = list()
    for i in str(Kab):
        seed.append(i)

    # initialization S array and Key array
    s = initialS()
    t = initialT(seed)

    # Initial permutation of S
    s = scheduling(s, t)

    # Stream generation
    k = stream(s, len(seed))

    return k

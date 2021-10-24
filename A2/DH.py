import random
def e(n, p):
    x = yy = 0
    y = xx = 1
    while p:
        q = n // p
        n, p = p, n % p
        x, xx = xx - q * x, x
        y, yy = yy - q * y, y
    return xx, yy, n


def inverse(n, p):
    i = e(n, p)[0]
    while i < 0:
        i += p
    return i


def G(a, p, g1, g2):
    if g1 == (0, 0) or g2 == (0, 0):
        x = g1[0]+g2[0]
        y = g1[1]+g2[1]
        return (x, y)

    # infinite
    if g1[0] == g2[0]:
        if (-g1[1]) % p == g2[1] or (-g1[1]) % p == g2[1]:
            return (0, 0)

    if g1 == g2:
        s = (3*g1[0]*g1[0]+a)*inverse(2*g1[1], p)
    else:
        s = (g2[1]-g1[1])*inverse(g2[0]-g1[0], p)

    x = (s*s-g1[0]-g2[0]) % p
    y = (s*(g1[0]-x)-g1[1]) % p

    return (x, y)


def curve():
    # get a ellipic curve
    # a,b,p,g
    a = int(input("Enter the a for Elliptic Curve (default:2) :") or "2")
    b = int(input("Enter the b for Elliptic Curve (default:2) :") or "2")
    p = int(input("Enter the p (default:17) :") or "17")

    print("Curve: y^2 = x^3 + %dx + %d (mod %d)" % (a, b, p))

    gl = list()
    gs = str(input("Enter the G(generator) (default:5,1) :") or "5,1")
    gl = list(gs.split(','))
    gl[0] = int(gl[0])
    gl[1] = int(gl[1])
    g = tuple(gl)

    return a, b, p, g


# use ellipic curve to generate a cyclic group for DH key exchange
def CyclicGroup(a, p, g):
    cy = list()
    cy.append(g)
    r = ()+g
    r = G(a, p, g, r)
    while r not in cy:
        cy.append(r)
        r = G(a, p, r, g)
    return cy


# diffie-hellman key exchange, use x coordnates in cyclic groups
def priavteKey(n):
    pk = random.randint(0, n)
    return pk


def publicKey(pk, cy):
    yk = cy[pk-1][0]
    return yk


def sharedKey(a, b, n, cy):
    if a*b > n:
        k = cy[(a*b) % n-1][0]
    else:
        k = cy[a*b-1][0]
    return k


def exchange(n, cy):
    # alic choose a private key
    print("Alice choose a private key.")
    pA = 121
    # pA=privateKey(n)

    # bob choose a private key
    print("Bob choose a private key.")
    pB = 203
    # pB=privateKey(n)

    # calculate the public key
    pbA = publicKey(pA, cy)
    pbB = publicKey(pB, cy)

    print("Alice\'s public key:", pbA)
    print("Bob\'s public key:", pbB)

    # calculate the K
    k = sharedKey(pA, pB, n, cy)
    print("The shared key of Alice and bob:", k)

    return k


def dh():
    # c=curve()
    ###---test-----###
    c = (0, -4, 211, (2, 2))
    print("Curve: y^2 = x^3 + %dx + %d (mod %d)" % (c[0], c[1], c[2]))
    print("Generator:", c[3])
    cy = CyclicGroup(c[0], c[2], c[3])
    # print("Clyclic group:")
    # for i in range(0,len(cy)):
    #     print(i+1,":",cy[i])
    ###---test-----###

    n = len(cy)
    # the number of sub-sequence of cyclic group
    print("n=", n)
    k = exchange(n, cy)

    return k

def e(n, p):
    x = 0
    x2 = 0
    y = 1
    y2 = 1
    while p:
        q = n // p
        n, p = p, n % p
        x, y2 = y2 - q * x, x
        y, x2 = x2 - q * y, y
    return y2, x2, n


def inverse(n, p):
    i = e(n, p)[0]
    while i < 0:
        i += p
    return i


def G(a, p, g1, g2):
    # g1 or g2 is origin
    if g1 == (0, 0) or g2 == (0, 0):
        x = g1[0]+g2[0]
        y = g1[1]+g2[1]
        return (x, y)

    # infinite
    if g1[0] == g2[0]:
        if (-g1[1]) % p == g2[1] or (-g1[1]) % p == g2[1]:
            return (0, 0)
    # if g1==g2
    # s=((3x1)^2+a)*inverse(2*y1)
    if g1 == g2:
        s = (3*g1[0]*g1[0]+a)*inverse(2*g1[1], p)
    # else g1!=g2
    # s=(y2-y1)*inverse(x2-x1)
    else:
        s = (g2[1]-g1[1])*inverse(g2[0]-g1[0], p)

    # caculate the next point in cyclic group
    x = (s*s-g1[0]-g2[0]) % p
    y = (s*(g1[0]-x)-g1[1]) % p

    return (x, y)

# use ellipic curve to generate a cyclic group for DH key exchange
def CyclicGroup():
    c = (0, -4, 211, (2, 2))
    a = c[0]
    p = c[2]
    g = c[3]
    cy = list()
    cyx=list()
    cy.append(g)
    cyx.append(g[0])
    r = ()+g
    # get the next point
    r = G(a, p, g, r)
    # add the point into cyclic group
    # cyx only take the x coordinator
    while r not in cy:
        cy.append(r)
        cyx.append(r[0])
        r = G(a, p, r, g)
    return cyx
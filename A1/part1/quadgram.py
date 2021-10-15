def quad():
    fhand=open('english_quadgrams.txt')
    file=fhand.readlines()
    quadgram=set()
    for line in file:
        quadgramL=line.split(' ')
        if int(quadgramL[1][:-1]) > 15000:
            # quadgramD[quadgramL[0]]=int(quadgramL[1][:-1])
            quadgram.add(quadgramL[0])

    return quadgram
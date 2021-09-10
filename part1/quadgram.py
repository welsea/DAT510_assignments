def quad():
    fhand=open('english_quadgrams.txt')
    file=fhand.readlines()
    quadgramD={}
    for line in file:
        quadgramL=line.split(' ')
        if int(quadgramL[1][:-1]) > 1000:
            quadgramD[quadgramL[0]]=int(quadgramL[1][:-1])

    quadgram=list(quadgramD.keys())

    return quadgram

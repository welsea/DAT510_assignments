def quad():
    fhand=open('english_quadgrams.txt')
    file=fhand.readlines()
    quadgramD={}
    for line in file:
        quadgramL=line.split(' ')
        quadgramD[quadgramL[0]]=int(quadgramL[1][:-1])

    quadgram=list(quadgramD.keys())

    return quadgram

def p(text,order):
    p_key=[]
    for i in range(0,len(order)):
        try:
            p_key.append(text[order[i]-1])
        except IndexError:
            print(text)
    return p_key
def p(text,order):
    p_key=[]
    for i in range(0,len(order)):
        p_key.append(text[order[i]-1])
    return p_key
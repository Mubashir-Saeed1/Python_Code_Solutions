def has(t):
    n=t.split()
    tn=[]
    for x in range(0,len(n)):
        w=n[x]
        tn.append(w)
    j=tuple(tn)
    g=hash(j)
    return g
tu=input('Enter Elements of Tuple: ')
q=has(tu)
print(hash(tu))
print(q)

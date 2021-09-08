tu=input('Enter Tuple Elements: ')
a=tu.split()
b=[]
for x in range(len(a)):
    c=int(a[x])
    b.append(c)
d=tuple(b)
print(b)
print(d)

def con(a):
    s=str(a)
    return s
j=int(input('Enter Number of Elements of Tuple: '))
d=[]
for x in range(j):
    k=input(f'Enter Element {x+1}: ')
    d.append(k)
t=tuple(d)
pro=con(t)
print(pro)

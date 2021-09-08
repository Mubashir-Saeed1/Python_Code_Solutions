t=(3,3,3,6,6)
k=list(t)
j=int(input('Enter the Number of Elements to be Added in Tuple: '))
print('Enter Elements to be Added')
for x in range(j):
    d=input(f'Enter Element {x+1}: ')
    k.append(d)
final=tuple(k)
print(final)

def las4(a):
    print(f'4th Element = {a[3]}')
    print(f'4th Element From the Last = {a[-4]}')
lis=()
n=int(input('Enter The Number of Elements of the Tuple: '))
for x in range(n):
    c=int(input(f'Enter the Element {x+1}: '))
    lis.append(c)
#lists=tuple(lis)
last=las4(lists)

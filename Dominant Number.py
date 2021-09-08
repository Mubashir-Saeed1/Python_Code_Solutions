def dom(a,b):
    j,k=0,0
    for x in range(2,a):
        if a%x==0:
            j+=x
    print(j)
    for y in range(2,b):
        if b%y==0:
            k+=y
    print(k)
    if j>k:
        return 1
    elif k>j:
        return 2
    else:
        return 0
print('Enter Two Numbers to Check Their Dominance')
a=int(input('Enter 1st Number: '))
b=int(input('Enter 2nd Number: '))
d=dom(a,b)
if d==2:
    print(f'{b} is Dominant Over {a}')
elif d==1:
    print(f'{a} is Dominant Over {b}')
else:
    print('No Dominance')

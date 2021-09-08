def cfs(c):
    k=0
    for x in range(c,0,-1):
        t1=x
        t2=x-1
        t3=x-2
        t4=x-3
        t=t1+t2+t3+t4
        print(t)
        if t==c:
            k=1
            break
    return k
c=int(input('Enter a Number to Check Whether it is CFS or Not: '))
r=cfs(c)
if r==1:
    print('The Number You Entered is a CFS Number')
else:
    print('The Number You Entered is Not a CFS Number')

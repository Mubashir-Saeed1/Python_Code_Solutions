def ga(a):
    lists=[]
    k=0
    t=0
    inte=0
    for i in range(len(a)):
        k+=int(a[i])
        inte=k/(i+1)
        lists.append(inte)
    print(f'Moving Averages = {lists}')
    y=len(lists)
    for j in lists:
        t+=j
    t=t/y
    print(f'Grand Moving Average = {t}')
n=int(input("Enter Number of Elements: "))
lis=[]
for x in range(0,n):
    a=int(input(f'Enter Element {x+1}: '))
    lis.append(a)
print(f'The Elements You Entered are= {lis}')
ga(lis)

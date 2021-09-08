def count(lis):
    j=0
    for x in lis:
        if x%2==0:
            j+=1
    return j
lists=[]
n=int(input('Enter Number of Elements of List: '))
for x in range(n):
    t=int(input(f'Enter Element {x+1} of the List: '))
    lists.append(t)
o=count(lists)
print(f'The Number of Even Elements = {o}')

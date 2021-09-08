class lar:
    def large(a):
        c=0
        for x in a:
            if x>c:
                c=x
        return c
lis=[]
n=int(input('Enter Number of Elements of The List: '))
for x in range(n):
    j=int(input(f'Enter Element {x+1}: '))
    lis.append(j)
d=lar
print(d.large(lis))

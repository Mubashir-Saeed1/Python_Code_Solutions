def fl6(lis):
    if lis[0]==6 or lis[-1]==6:
        return True
    else:
        return False
lists=[]
n=int(input('Enter the Number of Elements of the List: '))
for x in range(n):
    t=int(input(f'Enter the Element {x+1} of the List: '))
    lists.append(t)
o=fl6(lists)
if o:
    print('The List has 6 at the Beginning or at the End')
else:
    print("The List Doesn't have 6 at the Beginning or at the End")

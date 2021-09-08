def check(dic):
    t=input('Enter Key You Want to Check: ')
    for x in dic:
        if x==t:
            return True
        else:
            return False
dic={}
n=int(input('Enter Number of Keys of the Dictionary: '))
for x in range(1,n+1):
    k=input(f'Enter Key{x} of the Dictionary: ')
    v=input(f'Enter Value of Key{x} of the Dictionary: ')
    dic[k]=v
Check=check(dic)
if Check:
    print("The Key You Entered is Available")
else:
    print('The Key You Entered is Not Available')

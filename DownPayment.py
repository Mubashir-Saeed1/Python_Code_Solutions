x=float(input('Enter your Credit  :' ))
if int(x)>1000000:
    print('''You have a good Credit.
So, we have to put down 10%,
You have to pay,
''')
    print(1000000-(0.1*1000000))
else:
    print('''
You don't have a good Credit.
So, we have to put down 20%,
You have to pay,
''')
    print(1000000-(0.2*1000000))

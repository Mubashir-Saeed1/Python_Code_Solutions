w=int(input('Weight = '))
c=input('''
Is weight in pounds or Kilograms?
Please Enter P for Pounds and K for Kilograms.
''')
if c=='p' or c=='P':
    x=float(w)*0.45
    print(f'Your Weight is {x} Kilograms')
elif c=='k' or c=='K':
          x=float(w)/0.45
          print(f'Your Weight is {x} Pounds')

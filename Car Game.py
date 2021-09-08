c=True
start=False
stop=True
print('Please Enter "Help" for help')
while c:
    i=input('>')
    if i.lower()=='help':
        print('''
Start -> To Start the Car...
Stop  -> To Stop the Car...
Quit  -> To Quit the Game...
''')
    elif i.lower()=='start':
        if start:
            print('What are you doing, the car is already Started')
        else:
            start=True
            stop=False
            print("Car Started, We are ready to Go")
    elif i.lower()=='stop':
        if stop:
            print('What are you doing, the car is already Stopped')
        else:
            start=False
            stop=True
            print("Car Stopped")
    elif i.lower()=='quit':
        c=False
    else:
      print("Sorry!!!I Don't Understand that...")
else:
    print('!!!Game Ended!!!')


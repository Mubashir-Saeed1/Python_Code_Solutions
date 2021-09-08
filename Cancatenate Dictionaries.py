nod=int(input('Enter Number of Dictionaries You Want to Cancatenate: '))
maindictionary={}
for x in range(nod):
    print(f'Enter Dictionary {x+1}')
    keys=int(input(f'Enter Number of Keys of Dictionary {x+1}: '))
    k=1
    dic={}
    for x in range(keys):
        key=int(input(f'Enter Key {k}: '))
        item=int(input('Enter Item: '))
        k+=1
        newkeyanditem={key:item}
        dic.update(newkeyanditem)
    maindictionary.update(dic)
for t,s in maindictionary.items():
    print(t,s)

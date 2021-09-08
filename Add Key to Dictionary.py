dic={
    0:10,
    1:20,
    2:30
    }
d={3:40}
k=input('Enter Key: ')
i=input('Enter Item: ')
d={k:i}
dic.update(d)
for x,y in dic.items():
    print(x,y)

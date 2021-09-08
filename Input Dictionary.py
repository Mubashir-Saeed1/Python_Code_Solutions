dic={
    }
x=int(input('Enter Elements of the Dictionary: '))
for i in range(1,x+1):
    dic[i]=i*i
print(dic)
for x in dic:
    print(x)
for x in dic:
    print(dic[x])
for x,y in dic.items():
    print(x,y)

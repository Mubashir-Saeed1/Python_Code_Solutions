print('Institute 1')
f1=int(input('Enter Facilities for Institute 1: '))
a1=int(input('Enter Academics for Institute 1: '))
i1=int(input('Enter Infrastructure for Institute 1: '))
I1=f1+a1+i1
print('Institute 2')
f2=int(input('Enter Facilities for Institute 2: '))
a2=int(input('Enter Academics for Institute 2: '))
i2=int(input('Enter Infrastructure for Institute 2: '))
I2=f2+a2+i2
print('Institute 3')
f3=int(input('Enter Facilities for Institute 3: '))
a3=int(input('Enter Academics for Institute 3: '))
i3=int(input('Enter Infrastructure for Institute 3: '))
I3=f3+a3+i3
l=[I1,I2,I3]
l.sort()
l.reverse()
print(l)

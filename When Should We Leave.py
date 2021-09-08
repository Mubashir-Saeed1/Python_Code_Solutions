def time(x,y,z,a,b,c):
    m=0
    h=0
    m+=x
    if m>60:
        h+=1
        m-=60
    m+=y
    if m>60:
        h+=1
        m-=60
    m+=z
    if m>60:
        h+=1
        m-=60
    m+=a
    if m>60:
        h+=1
        m-=60
    m+=b
    if m>60:
        h+=1
        m-=60
    m+=c
    final(h,m)
def final(h,m):
    lth=int(input('Enter time(Hour) for the Appointment: '))
    ltm=int(input('Enter time(Minutes) for the Appointment: '))
    fh=lth-h
    fm=ltm-m
    if fm<0:
        fh-=1
        fm=60+fm
    print(f'You Should Leave at {fh}:{fm} ')
x=int(input('Enter time(minutes) in driving to the Mall: '))
y=int(input('Enter time(minutes) in Getting the Clothes dry: '))
z=int(input('Enter time(minutes) in having lunch in the Restaurant: '))
a=int(input('Enter time(minutes) in Getting Dog Food: '))
b=int(input('Enter time(minutes) in Getting money in the Bank: '))
c=int(input("Enter time(minutes) in driving to the Doctor's Office: "))
time(x,y,z,a,b,c)

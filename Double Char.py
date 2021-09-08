def cha(d):
    s=len(d)
    o=''
    for x in d:
        c=x*2
        o+=c
    return o
a=input('Enter any String: ')
b=cha(a)
print(b)

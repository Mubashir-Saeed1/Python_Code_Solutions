def yes(s1,s2):
    l1=list(s1)
    l2=list(s2)
    lis=[]
    for x in range(len(s2)):
        for y in range(len(s1)):
            if l2[x]==l1[y]:
                lis.append(y)
    k=len(lis)
    t=max(lis)
    print(t)
    print(lis[k-1])
    if lis[k-1]==t:
        return True
    else:
        return False
s1=input('Enter Main String: ')
s2=input('Enter Sub-String: ')
v=yes(s1,s2)
if v:
    print('Main String Contains the Sub-String')
else:
    print("Main String doesn't contain the Sub-String")

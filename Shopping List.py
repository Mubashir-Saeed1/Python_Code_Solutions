def shop(liss,lisd):
    lisc=[]
    for x in liss:
        for y in lisd:
            if x==y:
                lisc.append(x)
    for j in lisc:
        liss.remove(j)
        lisd.remove(j)
    print(f'Common Items= {lisc}')
    print(f"Remaining Items in Son's List= {liss}")
    print(f"Remaining Items in Daughter's List= {lisd}")
liss=[]
lisd=[]
s=int(input("Enter Number of Items of Son's List: "))
d=int(input("Enter Number of Items of Daughter's List: "))
print("Son's List")
for x in range(s):
    so=input(f'Enter Element {x+1}: ')
    liss.append(so)
print("Daughter's List")
for y in range(d):
    da=input(f'Enter Element {y+1}: ')
    lisd.append(da)
last=shop(liss,lisd)

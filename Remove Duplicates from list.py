lists=[3,4,7,4,6,8,5,0]
uniques=[]
for x in lists:
    if x not in uniques:
        uniques.append(x)
uniques.sort()
print(uniques)

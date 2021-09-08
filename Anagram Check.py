def anagram(str1, str2):
    new = []
    strl = list(str1.lower())
    strk = list(str2.lower().split(" "))
    for x in range(len(strk)):
        if len(strk[x]) == len(strl):
            for y in range(len(strl)):
                if strl[y] in strk[x]:
                    new.append(strl[y])
                    strk[x].replace(strl[y], '')
    if new == strl:
        return True
    else:
        return False


checkAnagram = anagram('clint eastwood', 'old west action')
checkAnagram1 = anagram('Mubashir', 'My name is Mubashir')
print(checkAnagram)
print(checkAnagram1)

def anagram(str1, str2):
    lis1 = list(str1.lower())
    lis2 = list(str2.lower())
    new = []
    for x in range(len(lis1)):
        for y in range(len(lis2)):
            if lis1[x] in lis2[y]:
                new.append(lis2[y])
                lis2.remove(lis2[y])
                lis2.append('')
                break
    if new == lis1:
        return True
    else:
        return False


check = anagram("public relations", "crap built on lies")
checkAnagram = anagram('clint eastwood', 'old west action')
check2 = anagram('dog', 'god')
print(check)
print(checkAnagram)
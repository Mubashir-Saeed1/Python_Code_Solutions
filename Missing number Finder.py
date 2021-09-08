def finder(arr1, arr2):
    arr2.sort()
    for x in arr2:
        if x in arr1:
            arr1.remove(x)
    return arr1[0]


finder = finder([5, 5, 7, 7], [5, 7, 7])
print('The Missing Number is: ', finder)

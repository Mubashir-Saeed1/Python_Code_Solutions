def largest_continuous_sum(arr):
    if len(arr) == 0:
        return 0
    sum = l_number = arr[0]
    for x in arr[1:]:
        sum = max(sum + x, x)
        l_number = max(l_number, sum)
    return l_number


largest = largest_continuous_sum([1, 2, -1, 3, 4, -1])
largest2 = largest_continuous_sum([1, 2, -1, 3, 4, 10, 10, -10, -1])
largest3 = largest_continuous_sum([-1, 1])
print(largest)
print(largest2)
print(largest3)

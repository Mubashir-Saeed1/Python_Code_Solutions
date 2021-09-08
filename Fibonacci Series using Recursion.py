def fibonacci(n):
    a, b = 0, 1
    print(n)
    for x in range(n):
        a, b = b, a+b
    return a


print(fibonacci(10))
print(fibonacci(1))
print(fibonacci(23))

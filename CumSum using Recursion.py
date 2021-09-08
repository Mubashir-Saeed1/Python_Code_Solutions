def c_sum(n):
    if n == 0:
        return 0
    return n + c_sum(n-1)


print(c_sum(4))
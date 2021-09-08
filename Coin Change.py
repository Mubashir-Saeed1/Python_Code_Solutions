def coin_change(number, lis):
    min_num = number
    if number in lis:
        return 1
    else:
        for x in [c for c in lis if c <= number]:
            coins_list = 1 + coin_change(number - x, lis)
        if coins_list < min_num:
            min_num = coins_list
    return min_num


coins = [1, 5, 10, 25]
print(coin_change(45, coins))
print(coin_change(74, coins))
print(coin_change(74, coins))

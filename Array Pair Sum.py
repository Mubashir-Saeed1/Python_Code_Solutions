def pairs(lis, num):
    pairlist = []
    final = []
    for x in range(len(lis)):
        for y in range(len(lis)):
            if lis[x] + lis[y] == num:
                pairlist.append((lis[x], lis[y]))
    for item in pairlist:
        if item not in final:
            final.append(item)
    print(f'Number of Pairs: {len(final)}')
    print(f'List of Pairs: {final}')


pairs([1, 3, 2, 2], 4)
for i in range(4, 0, -1):
    for j in range(0, 4 - i):
        print(' ', end='')
    for j in range(0, i):
        print('*', end='')
    print()

# ls = range(4, 0, -1)
# print(*ls)

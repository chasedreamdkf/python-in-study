def p(x, n):
    m = 1
    for i in range(0, n, 1):
        m *= x
    return m


print('丁凯峰\n学号: 2302190128')
x, n = map(int, input('请输入两个整数: ').split())
print(p(x, n))

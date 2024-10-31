print('丁凯峰\n学号: 2302190128')
n = int(input('请输入一个整数: '))
Sum = 0
temp = 0
if n > 10:
    print('Data error!')
else:
    for i in range(1, n + 1, 1):
        temp = temp * 10 + i
        Sum += temp
    print('1+12+123+1234+···的前{}项的和: {}'.format(n, Sum))

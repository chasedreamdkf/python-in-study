print('丁凯峰\n学号: 2302190128')
a = int(input('请输入里程数（整数,Km）: '))
Time = int(input('请输入等待时间（整数,Min）: '))
if a <= 3:
    fee = 13 + Time
elif a <= 15:
    fee = 13 + 2.3 * (a - 3) + Time
else:
    fee = 13 + 2.3 * 12 + 2.3 * (a - 15) * 0.5 + Time
print('车费为: {:.2f}元'.format(fee))

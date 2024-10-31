# 求1-1/2+2/3-3/5.....的前n项和
import math

print('丁凯峰\n学号: 2302190128')
n = int(input('请输入整数: '))
Sum = a = 1
b = 2
if n == 2:
    Sum = 1 - 1 / 2

for i in range(3, n + 1):
    Sum += math.pow(-1, (i - 1)) * ((i - 1) / (a + b))
    a, b = b, a + b
print('1-1/2+2/3-3/5.....的前{}项和为: {:.6f}'.format(n, Sum))

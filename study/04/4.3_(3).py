# 阶乘和数
from math import factorial

print('丁凯峰\n学号: 2302190128')
n = int(input('请输入一个整数: '))
g = n % 10
s = n // 10 % 10
b = n // 100
if factorial(g) + factorial(s) + factorial(b) == n:
    print('YES')
else:
    print('NO')

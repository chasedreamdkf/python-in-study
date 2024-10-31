from math import factorial

n = int(input('请输入整数:'))
Sum = 0
for i in range(1, n + 1, 1):
    Sum += factorial(i)

print(Sum)

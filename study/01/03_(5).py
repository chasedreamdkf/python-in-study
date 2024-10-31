# 求自然对数的底数e
from math import factorial

limit = float(input('请输入下限:'))
e = 1
i = 1
while 1:
    e += 1 / factorial(i)
    if 1 / factorial(i) < limit:
        print(e)
        break
    i += 1

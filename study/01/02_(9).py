import math

PI = math.pi
a, b = input('请输入两个整数:').split()
a = eval(a)
b = eval(b)
x = (math.sqrt(2 * a * math.sin(PI / 3) * math.cos(PI / 3))) / (2 * a)
print('{:.3f}'.format(x))

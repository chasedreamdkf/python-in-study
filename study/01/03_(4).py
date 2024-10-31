# 求sin积分
import math

PI = math.pi
a, b = map(eval, input('请输入积分的范围（单位为PI）:').split())
c = a
d = int(input('请输入微分次数:'))
dx = (b - a) / d
S = 0
for i in range(0, d):
    S += (math.sin(a * PI) + math.sin(a * PI)) * dx * PI / 2
    a = a + dx
print('sin(x)从{0}到{1}的积分为{2}'.format(c, b, S))

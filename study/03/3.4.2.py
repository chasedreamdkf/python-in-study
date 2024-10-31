from math import pi

print('丁凯峰\n学号: 2302190128\n')
radius = 6371 * 1000
# 1. 计算地球表面积（表面积公式S = 4πR2）
surface_area = 4 * pi * radius ** 2
print(f'地球表面积为: {surface_area:.5e}平方米')

# 2. 计算地球体积（体积公式是V = 4πR3/3）
V = 4 * pi * radius ** 3 / 3
print(f'地球体积为: {V:.5e}立方米')

# 3. 计算地球赤道的周长（圆周长公式是L = 2πR）
L = 2 * pi * radius
print(f'地球赤道长度为: {L:.5e}米')

# 4.假设有一根绳子正好可以紧贴地球绕赤道一周，紧密的捆绑住地球。现在将绳子延长1 米, 计算绳子与地球之间的空隙大小
D = (L + 1) / 2 / pi - L / 2 / pi
print(f'绳子与地球之间的空隙大小为: {D:.5f}米')

# 5.判断老鼠是否可以从空隙中钻过
d = 0.1
if d > D:
    print("老鼠无法通过空隙!")
else:
    print("老鼠可以通过空隙!")

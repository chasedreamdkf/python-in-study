import math

# h=1/2 gt^2
H = 100
g = 10                                                                      # 重力加速度
print('小球从100m的高处自由落体到地面用时{0:.2f}s'.format(math.sqrt(2 * H / g)))
print('小球前三秒下降的高度为{0:.2f}m'.format(g * 3 * 3 / 2))

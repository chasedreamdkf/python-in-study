PI = 3.14
r, h = input('请输入圆柱体的半径和高(cm):\n').split()
r = eval(r)
h = eval(h)
S = 2*PI*r*r + 2*PI*r*h
V = PI*r*r*h
print('圆柱体的表面积为{0:.2f}cm²\n圆柱体的体积为{1:.2f}cm³'.format(S, V))

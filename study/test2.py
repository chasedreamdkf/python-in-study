# 我的代码
z = h = 0
s = list(input())
for i in s:
    if i == '北':
        z += 1
    elif i == '南':
        z -= 1
    elif i == '东':
        h += 1
    elif i == '西':
        h -= 1

if z or h:
    print('否')
else:
    print('是')

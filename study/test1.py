# 参考代码
l = input()
e, s, w, n = 0, 0, 0, 0
for i in l:
    if i == '东':
        e += 1
    elif i == '南':
        s += 1
    elif i == '西':
        w += 1
    else:
        n += 1

if e == w and s == n:
    print('是')
else:
    print('否')

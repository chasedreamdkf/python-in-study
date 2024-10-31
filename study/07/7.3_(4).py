print('丁凯峰 2302191028')
ls1 = [('dungeon', 7), ('winterfell', 4), ('bran', 9), ('meel0', 6)]
ls2 = [['Angle', '0121701100106', 99], ['Jack', '0121701100107', 86], ['Tom', '0121701100109', 65],
       ['Smith', '0121701100111', 100], ['Bob', '0121701100115', 77], ['Lily', '0121701100117', 59]]
ls1.sort(key=lambda x: x[1])
ls3 = sorted(ls2, key=lambda x: x[0],)
ls4 = sorted(ls2, key=lambda x: x[2],)
m, n = map(int, input('请输入两个整数: ').split())
if m > len(ls1):
    print(ls1)
else:
    for i in range(m):
        print(ls1[i], end=' ')
    print()
if n > len(ls2):
    print(ls3)
    print(ls4)
else:
    for i in range(n):
        print(ls3[i], end=' ')
    print()
    for i in range(n):
        print(ls4[i], end=' ')

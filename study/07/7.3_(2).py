from math import pow

print('丁凯峰 2302191028')
N = int(input('请输入一个整数: '))
a = 2

while a <= N:
    for b in range(2, N + 1):
        for c in range(b, N + 1):
            for d in range(c, N + 1):
                if pow(a, 3) == pow(b, 3) + pow(c, 3) + pow(d, 3):
                    print('Cube ={:<3},Triple ={}'.format(a, (b, c, d)))
    a += 1

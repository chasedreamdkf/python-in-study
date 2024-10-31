import math

M, N = input('请输入两个整数:').split()
M = int(M)
N = int(N)
print(math.gcd(M, N), math.lcm(M, N), sep=' ')

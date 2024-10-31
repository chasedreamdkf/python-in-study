import math


def is_prime_fast(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1, 1):
        if n % i == 0:
            return False
    else:
        return True


def output_prime(number):
    for i in range(number+1):
        if is_prime_fast(i):
            print(i, end=' ')


print('丁凯峰\n学号: 2302190128')
positive_int = int(input('请输入一个整数: '))
output_prime(positive_int)

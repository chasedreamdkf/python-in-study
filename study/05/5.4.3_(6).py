import math


def is_prime_fast(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    else:
        return True


def reverse_prime(number):
    for i in range(2, number):
        if is_prime_fast(i) and is_prime_fast(int(str(i)[-1::-1])) and str(i) != str(i)[-1::-1]:
            print(i, end=' ')


print('丁凯峰\n学号: 2302191028')
positive_int = int(input('请输入一个整数: '))
reverse_prime(positive_int)

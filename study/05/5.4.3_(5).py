import math


def is_prime_fast(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1, 1):
        if n % i == 0:
            return False
    else:
        return True


def palindrome_prime(number):
    for i in range(1, number):
        if is_prime_fast(i) and str(i)[-1::-1] == str(i):
            print(i, end=' ')


print('丁凯峰\n学号: 23021901258')
positive_int = int(input('请输入一个整数: '))
palindrome_prime(positive_int)

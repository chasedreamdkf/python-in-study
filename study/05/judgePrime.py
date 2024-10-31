import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1, 1):
        if n % i == 0:
            return False
    else:
        return True


if __name__ == '__main__':
    print('丁凯峰\n学号: 2302190128')
    positive_int = int(input('请输入一个正整数: '))
    print(is_prime(positive_int))

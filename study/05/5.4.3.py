from math import sqrt


def question_judge(question):
    """接收一个字符串为参数，根据参数值判断问题类型，调用合适的函数进行操作。"""
    if question == '素数':  # 如果输入”素数“，再输入一个正整数n，输出不大于n的所有素数
        n = int(input('请输入一个整数:'))
        output_prime(n)  # 输出素数
        return 1
    elif question == '回文素数':
        n = int(input('请输入一个整数:'))
        palindromic(n)  # 输出回文素数
        return 1
    elif question == '反素数':
        n = int(input('请输入一个整数:'))
        reverse_prime(n)  # 输出反素数
        return 1
    elif question == '哥德巴赫猜想':
        n = int(input('请输入一个整数:'))
        goldbach_conjecture(n)
        return 1
    else:
        return 0


def print_prime(n: int):
    for i in range(0, n + 1):
        if is_prime(i):
            print(i, end=' ')
    print()


def is_prime_normal(n):  # 判断素数的函数，一般方法
    """判断素数的函数,接收一个正整数为参数，参数是素数时返回True，否则返回False。"""
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True


def is_prime(n):
    """判断素数的函数,接收一个正整数为参数，参数是素数时返回True，否则返回False
    减小判定区间，减少循环次数，提升效率。"""
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        else:
            return True


def output_prime(number):
    """接收一个正整数为参数，遍历从0到number之间的所有整数，
    在一行中输出不大于number的所有素数，函数无返回值。"""
    for i in range(0, number + 1):
        if is_prime(i):
            print(i, end=' ')
    print()


def palindromic(num):
    for i in range(2, num):
        if is_prime(i) and str(i)[::-1] == str(i):
            print(i, end=' ')
    print()


def reverse_prime(number):
    """接收一个正整数参数，找出并在同一行内输出所有小于number的反素数，数字间用一个空格分隔。
    反素数指某数i及其逆序数都是素数，但数i对应的字符串不是回文字符串，函数无返回值。"""
    for i in range(2, number):
        if str(i)[::-1] != str(i) and is_prime(i) and is_prime(int(str(i)[::-1])):
            print(i, end=' ')
    print()


def goldbach_conjecture(num):
    if num < 4 or num % 2 != 0:
        print('Data error!')
        return
    for i in range(4, num):
        temp = num - i
        if temp < i:
            break
        if is_prime(i) and is_prime(temp):
            print(f'{num} = {i} + {temp}')


if __name__ == '__main__':
    print('丁凯峰\n学号: 2302190128')
    while 1:
        print("请输入：反素数、回文素数、素数、哥德巴赫猜想，选择对应功能: ")
        problems = input()
        if question_judge(problems) == 0:
            print('输入错误')
            break

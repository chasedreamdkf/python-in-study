def power(x, n):
    s = 1
    for i in range(1, n + 1):
        s = s * x  # s *= x
    return s


def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


def fabs(x):
    if x < 0:
        return float(-x)
    return float(x)


def ceil(x):
    if x > 0:
        return int(x) + 1
    else:
        return int(x)


def floor(x):
    if x > 0:
        return int(x)
    else:
        return int(x) - 1


def factorial(n):
    s = 1
    for i in range(1, n + 1, 1):
        s *= i
    return s


if __name__ == '__main__':
    print('欢迎使用私人定制的数学库!')
    print(power(5, 0))
    print(pow(0, 0))

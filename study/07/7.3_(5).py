def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = int(input('请输入一个整数: '))
ls = []
if not is_prime(num):
    for i in range(2, num):
        j = num // i
        if is_prime(i) and is_prime(j) and i * j == num:
            ls.append(i)
print(ls)

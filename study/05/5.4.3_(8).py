import judgePrime


def goldbach_conjecture(num):
    if num < 4 or num % 2 != 0:
        print('Data error!')
        return
    for i in range(4, num):
        temp = num - i
        if temp < i:
            break
        if judgePrime.is_prime(i) and judgePrime.is_prime(temp):
            print(f'{num} = {i} + {temp}')


if __name__ == '__main__':
    print('丁凯峰\n学号: 2302190128')
    positive_int = int(input('请输入一个正偶数: '))
    goldbach_conjecture(positive_int)

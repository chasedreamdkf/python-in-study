def type_judge(question):
    """@接收一个数字为参数，根据参数调用不同函数执行不同代码。"""
    if question == 1:
        chicken_rabbit()  # 用户输入为'鸡兔同笼'调用此函数
    elif question == 2:
        amount_of_goods()  # 用户输入为'物不知数'调用此函数
    elif question == 3:
        two_mice()  # 用户输入为'二鼠打洞'调用此函数
    elif question == 4:
        libai_buy_wine()  # 用户输入为'李白买酒'调用此函数
    elif question == 5:
        lamp_on_pagoda()  # 用户输入为'宝塔上的琉璃灯'调用此函数


def chicken_rabbit():
    """@1 鸡兔同笼"""
    heads, feet = map(int, input('请输入头数 脚数: ').split())
    flag = 0
    for rabbits in range(1, feet // 4, 1):
        cocks = heads - rabbits
        if cocks * 2 + rabbits * 4 == feet:
            print('有{}只鸡  有{}只兔'.format(cocks, rabbits))
            flag = 1
            continue
    if flag == 0:
        print("Data Error!")


def amount_of_goods():
    """@2 物不知数"""
    num = int(input('请输入一个整数: '))
    m = 0
    print('满足条件的数如下: ')
    for i in range(1, num, 1):
        if (i % 3 == 2) and (i % 5 == 3) and (i % 7 == 2):
            print(f'{i:<4}', end='')
            m += 1
            if m % 4 == 0:
                print()
    print()


def two_mice():
    """@3 老鼠打洞"""
    n = int(input('请输入墙的厚度（整数）: '))
    rat, mouse, day, time = 1, 1, 0, 1
    distance_of_rat, distance_of_mouse = 0, 0
    Sum = 0
    while Sum < n:
        Sum = 0
        day += 1
        distance_of_rat += rat
        distance_of_mouse += mouse
        Sum += distance_of_mouse + distance_of_rat
        rat = rat * 2
        mouse = mouse / 2
    rat = rat / 2
    mouse = mouse * 2
    distance_of_rat -= (Sum - n) * (rat / (rat + mouse))
    distance_of_mouse -= (Sum - n) * (mouse / (rat + mouse))
    print(f'{day}天')
    print(f'两只老鼠分别打洞{distance_of_rat:.1f}尺{distance_of_mouse:.1f}尺')


def libai_buy_wine():
    """@4 李白买酒"""
    o = 0
    for i in range(1, 6, 1):
        o = (o + 1) / 2
    print(f'李白壶中原有{o}斗酒')


def lamp_on_pagoda():
    """@5 宝塔琉璃灯"""
    y = 1
    lou = 8
    while True:
        x = y
        Sum = 0
        for i in range(1, lou + 1, 1):
            Sum += x
            x *= 2
        if Sum == 765:
            break
        else:
            y += 1
    for i in range(1, lou + 1, 1):
        print(f'第{i}层有{y:<3}盏琉璃灯')
        y *= 2


def menu():
    print("请输入对应数字以实现对应功能")
    print("1: 鸡兔同笼\n2: 物不知数\n3: 二鼠打洞\n4: 李白买酒\n5: 宝塔上的琉璃灯\nother: 退出程序")


if __name__ == '__main__':
    menu()
    while 1:
        choice = int(input("请输入对应数字以实现对应功能: "))  # 接收用户输入的字符串
        type_judge(choice)  # 调用判断输入的函数决定执行哪个函数
        if choice > 5:
            print("退出程序")
            break

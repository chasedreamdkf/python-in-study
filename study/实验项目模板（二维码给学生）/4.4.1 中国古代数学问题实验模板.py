# ------------      -------    --------    -----------    -----------
# @File       : 4.4.1 中国古代数学问题实验模板.py    
# @Contact    : vasp@qq.com
# @Copyright  : 2018-2025, Wuhan University of Technology
# @Modify Time: 2021/4/26 11:53
# @Author     : 赵广辉
# @Version    : 1.0
# @License    : 仅限用于Python程序设计基础实践教程(赵广辉,高等教育出版社)配套实验
# ------------      -------    --------    -----------    -----------

def type_judge(question):
    """接收一个字符串为参数，根据参数调用不同函数执行不同代码。
    这种写法不规范，但把输入、输出都放在一个函数中，方便管理。
    """
    if question == '鸡兔同笼':
        chicken_rabbit()  # 用户输入为'鸡兔同笼'调用此函数
    elif question == '物不知数':
        amount_of_goods()  # 用户输入为'物不知数'调用此函数
    elif question == '二鼠打洞':
        two_mice()  # 用户输入为'二鼠打洞'调用此函数
    elif question == '李白买酒':
        libai_buy_wine()  # 用户输入为'李白买酒'调用此函数
    elif question == '宝塔上的琉璃灯':
        lamp_on_pagoda()  # 用户输入为'宝塔上的琉璃灯'调用此函数
    else:
        print('输入错误')


def chicken_rabbit():
    """
    在同一行内输入用空格分隔的两个整数，代表头和脚的数量，计算并输出笼中各有多少只鸡和兔，
    如无解则输出“Data Error!”，函数无返回值。
    输入：35 94
    输出：有23 只鸡，12 只兔
    输入：100 5
    输出：Data Error!
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def amount_of_goods():
    """一些物品，不知道有多少个，3个3个数的话，还多出2个；5个5个数则多出3个；
    7个7个数也会多出2个。输入一个正整数，从小到大依次输出所有不超过输入数字
    且满足条件的物品数量，有多个答案时每行输出一个。
    例如输入：200
    输出：
    23
    128
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def two_mice():
    """有一堵十尺厚的墙，两只老鼠从两边向中间打洞。大老鼠第一天打洞一尺，小老鼠也是打洞一尺。
    大老鼠每天的打洞进度是前一天的一倍，小老鼠每天的进度是前一天的一半。计算并输出它们几天可以相逢，
    相逢时各打了多少尺。
    输入格式：输入1 个整数，代表墙的厚度，单位为尺
    输出格式：
    第一行输出1 个整数，表示相遇时所需的天数
    第二行输出2 个浮点数，分别为小鼠和大鼠打洞的距离，单位为尺，保留小数点后1 位数字。
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================

def libai_buy_wine():
    """大诗人李白，提着酒壶，从家里出来，酒壶中有酒若干。他边走边唱：无事街上走，提壶去买酒，
    遇店加一倍，见花喝一斗，五遇店和花，喝光壶中酒，计算并输出壶中原有酒几斗？
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def lamp_on_pagoda():
    """有一座八层宝塔，每一层都有一些琉璃灯，每一层的灯数都是上一层的二倍，
    已知共有765 盏琉璃灯，计算并输出每层各有多少盏琉璃灯。
    输出为8行，每行都是一个正整数，从上往下数字依次增大，每个数字代表本层宝塔上的琉璃灯数目。
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


if __name__ == '__main__':
    choice = input()    # 接收用户输入的字符串
    type_judge(choice)  # 调用判断输入的函数决定执行哪个函数

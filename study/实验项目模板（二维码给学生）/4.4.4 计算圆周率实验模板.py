# ------------      -------    --------    -----------    -----------
# @File       : 4.4.4 计算圆周率实验模板.py    
# @Contact    : vasp@qq.com
# @Copyright  : 2018-2025, Wuhan University of Technology
# @Modify Time: 2021/4/26 23:22
# @Author     : 赵广辉
# @Version    : 1.0
# @License    : 仅限用于Python程序设计基础实践教程(赵广辉,高等教育出版社)配套实验
# ------------      -------    --------    -----------    -----------
import math
import random
import matplotlib.pyplot as plt
import numpy as np
import turtle


def type_judge(pi_type):
    """接收一个字符串为参数，根据参数调用相应函数计算圆周率。
    @参数 pi_type：计算圆周率的方法
    """
    if pi_type == '割圆法':
        times = int(input())             # 输入一个切割次数的正整数
        return cutting_circle(times)     # 调用函数计算圆周率
    elif pi_type == '无穷级数法':
        threshold = float(input())       # 输入转为浮点数
        return leibniz_of_pi(threshold)  # 调用函数计算圆周率
    elif pi_type == '蒙特卡洛法':
        num = int(input())               # 输入转为整数
        s = int(input())                 # 输入随机数种子
        return monte_carlo_pi(num, s)    # 调用函数计算圆周率
    elif pi_type == '梅钦法':
        return machin_of_pi()            # 调用函数计算圆周率
    elif pi_type == '拉马努金法':
        num = int(input())               # 输入转为整数
        return ramanujan_of_pi(num)
    else:
        return f'输入错误'



def xy_of_polygon(r, side_num):
    """计算圆内接正多边形顶点坐标，返回数组。
    @参数 r：圆的半径
    @参数 side_num：正多边形的边数
    """
    angle = np.linspace(0, 2 * np.pi, side_num, False)  # 划分角度时不包含终点
    x = r * np.sin(angle)                               # 圆周上点的
    y = r * np.cos(angle)
    x = np.append(x, x[0])
    y = np.append(y, y[0])
    return x, y


def draw_circle(r, side_num):
    """创建图形和轴，用折线图绘制正多边形。
    @参数 r：圆的半径
    @参数 side_num：正多边形的边数
    """
    fig, ax = plt.subplots()           # 创建图形和轴
    plt.subplots_adjust(left=0.1, bottom=0.25)
    x, y = xy_of_polygon(r, side_num)
    plt.plot(x, y, lw=2, color='red')  # 设置线宽和颜色
    ax.set_aspect('equal')             # 设置坐标轴纵横比相等
    ax.set_xlim(-r-5, r+5)             # 设置x轴刻度起止值
    ax.set_ylim(-r-5, r+5)
    plt.draw()                         # 重新绘制多边形
    plt.show()                         # 显示图形


def cutting_circle(times):
    """
    接收表示分割次数的整数n 为参数，计算分割n 次时正多边形的边数和圆周率值，返回边数和圆周率值。
    @参数 times：分割次数
    π = 周长/(2*圆的半径)得到π的近似值。
    # 半径为1的圆内接正6边形边长也是1
    # 边长  side_length
    # 半径  radius
    # 圆周率 pi
    # 三角形的高 height
    # >>> cutting_circle(4)
    # 3.14103195089051
    """
    side_length = 1          # 初始边长
    edges = 6                # 初始边数
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================
    return pi


def monte_carlo_show(in_circle_lst, out_circle_lst):
    """
    @参数 in_circle_lst：落在圆内的点的坐标列表
    @参数 out_circle_lst：落在圆外的点的坐标列表

    """
    plt.rcParams['font.sans-serif'] = ['SimHei']   # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False     # 用来正常显示负号
    plt.figure(figsize=(11, 11))                   # 设置画布长宽
    x_in_circle = [x[0] for x in in_circle_lst]    # 落在圆内的点的列表x
    y_in_circle = [x[1] for x in in_circle_lst]    # 落在圆内的点的列表y
    x_out_circle = [x[0] for x in out_circle_lst]  # 落在圆外的点的列表x
    y_out_circle = [x[1] for x in out_circle_lst]  # 落在圆外的点的列表y
    plt.scatter(x_out_circle, y_out_circle, s=10, facecolors='blue')  # 绘制散点，落在圆外在点颜色用蓝色
    plt.scatter(x_in_circle, y_in_circle, s=5, facecolors='red')    # 绘制散点，落在圆内在点颜色用红色
    plt.title('蒙特卡洛法计算圆周率演示')                                     # 图的标题
    plt.show()                                                             # 显示绘制结果


# 给出turtle模板，学生填monte_carlo代码，帮助学生理解算法，了解turtle绘图
def monte_carlo_pi_turtle(n, s):
    """用turtle绘图模拟蒙特卡洛n次结果"""
    random.seed(s)
    turtle.tracer(1000)
    turtle.pensize(4)
    turtle.penup()
    turtle.goto(-300, -300)
    turtle.pendown()
    for i in range(4):
        turtle.forward(600)
        turtle.left(90)
    turtle.forward(300)
    turtle.pencolor('green')
    turtle.circle(300)
    hits = 0  # 落在圆内的计数器初值设为 0
    for i in range(1, n + 1):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)  # 生成两个随机数模拟一个点的坐标
        pos = (x ** 2 + y ** 2) ** 0.5                       # 计算坐标（x,y）到原点的距离
        if pos <= 1.0:                                       # 如果距离小于等于1，点在圆内
            hits = hits + 1
            turtle.pencolor('red')                           # 落在圆内在点颜色用红色
        else:                                                # 如果距离大于1，点在圆外
            turtle.pencolor('blue')                          # 落在圆内在点颜色用蓝色
        turtle.penup()
        turtle.goto(x * 300, y * 300)                        # 画笔抬起并移动到数值放大400倍的x,y处
        turtle.pendown()
        turtle.dot(3)                                        # 画一个半径为 3 的圆点
        if i % 10000 == 0:                                   # 实验为10000的倍数次时
            turtle.pencolor('black')
            pi = 4 * (hits / i)                              # 根据落在圆内外的点数量估算PI值
            turtle.penup()                                   # 画笔抬起
            turtle.goto(320, 150 - i // 1000 * 30)           # 移动到区域外记录当前PI值
            turtle.pendown()                                 # 画笔抬起
            turtle.write("{}次时PI的值是{:.4f}".format(i, pi), font=("宋体", 18, "normal"))
    turtle.hideturtle()  # 隐藏光标
    turtle.update()      # 刷新
    turtle.done()        # 结束绘制


def leibniz_of_pi(error):
    """接收用户输入的浮点数阈值为参数，用格雷戈里-莱布尼茨级数计算圆周率，返回圆周率值。
    @参数 error：阈值，当最后一项的绝对值小于给定error时停止计算并输出得到的π 值。
    # >>> leibniz_of_pi(2e-6)
    # 3.141588653589781
    # >>> leibniz_of_pi(1e-8)
    # 3.1415926335902506
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def monte_carlo_pi(num, s):
    """
    接收一个表示随机次数的整数和一个整数做随机数种子，用蒙特卡洛法计算圆周率。
    当产生点的坐标(x,y)落在圆内时执行in_circle_lst.append((x, y))将坐标加入到列表in_circle_lst,
    产生点的坐标(x,y)落在圆外部时执行out_circle_lst.append((x, y))将坐标加入到列表out_circle_lst,
    以浮点数形式返回圆周率值。
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def machin_of_pi():
    """用梅钦级数计算圆周率，返回圆周率值"""
    quarter_of_pi = 4 * math.atan(1/5) - math.atan(1/239)
    pi = 4 * quarter_of_pi
    return pi


def ramanujan_of_pi(n):
    """接收一个正整数n为参数，用拉马努金公式的前n项计算圆周率并返回。"""
    result = 0
    for i in range(n):
        result = result + ((2 * 2 ** 0.5)) * (math.factorial(4 * i) * (1103 + 26390 * i)) / (math.pow(math.factorial(i), 4) * math.pow(396, 4 * i))/9801
    pi = 1 / result
    return pi


if __name__ == '__main__':
    type_of_pi = input()             # 接收用户输入的字符串
    in_circle_lst, out_circle_lst = [], []
    cal_pi = type_judge(type_of_pi)  # 调用判断类型的函数
    print(cal_pi)                    # 输出函数运行结果

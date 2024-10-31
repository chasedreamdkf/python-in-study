# ------------      -------    --------    -----------    -----------
# @File       : 2.4.2 绘制特定图形.py    
# @Contact    : vasp@qq.com
# @Copyright  : 2018-2025, Wuhan University of Technology
# @Modify Time: 2021/4/26 10:37
# @Author     : 赵广辉
# @Version    : 1.0
# @License    : 仅限用于Python程序设计基础实践教程(赵广辉,高等教育出版社)配套实验
# ------------      -------    --------    -----------    -----------

# 利用turtle库绘制图2.4
# 以下为代码区
import turtle
import math

turtle.speed(0)
# =======================================================
# 此处去掉注释符号“#”并补充你的代码

# =======================================================

# 计算内接五角星的边长，数学问题
width = (math.sin(math.radians(36)) * 60) / math.sin(math.radians(126))
# =======================================================
# 此处去掉注释符号“#”并补充你的代码

# =======================================================
turtle.hideturtle()
turtle.done()

# [拓展] 尝试补充以下程序中每个函数的代码，每个函数只实现一个功能，
# 通过函数的调用来完成整个问题。
import turtle
import math


def shield():
    """由外向内依次绘制同心圆并按要求填充颜色"""
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================
    turtle.hideturtle()
    turtle.done()


def draw_circle(radium):
    """
    :参数 radium：圆的半径，单位为像素，整型
    函数功能为绘制半径为radium的圆。
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


# 填充圆环
def fill_circle(color, radium):
    """
    :参数 color：线条和填充颜色，字符串类型
    :参数 radium为圆的半径，整型
    函数功能为调用函数draw_circle()绘制半径为radium的圆并用color指定的颜色填充。
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


# 画并填充五角星
def draw_five(color, radium):
    """
    :参数 color：线条和填充颜色，字符串类型
    :参数 radium为圆的半径，整型
    函数功能为半径为radium的圆画内接五角星。
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


if __name__ == '__main__':
    shield()
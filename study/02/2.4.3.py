import turtle as t


def draw_chessboard(x, y):
    """@根据画笔初始位置坐标x,y和单元格宽度，绘制棋盘的方格"""
    t.penup()
    # 画边框
    t.goto(x - 15, y - 15)
    t.pendown()
    for i in range(2):
        t.forward(8 * width + 30)
        t.left(90)
        t.forward(9 * width + 30)
        t.left(90)
    t.penup()

    # 画横线
    for i in range(10):
        t.goto(x, y + width * i)
        t.pendown()
        t.forward(width * 8)
        t.penup()
    t.left(90)

    # 画竖线
    for i in range(9):
        t.goto(x + width * i, y)
        t.pendown()
        t.forward(width * 4)
        t.penup()
        t.forward(width)
        t.pendown()
        t.forward(width * 4)
        t.penup()


def draw_camp(x, y):
    """@ 根据画笔初始位置坐标x,y和单元格宽度，绘制棋盘帅营斜线"""
    for i in range(2):
        t.goto(x + width * 3, y + width * 9 * i)
        t.pendown()
        t.goto(x + width * 5, y + width * (2 + 5 * i))
        t.penup()
        t.goto(x + width * 3, y + width * (2 + 5 * i))
        t.pendown()
        t.goto(x + width * 5, y + width * 9 * i)
        t.penup()


def draw_chess():
    t.begin_fill()
    t.color('black', 'white')
    t.pendown()
    t.circle(width // 3)
    t.end_fill()
    t.penup()


def draw_piece_gun(x, y):
    """@ 绘制黑红双方的棋子炮"""
    for i in range(2):
        for j in range(2):
            t.goto(x + width * (4 + 18 * j) / 3, y + width * (2 + 5 * i))
            draw_chess()
            t.goto(x + width * (4 + 30 * j) / 5, y + width * (7 + 20 * i) / 4)
            t.color(c[i])
            t.write('炮', font=("华文新魏", 20, "normal"))


def draw_piece_soldier(x, y):
    """@ 绘制黑红双方的兵和卒棋子"""
    b = ['兵', '卒']
    for i in range(2):
        for j in range(5):
            t.goto(x + width * (2 * j + 1 / 3), y + width * 3 * (i + 1))
            draw_chess()
            t.goto(x + width * (2 * j - 1 / 5), y + width * (11 + 12 * i) / 4)
            t.color(c[i])
            t.write(b[i], font=("华文新魏", 20, "normal"))
            t.penup()


def draw_boundary(x, y):
    """@ 写楚河汉界的文字"""
    t.pen()
    t.goto(x + width * 2, y + width * 4 + 7)
    t.color('black')
    t.write('楚  河  汉  界', font=("华文新魏", 32, "normal"))
    t.penup()


def draw_piece_other(x, y):
    """@ 绘制其他棋子"""
    chess_pieces = [['车', '马', '相', '仕', '帅', '仕', '相', '马', '车'],
                    ['车', '马', '象', '士', '将', '士', '象', '马', '车']]
    for i in range(2):
        for j in range(9):
            t.goto(x + width * (j + 1 / 3), y + width * 9 * i)
            draw_chess()
            t.goto(x + width * (j - 1 / 5), y + width * (36 * i - 1) / 4)
            t.color(c[i])
            t.write(chess_pieces[i][j], font=("华文新魏", 20, "normal"))


if __name__ == '__main__':
    t.tracer(10)  # 取消注释可加速刷新绘制速度
    t.speed(0)  # 绘制速度
    t.pensize(2)  # 画笔粗线
    t.bgcolor('gray')  # 修改画布背景色
    width = 60  # 设置每格宽度
    t.screensize(10 * width, 12 * width)  # 画布大小为12倍单元格宽度
    pos_of_x, pos_of_y = -4 * width, -4 * width  # 画笔初始坐标
    c = ['red', 'green']
    draw_chessboard(pos_of_x, pos_of_y)  # 绘制空棋盘
    draw_camp(pos_of_x, pos_of_y)  # 绘制将帅营房
    draw_boundary(pos_of_x, pos_of_y)  # 绘制楚河汉界
    draw_piece_soldier(pos_of_x, pos_of_y)  # 绘制棋子兵和卒
    draw_piece_gun(pos_of_x, pos_of_y)  # 绘制棋子炮
    draw_piece_other(pos_of_x, pos_of_y)  # 绘制其他棋子
    t.hideturtle()  # 隐藏画笔
    t.update()  # 更新缓存
    t.done()  # 结束绘制

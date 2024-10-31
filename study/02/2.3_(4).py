import turtle as tr

l = int(input('请输入国际象棋棋盘小格的边长: '))
tr.hideturtle()
tr.penup()
tr.tracer(10)
tr.speed(0)

for i in range(0, 8, 1):
    for j in range(0, 8, 1):
        tr.goto(-4 * l + j * l, 4 * l - i * l)
        tr.begin_fill()
        if (j % 2 != 0 and i % 2 == 0) or (j % 2 == 0 and i % 2 != 0):
            tr.color("black", "black")
        else:
            tr.color("black", "white")
        tr.pendown()
        for k in range(0, 4, 1):
            tr.forward(l)
            tr.right(90)
        tr.end_fill()
        tr.penup()

tr.exitonclick()

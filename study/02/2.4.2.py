import turtle
import math

turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(0, -240)

#画圆圈
colors = ["red", "white", "red", "blue"]
m = 1
for color in colors:
    turtle.begin_fill()
    turtle.color(color, color)
    turtle.pendown()
    turtle.circle(240 - (m - 1) * 60)
    turtle.penup()
    turtle.goto(0, -240 + m * 60)
    turtle.end_fill()
    m += 1

# 五角星
width = (math.sin(math.radians(36)) * 60) / math.sin(math.radians(126))
turtle.begin_fill()
turtle.color("white", "white")
turtle.goto(0, 60)
turtle.right(72)
for i in range(0, 10, 1):
    turtle.forward(width)
    if i % 2 == 0:
        turtle.left(72)
    else:
        turtle.right(144)
turtle.end_fill()
turtle.exitonclick()

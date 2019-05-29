import turtle
import time

def hart_arc():#画心型圆弧
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
def move_pen_position(x,y):
    turtle.hideturtle()#隐藏画笔
    turtle.up()#提笔
    turtle.goto(x,y)#移动画笔到指定起始坐标
    turtle.down()
    turtle.showturtle()

love = "婷婷\n早日康复"

#初始化
turtle.setup(width = 800,height = 500)
turtle.color('red',"pink")
turtle.pensize(3)
turtle.speed(1)

#初始化画笔起始坐标
move_pen_position(x=0,y=-180)
turtle.left(140)
turtle.begin_fill()

turtle.forward(224)
hart_arc()
turtle.left(120)
hart_arc()

turtle.forward(224)
turtle.end_fill()

move_pen_position(0,0)
turtle.hideturtle()
turtle.color('#CD5C5C',"pink")
turtle.write(love,font =('Arial',30,'bold'),align = 'center')
window = turtle.Screen()
window.exitonclick()

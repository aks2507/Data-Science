import turtle
pen = turtle.Turtle()
turtle.bgcolor("pink")
slow=2
fast=400
pen.pensize(3)
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
def heart():
    pen.speed(slow)
    pen.fillcolor('red')

    pen.begin_fill()

    pen.left(140)
    pen.forward(113)

    pen.speed(fast)
    curve()
    pen.speed(slow)
    pen.left(120)
    pen.speed(fast)
    curve()
    pen.speed(slow)

    pen.forward(112)
    pen.end_fill()

heart()

pen.up()
pen.setpos(-128, -40)
pen.down()

pen.color('red')

pen.write("Valentine's Day?!?", font=(
    "Verdana", 20, "bold"))
pen.ht()
turtle.done()

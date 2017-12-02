# Classes - build a movie program!

# draw shapes

import turtle

def draw_square(slim):
    slim.shape("turtle")
    slim.speed(10)
    slim.color("black","green")
    slim.begin_fill()
    for i in range(1,5):
        slim.forward(100)
        slim.right(90)

    slim.end_fill()

def draw_circle(slim):
    slim.shape("turtle")
    slim.color("yellow")
    slim.circle(50)
def draw_triangle(slim):
    slim.shape("turtle")
    slim.color("blue")
    for i in range(1,4):
        slim.forward(100)
        slim.left(120)
def draw_ke():
    cc = turtle.Turtle()
    cc.speed(10)
    for i in range(1,3):
        cc.right(90*i)
        cc.forward(100*i)
    cc.right(180)
    cc.forward(100)
    for i in range(1,3):
        cc.left(180-45*i)
        cc.forward(125)
        cc.left(180)
        cc.forward(125)
    cc.penup()
    cc.right(45)
    cc.setpos(150,0)
    cc.pendown()

    for i in range(1,3):
        cc.forward(100)
        cc.right(90*i)

    for i in range(1,3):
        cc.forward(100*i)
        cc.left(90)

    cc.forward(100)
def draw_lotsofsquares():
    sq=turtle.Turtle()
    for i in range(0,36):
        sq.right(10)
        draw_square(sq)





window = turtle.Screen()
window.bgcolor("red")

#draw_ke()
some_turtle = turtle.Turtle()

#draw_square(some_turtle)
#draw_lotsofsquares()
#draw_circle(some_turtle)
#draw_triangle(some_turtle)

window.exitonclick()

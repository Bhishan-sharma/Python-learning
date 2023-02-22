import turtle

wn = turtle.Screen()
wn.setup(width=600,height=600)
wn.bgcolor("yellow")

a = turtle.Turtle()
a.color("red")
a.speed(20)
for i in range(80):
    a.circle(50)
    a.right(5)
    a.forward(5)
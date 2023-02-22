import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("ooo")
wn.setup(width=300,height=300)

colors = ["red","white","yellow","blue"]
list1 =[90,95,100]

a = turtle.Turtle()
a.color(random.choice(colors))
a.speed(60)
for i in range(350):
	a.circle(50)
	a.right(random.choice(list1))

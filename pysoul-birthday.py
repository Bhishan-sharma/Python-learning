import turtle
from unicodedata import name

birthdayhuman = input("Enter the name :")

wn = turtle.Screen()
wn.setup(width=600,height=600)
wn .bgcolor("red")

a = turtle.Turtle()
a.color("yellow")
a.speed(0)
a.pensize(10)

###########################
a.penup()
# co-ordintes for HAPPY
a.backward(200)
a.left(90)
a.forward(120)
a.right(90)
a.pendown()
###########################

#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
a.right(270)
a.forward(100)
a.backward(50)
a.right(90)
a.forward(60)
a.left(90)
a.forward(50)
a.backward(100)

a.penup()
a.right(90)
a.forward(30)
a.pendown()

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
a.left(90)
a.forward(100)
a.right(90)
a.forward(50)
a.right(90)
a.forward(100)
a.backward(50)
a.right(90)
a.forward(50)
a.backward(50)

a.penup()
a.backward(30)
a.pendown()

#PPPPPPPPPPPPPPPPPPPPPPPPPP
for i in range(2):
    a.right(90)
    a.forward(50)
    a.backward(100)
    a.forward(100)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.backward(50)
    a.penup()
    a.backward(30)
    a.pendown()

##YYYYYYYYYYYYYYYYYYYYYYYYY
a.right(70)
a.forward(60)
a.backward(60)
a.left(120)
a.forward(60)
a.backward(120)
a.left(40)

######################
a.penup()
# co-ordinates  for BIRTH
a.forward(110)
a.right(90)
a.forward(380)
a.pendown()
#####################

#BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
a.left(90)
a.forward(100)
a.left(90)
a.forward(60)
a.left(90)
a.forward(100)
a.left(90)
a.forward(60)
a.left(90)
a.forward(50)
a.left(90)
a.forward(60)

a.penup()
a.forward(60)
a.pendown()

#IIIIIIIIIIIIIIIIIIIIIIII
a.left(90)
a.forward(50)
a.backward(100)
a.left(90)
a.forward(30)
a.backward(60)
a.forward(30)
a.right(90)
a.forward(100)
a.left(90)
a.forward(30)
a.backward(60)

a.penup()
a.backward(30)
a.pendown()

#RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
a.left(90)
a.forward(100)
a.backward(100)
a.left(90)
a.forward(60)
a.right(90)
a.forward(50)
a.right(90)
a.forward(50)
a.left(130)
a.forward(60)

a.penup()
a.left(70)
a.forward(60)
a.pendown()

#TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
a.left(70)
a.forward(80)
a.backward(100)
a.forward(100)
a.left(90)
a.forward(20)
a.backward(40)

a.penup()
a.backward(30)
a.pendown()

#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
a.left(90)
a.forward(100)
a.backward(50)
a.left(90)
a.forward(50)
a.left(90)
a.forward(50)
a.backward(100)

#####################
a.penup()
# co-ordinates of day
a.backward(30)
a.left(90)
a.forward(330)
a.pendown()
####################

#DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
a.left(90)
a.forward(120)
a.left(130)
a.forward(100)
a.left(100)
a.forward(100)
a.right(140)

a.penup()
a.forward(110)
a.pendown()

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
a.right(90)
a.forward(120)
a.backward(120)
a.left(90)
a.forward(60)
a.right(90)
a.forward(120)
a.backward(60)
a.right(90)
a.forward(60)
a.backward(60)

a.penup()
a.backward(60)
a.pendown()

#YYYYYYYYYYYYYYYYYYYYYYYYYYYYY
a.right(70)
a.forward(60)
a.backward(60)
a.left(120)
a.forward(60)
a.backward(120)
a.left(40)

name1 = turtle.Turtle()
name1.speed(0)
name1.shape("square")
name1.color("white")
name1.penup()
name1.hideturtle()
name1.goto(0, -210)
name1.write(f"{birthdayhuman}", align="center",
		font=("candara", 36, "bold"))

while True:
    wn.update()
wn.mainloop()
import turtle
import random

delay = 0.1
score = 0

wn = turtle.Screen()
wn.setup(width=600,height=600)
wn.bgcolor("black")

player = turtle.Turtle()
player.color("yellow")
player.shape("circle")
player.penup()
player.goto(0,0)
player.direction = "Stop"

coin = turtle.Turtle()
coin.speed(0)
coin.shape("circle")
coin.color("white")
coin.penup()
coin.goto(0, 100)

Scoreboard = turtle.Turtle()
Scoreboard.speed(0)
Scoreboard.shape("square")
Scoreboard.color("white")
Scoreboard.penup()
Scoreboard.hideturtle()
Scoreboard.goto(0, 230)
Scoreboard.write("Hello!!!   Your Score : 0", align="center",
		font=("candara", 24, "bold"))

def jump():
    if player.direction != "down":
        player.direction = "up"

def dig():
	if player.direction != "up":
		player.direction = "down"

def goright():
    if player.direction != "left":
        player.direction = "right"

def goleft():
	if player.direction != "right":
		player.direction = "left"

def move():
	if player.direction == "up":
		y = player.ycor()
		player.sety(y+20)
	if player.direction == "down":
		y = player.ycor()
		player.sety(y-20)
	if player.direction == "left":
		x = player.xcor()
		player.setx(x-20)
	if player.direction == "right":
		x = player.xcor()
		player.setx(x+20)

wn.listen()
wn.onkeypress(jump, "Up")
wn.onkeypress(dig, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")

while True:
    wn.update()
    if player.ycor() > 290 or player.ycor() < -290 or player.xcor() <-290 or player.xcor() > 290:
        player.goto(0,0)
        player.direction = "Stop"
    move()
    if player.distance(coin) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270,270)
        coin.goto(x,y)
        delay -= 0.001
        score += 10
        Scoreboard.clear()
        Scoreboard.write("Hello!!!   Your Score : {}".format(
			    score), align="center", font=("candara", 24, "bold"))
wn.mainloop()
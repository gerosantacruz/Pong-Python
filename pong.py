# Pong game by Gero

import turtle
import winsound

wm = turtle.Screen()
wm.title("Pong by Gero")
wm.bgcolor("black")
wm.setup(width=800, height=600)
wm.tracer(0)

#Score 
point_a = 0
point_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

#Score Board 'pen'
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Consolas", 24, "normal"))


# Function
def paddle_a_up():
    if paddle_a.ycor() < 240:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)
    else:
        y = paddle_a.ycor()
        y += 0
        paddle_a.sety(y)


def paddle_a_down():
    if paddle_a.ycor() > -240:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)
    else:
        y = paddle_a.ycor()
        y -= 0
        paddle_a.sety(y)


def paddle_b_up():
    if paddle_b.ycor() < 240:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)
    else:
        y = paddle_b.ycor()
        y += 0
        paddle_b.sety(y)


def paddle_b_down():
    if paddle_b.ycor() > -240:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)
    else:
        y = paddle_b.ycor()
        y -= 0
        paddle_b.sety(y)


# Listener keyboard binding
wm.listen()
wm.onkeypress(paddle_a_up, "w")
wm.onkeypress(paddle_a_down, "s")
wm.onkeypress(paddle_b_up, "Up")
wm.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
    wm.update()

    # Move the ball across the screen
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking for the ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        point_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(point_a, point_b), align="center", font=("Consolas", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1 
        point_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(point_a,point_b), align="center", font=("Consolas", 24, "normal"))


    #Paddle border collision
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    
    

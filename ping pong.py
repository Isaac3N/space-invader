# simple pong in python 3.7 for beginners

import turtle

win = turtle.Screen()
win.title("pong isaac")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#score
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.penup()  
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1 )
#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.penup()  
paddle_b.goto(+350,0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1 )




#Ball
ball= turtle.Turtle()  
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy= -0.2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PLayer 1: 0  player2:0", align= "center", font=("Courier",24, "normal"))
#Functions
def paddle_a_up():
    y= paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y= paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y= paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y= paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)




# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")

win.listen()
win.onkeypress(paddle_a_down, "a")

win.listen()
win.onkeypress(paddle_b_up, "Up")

win.listen()
win.onkeypress(paddle_b_down, "Down")
#Main game loop
while True:
    win.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx )
    ball.sety(ball.ycor()+ ball.dy )
      
#borderchecking
    if ball.ycor()<-290:   
        ball.sety(-290)
        ball.dy *=-1

    if ball.ycor()> 290:   
        ball.sety(290)
        ball.dy *=-1

    if ball.xcor()> 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PLayer 1: {} player2:{}".format(score_a, score_b), align= "center", font=("Courier",24, "normal")) 

    if ball.xcor()< -390: 
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("PLayer 1: {} player2:{}".format(score_a, score_b), align= "center", font=("Courier",24, "normal"))
    # paddle and ball collisions
    if (ball.xcor()>340 and ball.xcor()< 350)and (ball.ycor()< paddle_b.ycor()+40 and ball.ycor()> paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor()<-340 and ball.xcor()>-350)and (ball.ycor()< paddle_a.ycor()+40 and ball.ycor()> paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        


import turtle

########## Graphics setting ##########

#background
wn = turtle.Screen()
wn.title("Game")
wn.bgcolor("black")
wn.setup(width = 800 , height = 600)
wn.tracer()

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize( stretch_wid = 6 , stretch_len = 1)
paddle_a.color("orange")
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize( stretch_wid = 6 , stretch_len = 1)
paddle_b.color("green")
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 5
ball.dy = -5

#score 
score_a = 0
score_b = 0


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Player orange: {}     Player Green: {}".format(score_a,score_b),align = "center" , font = ("courier", 24 , "normal"))

#border
pen1 = turtle.Turtle()
pen1.hideturtle()
pen1.color("white")
pen1.speed(5)
pen1.penup()
pen1.goto(350,300)
pen1.pendown()
pen1.left(180)
pen1.forward(700)
pen1.left(90)
pen1.forward(600)
pen1.left(90)
pen1.forward(700)
pen1.left(90)
pen1.forward(600)

#health points
health_a = 3
health_b = 3


#health bar
pen2 = turtle.Turtle()
pen2.color("white")
pen2.hideturtle()
pen2.penup()
pen2.goto(0,-350)
pen2.write("Health = {}\t\t\t\tHealth = {}".format(health_a,health_b),align = "center", font = ("New Roman",20,"normal"))

########### kinematics ##########

#function
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 240:
        y += 30
        paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 30
        paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 240:
        y += 30
        paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 30
        paddle_b.sety(y)
        
#max_health
def end_game():
    wn.clear()
    wn.bgcolor("black")
    pen.goto(0,0)
    winner = "orange"
    if score_a  == score_b:
        pen.write(" Game Tied", align = "center", font = ("courier",30,"bold"))
        wn.exitonclick()
    if score_a < score_b:
        winner = "Green"
    pen.write("Player {} Won! \nHighscore :{}".format(winner,max(score_a,score_b)), align = "center", font = ("courier",30,"bold"))
    wn.exitonclick()

#keyboard binding
wn.listen()
wn.onkeypress( paddle_a_up , "w")
wn.onkeypress( paddle_a_down , "s")
wn.onkeypress( paddle_b_up , "Up")
wn.onkeypress( paddle_b_down , "Down")

########### Actaul Logic ##########

#main
while True:
    wn.update()
    

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() <  -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 350:
        ball.goto(0,0)
        ball.dx *= -1
        health_b -= 1
        if health_b < 0:
            end_game()
        pen2.clear()
        pen2.write("Health = {}\t\t\t\tHealth = {}".format(health_a,health_b),align = "center", font = ("New Roman",20,"normal"))
        
    if ball.xcor() < -350:
        ball.goto(0,0)
        ball.dx *= -1
        health_a -= 1
        if health_a < 0:
            end_game()
        pen2.clear()
        pen2.write("Health = {}\t\t\t\tHealth = {}".format(health_a,health_b),align = "center", font = ("New Roman",20,"normal"))
        

    
    # collision
    if ball.xcor() > 349 and ball.ycor() < paddle_b.ycor() + 59 and ball.ycor() > paddle_b.ycor() - 59:
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player orange: {}     Player Green: {}".format(score_a,score_b),align = "center" , font = ("courier", 24 , "normal"))
        
    if ball.xcor() < -349 and ball.ycor() < paddle_a.ycor() + 59 and ball.ycor() > paddle_a.ycor() - 59:
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player orange: {}     Player Green: {}".format(score_a,score_b),align = "center" , font = ("courier", 24 , "normal"))
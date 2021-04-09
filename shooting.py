import turtle
import random

## design

# screen
wn = turtle.Screen()
wn.title("shooting game")
wn.bgcolor("black")
wn.setup( width =  800, height =  600)
wn.tracer()

# border
border = turtle.Turtle()
border.hideturtle()
border.speed(10)
border.color("white")
border.penup()
border.goto( -400, -300)
border.pendown()
for i in range (4):
    if i % 2 == 0:
        border.forward(800)
    else:
        border.forward(600)
    border.left(90)

# player
char = turtle.Turtle()
char.speed(0)
char.shape("triangle")
char.setheading(90)
char.shapesize( stretch_wid = 2 , stretch_len = 2)
char.color("orange")
char.penup()
char.goto( 0 , - 280 )

# bullets
bull1 = turtle.Turtle()
bull1.penup()
bull1.speed(0)
bull1.dx = 0
bull1.dy = 10
bull1.bulletstate = "ready"

# health
health = turtle.Turtle()
health.penup()
health.speed(0)
health.shape("circle")
health.color("red")
health.goto(200,100)
health.dy = -2



## kinematics
# function

def char_left():
    left = char.xcor()
    if left > -380:
        left -= 20
        char.setx(left)
def char_right():
    right = char.xcor()
    if right < 380:
        right += 20
        char.setx(right)
def bullets():
    if bull1.bulletstate == "ready":
        bull1.bulletstate = "fired"
        bull1.dy = 10
        x = char.xcor()
        y = char.ycor()
        bull1.goto(x,y)
        bull1.color("white")
        bull1.shape("circle")
def getcor():
    en_x = random.randint(-380,380)
    en_y = random.randint( 100 , 280)
    return en_x , en_y
    
# enemy
en = turtle.Turtle()
en.penup()
en.speed(0)
en.shape("circle")
en.shapesize( stretch_wid = 2 , stretch_len = 2 )
en.color("blue")
en_x,en_y = getcor()
en.goto(en_x ,en_y)

   

## keyboard binding
# binding
wn.listen()
wn.onkeypress( char_left , "Left")
wn.onkeypress( char_right , "Right")
wn.onkeypress( bullets , "Up")
        
        
    








# main
while True:
    wn.update()
    bull1.sety( bull1.ycor() + bull1.dy )
    health.sety( health.ycor() + health.dy )

    if bull1.ycor()> 279:
        bull1.bulletstate = "ready"
        bull1.dy = 0
        bull1.color("black")
    if health.ycor()< -280:
        health.dy = 0
        health.color("black")
        health.goto(1000,1000)

    if char.xcor() == health.xcor() and (char.ycor()+10) == health.ycor():
        health.dy = 0
        health.color("black")
        health.goto(1000,1000)
        
    if en.ycor() == bull1.ycor():
        if en.xcor() == bull1.xcor():
            en.color("black")
            en.clear()

    
        
        
    

#Basic graphic game

import turtle

wn = turtle.Screen()
wn.title("Gamedev")
wn.bgcolor("black")
wn.setup(width = 800, height = 800)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-400,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(400,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)


#main
while True:
	wn.update()



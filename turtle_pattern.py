import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width = 600 , height = 600)
wn.tracer()

pen = turtle.Turtle()
pen.pensize(10)
pen.speed(10)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(-300,-300)

for i in range(4):
	pen.pendown()
	pen.forward(600)
	pen.left(90)
y = -300
for i in range(5):
	y += 100
	pen.penup()	
	pen.goto(-300,y)
	pen.pendown()
	pen.forward(600)
x = -300
pen.left(90)
for i in range (5):
	x += 100
	pen.penup()
	pen.goto(x,-300)
	pen.pendown()
	pen.forward(600)


	
fillpen = turtle.Turtle()
fillpen.color("white")
fillpen.pensize(50)
fillpen.penup()
fillpen.goto(x,y)
fillpen.pendown()
fillpen.forward(100)
	


wn.update()
wn.exitonclick()
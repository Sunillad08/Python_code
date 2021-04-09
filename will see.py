import turtle



# screen setup
wn= turtle.Screen()
wn.bgcolor("black")
wn.setup(400,400)
wn.tracer()

# border
border = turtle.Turtle()
border.color("white")
border.penup()
#border.pensize(50)
border.speed(0)
border.hideturtle()
border.goto(-150,-150)
border.pendown()
for _ in range (4):
    count = 0
    border.forward(300)
    border.left(90)
border.forward(300)
border.left(90)
border.forward(100)
border.left(90)
border.forward(300)
border.right(90)
border.forward(100)
border.right(90)
border.forward(300)
border.left(90)
border.forward(100)
border.left(90)
border.forward(100)
border.left(90)
border.forward(300)
border.right(90)
border.forward(100)
border.right(90)
border.forward(300)












team = True
# main
while True:
    wn.update()
    while team : 
        px = int(input())
        py = int(input())
        border.goto(px,py)
        team = bool(int(input()))
    
    

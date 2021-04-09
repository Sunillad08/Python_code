import turtle as t
wn = t.Screen()
pen = t.Turtle()
pen.speed(100)
for i in range(89):
	pen.pendown()
	
	if i %2 == 0:
		pen.penup()
	pen.forward(100)
	pen.left(89)
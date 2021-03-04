import tkinter as tk
#import webbrowser as wb
import turtle as tr

wn = tk.Tk()
wn.title("Hello Boomer!")
def tur():
	sn = tr.Screen()
	sn.clear()
	sn.title("Drawing")
	sn.setup(500,500)
	sn.bgcolor("black")
	wi = tr.Turtle()
	wi.penup()
	wi.goto(0,0)
	wi.pendown()
	wi.clear()
	wi.speed(0)
	wi.color("white")
	for _ in range(100):
		wi.forward(80)
		wi.right(167)
button = tk.Button(wn , text = "star", width = 20, height = 2 , command = tur, activebackground = "blue", activeforeground = "black")
button.place( x = 250 , y= 1500)
wn.mainloop()

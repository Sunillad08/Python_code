from tkinter import *
from turtle import *
import random

sc = Screen()
sc.bgcolor("black")
def star():
    sc = Screen()
    sc.bgcolor("black")
    pen = Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.color("white")
    pen.penup()
    pen.goto( random.randint(-100,100),random.randint(-100,100))
    pen.pendown()
    for _ in range (5):
        pen.forward(100)
        pen.right(144)
    sc.exitonclick()
def square():
    pen = Turtle()
    pen.speed(0)
    pen.color("white")
    pen.hideturtle()
    pen.penup()
    pen.goto( random.randint(-100,100),random.randint(-100,100))
    pen.pendown()
    for _ in range (4):
        pen.forward(100)
        pen.left(90)
    sc.exitonclick()
def circle():
    pen = Turtle()
    pen.speed(0)
    pen.color("white")
    pen.hideturtle()
    pen.penup()
    pen.goto( random.randint(-100,100),random.randint(-100,100))
    pen.pendown()
    pen.circle(50)
    sc.exitonclick()
def g0t0():
    pen = Turtle()
    pen.speed(0)
    pen.color("white")
    pen.hideturtle()
    pen.goto( random.randint(-100,100),random.randint(-100,100))
def clear0():
    sc.clear()
    sc.bgcolor("black")
def bomb():
    pen = Turtle()
    pen.speed(0)
    pen.color("white")
    pen.hideturtle()
    for _ in range(100):
        pen.goto( random.randint(-100,100),random.randint(-100,100))
        pen.goto(0,0)
    
wn = Tk()
wn.title("Trial")
wn.geometry("300x300")

exitbutton = Button(wn , text = "Exit" , command = wn.destroy)
exitbutton.grid( column = 1 , row = 1)
star = Button(wn , text = "Star" , command = star)
star.grid( column = 1 , row = 2)
square = Button(wn , text = "Square" , command = square)
square.grid( column = 1 , row = 3)
goto = Button(wn , text = "Goto" , command = g0t0)
goto.grid( column = 1, row = 5)
circle = Button(wn , text = "Circle" , command = circle)
circle.grid( column = 1 , row = 4)
explosion = Button(wn , text = "bomb" , command = bomb)
explosion.grid( column = 1 , row = 7)
clear = Button(wn , text = "Clear" , command = clear0)
clear.grid( column = 1 , row = 6)
wn.mainloop()

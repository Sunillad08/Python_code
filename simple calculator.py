from tkinter import *
#from math import sqrt

wn = Tk()
wn.geometry("400x400")
wn.title("Simple Calculator")
global func
func = []


# function
def getin(n):
    display.insert("end" , n)
    func.append(n)

def displayy():
    global func
    try:
        func = "".join(func)
        re = eval(func)
        display.delete( 0 , "end")
        display.insert(0 , re)
    except Exception as e:
        display.delete(0, "end")
        display.insert(0,e)
        func = []
    finally:
        func = list(func)
def allclear():
    global func
    try:
        display.delete(0,"end")
        func = []
    except Exception as e:
        display.delete(0, "end")
        display.insert(0,e)
def clearr():
    global func
    try:
        display.delete(0,"end")
        func.pop()
        func = "".join(func)
        display.insert(0,func)
        func = list(func)
        
    except Exception as e:
        display.delete(0, "end")
        display.insert(0,e)


# screen

display = Entry(wn ,width =63 )

but1 = Button(wn, text = "1" , bg = "black" , fg = "white" , padx = 40 , pady =20 , command = lambda: getin("1"))
but2 = Button(wn, text = "2" , bg = "black" , fg = "white" , padx = 40 , pady =20 , command = lambda: getin("2"))
but3 = Button(wn, text = "3" , bg = "black" , fg = "white" , padx = 40 , pady =20 , command = lambda: getin("3"))
but4 = Button(wn, text = "4" , bg = "black" , fg = "white" , padx = 40 , pady =20 , command = lambda: getin("4"))
but5 = Button(wn, text = "5" , bg = "black" , fg = "white" , padx = 40 , pady =20 , command = lambda: getin("5"))
but6 = Button(wn, text = "6" , bg = "black" , fg = "white" , padx = 40 , pady =20 , command = lambda: getin("6"))
but7 = Button(wn, text = "7" , bg = "black" , fg = "white" , padx = 40 , pady =20 , command = lambda: getin("7"))
but8 = Button(wn, text = "8" , bg = "black" , fg = "white" , padx = 40 , pady =20 , command = lambda: getin("8"))
but9 = Button(wn, text = "9" , bg = "black" , fg = "white" , padx = 40 , pady =20 , command = lambda: getin("9"))
but0 = Button(wn, text = "0" , bg = "black" , fg = "white" , padx = 40 , pady =20 , command = lambda: getin("0"))
butA = Button(wn, text = "+" , bg = "black" , fg = "white" , padx = 40 , pady =20 , command = lambda: getin("+"))
butS = Button(wn, text = "-" , bg = "black" , fg = "white" , padx = 42 , pady =20 , command = lambda: getin("-"))
butM = Button(wn, text = "*" , bg = "black" , fg = "white" , padx = 42 , pady =20 , command = lambda: getin("*"))
butD = Button(wn, text = "/" , bg = "black" , fg = "white", padx = 42 , pady =20 , command = lambda: getin("/"))
butdel = Button(wn, text = "." , bg = "black" , fg = "white" , padx = 42 , pady =20 , command = lambda: getin("."))
butC = Button(wn, text = "C" , bg = "black" , fg = "white" , padx = 39 , pady =20 , command = clearr)
butAC = Button(wn, text = "AC" , bg = "black" , fg = "white", padx = 35 , pady =20, command = allclear)
butE = Button(wn, text = "=" , bg = "black" , fg = "white" , padx = 40 , pady =20 , command = displayy)
butsqrt = Button(wn, text = "sqrt" , bg = "black" , fg = "white" , padx = 35 , pady =20 , command = lambda: getin("**(1/2)"))
# placement

display.grid( row = 1 , column = 1 , columnspan = 4)

but1.grid(row = 2 , column = 1)
but2.grid(row = 2 , column = 2)
but3.grid(row = 2 , column = 3)
butA.grid(row = 2 , column = 4)
but4.grid(row = 3 , column = 1)
but5.grid(row = 3 , column = 2)
but6.grid(row = 3 , column = 3)
butS.grid(row = 3 , column = 4)
but7.grid(row = 4 , column = 1)
but8.grid(row = 4 , column = 2)
but9.grid(row = 4 , column = 3)
butM.grid(row = 4 , column = 4)
butdel.grid(row = 5 , column = 1)
but0.grid(row = 5 , column = 2)
butE.grid(row = 5 , column = 3)
butD.grid(row = 5 , column = 4)
butAC.grid(row = 6 , column = 1)
butC.grid(row =6 , column = 2)
butsqrt.grid(row =6 , column = 3)
wn.mainloop()

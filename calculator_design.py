from tkinter import *

wn = Tk()
wn.title("calculator")
wn.geometry("600x600")
display = Entry(wn)
display.grid( row = 1 , column = 1, columnspan = 9)
fun = []


def press():
	#try:
	display.insert(0 , fun)
	#except Exception as e:
	#	display.configure(text= e)
	
def funn(n):
	fun.append(n)		
 
num1 = Button(wn, text = "1", command = fun.append("1"))
num1.grid( row = 3 , column = 1)

num2= Button(wn , text = "2" ,command = fun.append("2"))
num2.grid( row = 3 , column = 3)

num3 = Button(wn , text = "3",command = fun.append("3") )
num3.grid( row = 3 , column = 5)

num4 = Button(wn , text = "4" ,command = fun.append("4"))
num4.grid( row = 5 , column = 1)

num5 = Button(wn , text = "5" ,command = fun.append("5"))
num5.grid( row = 5 , column = 3)

num6 = Button(wn , text = "6" ,command = fun.append("6"))
num6.grid( row = 5, column = 5)

num7 = Button(wn ,  text = "7",command = fun.append("7") )
num7.grid( row = 7 , column = 1)

num8 = Button(wn , text = "8" ,command = fun.append("8"))
num8.grid( row = 7 , column = 3)

num9= Button(wn , text = "9",command = fun.append("9"))
num9.grid( row = 7 , column = 5)

num0 = Button(wn , text = "0" ,command = fun.append("0"))
num0.grid( row = 9, column = 3)

equal = Button(wn , text = "=",command = press )
equal.grid( row = 9 , column = 5)

plus = Button(wn , text = "+" ,command = fun.append("+"))
plus.grid( row = 9 , column = 9)

minus = Button(wn , text = "-",command = fun.append("-") )
minus.grid( row = 7 , column = 9)

mult = Button(wn , text = "*",command = fun.append("*") )
mult.grid( row = 5, column = 9)

divi = Button(wn , text = "/",command = fun.append("/") )
divi.grid( row = 3 , column = 9)

quit = Button(wn , text = "E" ,command = wn.destroy)
quit.grid( row = 9 , column = 1,)





wn.mainloop()

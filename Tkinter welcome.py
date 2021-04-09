import tkinter as t

wn = t.Tk()
wn.title("Good")
wn.geometry("300x300")

wn1 = t.Tk()
wn1.title("Welcome")
wn1.geometry("300x300")

name = t.Entry(wn,width= 10,text = "Enter name")
name.grid( row = 6 ,column = 3)
def clicked():
	res = name.get()
	n.configure(text = res)
	wn.destroy()


enter = t.Button(wn,text="enter", command = clicked)
enter.grid(row = 6 , column = 5)

n = t.Label(wn1)
n.grid(row= 6 , column = 7)
wn.mainloop()
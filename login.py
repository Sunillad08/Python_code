from tkinter import *
from tkinter import messagebox
import turtle

global login_status

login_status = False
wn = turtle.Screen()
wn.bgcolor("black")

root = Tk()
root.resizable(0,0)
root.title("Login")


#function
def logged():
	global login_status
	name = entry_username.get()
	password = entry_password.get()
	if name == "sunil":
		if password == "sunil1234":
			space3.configure( text = "Logged in Successfully!")
			messagebox.showinfo("Login Info", "Logged in Successfully")
			login_status = True
			pen = turtle.Turtle()
			pen.color("white")
			for _ in range (400):
				pen.forward(100)
				pen.left(59)
	else :
		space3.configure(text = "Wrong mf")
		messagebox.showinfo("Login Info", "Login Failed")
if login_status == True:
	root.destroy()




#widget
space1 = Label (root , text = " ", height = 1)
label_username = Label ( root , text = "Username" , bg = "white" , fg = "black" )
entry_username = Entry( root)
space2 = Label(root, text = " ",height = 1)
label_password = Label(root , text = "Password",bg = "white", fg = "black")
entry_password = Entry(root)
space3 = Label(root , text = " ", height = 1)
button_login= Button ( root , text = " Login", bg = "white" , activeforeground = "blue" ,command = logged)
space4 = Label(root)

#widget setup
space1.grid(row = 1 , column = 1, columnspan = 2)
label_username.grid( row = 2 , column = 1)
entry_username.grid( row = 2 , column = 2)
space2.grid( row = 3 , column = 1 , columnspan = 2)
label_password.grid( row = 4 , column = 1)
entry_password.grid( row = 4 , column = 2)
space3.grid(row = 5 , column = 1 ,columnspan = 2)
button_login.grid(row = 6,column = 1,columnspan=2)
space4.grid(row = 7 , column = 1 , columnspan = 2)




root.mainloop()

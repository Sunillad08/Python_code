from tkinter import *


root = Tk()
root.geometry("300x300")

def save():
	con_name = name.get()
	con_number = phone.get()
	
	if len(con_name) == 0 :
		name.insert(0,"please enter your name : ")
	if len(con_number) == 0:
		phone.insert(0,"please enter 10 digit  phone number:")
	if len(con_name) >0 and len(con_number) == 10:
		v = "\n" + con_name + ' : ' + con_number
		with open("contact number.txt","a+") as f:
			L1.configure( text = "done")
			f.write(v)
			f.close()
		with open("contact number.txt","r") as f:
			 v = f.read()
			 L2.configure(text = v)
			 f.close()

L1 = Label( root , text = "Enter Your 10 digit Phone Number :")
L2 = Label(root, text= "Enter your name : ")
phone = Entry(root , width = 50)
name = Entry(root , width = 50)
savve = Button(root , text = "save" , command =  save)
exit = Button(root , text = "Exit", command = root.destroy)


L2.grid(row = 1 , column = 1 ,columnspan = 3 , rowspan = 4)
name.grid(row = 5 , column = 1 , columnspan = 3)
L1.grid(row= 6 , column = 1 ,columnspan = 3)
phone.grid( row = 7, column = 1 , columnspan = 3)
savve.grid(row = 8 , column = 2)
exit.grid(row = 9, column = 2)

root.mainloop()
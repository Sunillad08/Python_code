import turtle as tu
import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
global flag
flag = 1
#define function 
def drawing():
	global flag
	s1 = side1.get() 
	s2 = side2.get()
	s3 = side3.get()
	if len(s1)== 0 or s1 == "Enter value!":
		side1.delete(0 , "end")
		side1.insert(0, "Enter value!")
		flag = 0
	if  len(s2)==0 or s2 == "Enter value!" :
		side2.delete(0,"end")
		side2.insert(0,"Enter value!")
		flag = 0
	if len(s3)==0 or s3 == "Enter value!":
		side3.delete(0,"end")
		side3.insert(0, "Enter value!")
		flag=0
	if flag ==1:
		
		wn = tu.Screen()
		pen = tu.Turtle()
		pen.speed(0)
		for _ in range(100):
			pen.forward(100)
			pen.left(132)
		 	



side1 =  tk.Entry(root)
side2 = tk.Entry(root)
side3 = tk.Entry(root)
ok = tk.Button(root , text = 'save', command = drawing)
side1.pack()
side2.pack()
side3.pack()
ok.pack()






root.mainloop()
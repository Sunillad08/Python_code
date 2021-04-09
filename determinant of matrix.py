import numpy as np
import tkinter as tk


wn = tk.Tk()
wn.title("Matrix")
global b
b = []

def determinant():
    global b
    b.append(a11.get())
    b.append(a12.get())
    b.append(a13.get())
    b.append(a21.get())
    b.append(a22.get())
    b.append(a23.get())
    b.append(a31.get())
    b.append(a32.get())
    b.append(a33.get())
    c = np.array(b)
    c = c.reshape(3,3)
    d  = np.linalg.det(c)
    ans.configure(text = d)
    b.clear()
    
            



a11 = tk.Entry(wn,width = 10)
a12 = tk.Entry(wn,width = 10)
a13 = tk.Entry(wn,width = 10)
a21 = tk.Entry(wn,width = 10)
a22 = tk.Entry(wn,width = 10)
a23 = tk.Entry(wn,width = 10)
a31 = tk.Entry(wn,width = 10)
a32 = tk.Entry(wn,width = 10)
a33 = tk.Entry(wn,width = 10)

a11.grid(row = 1,column = 3)
a12.grid(row = 1,column = 4)
a13.grid(row = 1,column = 5)
a21.grid(row = 2,column = 3) 
a22.grid(row = 2,column = 4) 
a23.grid(row = 2,column = 5) 
a31.grid(row = 3,column = 3) 
a32.grid(row = 3,column = 4) 
a33.grid(row = 3,column = 5) 

a = tk.Label(wn,text = "|A|")
a.grid(row = 1 , column = 1 , rowspan = 3)
o1 = tk.Label(wn,text = "=")
o1.grid(row = 1 , column = 2 , rowspan = 3)
o2 = tk.Label(wn,text = "=")
o2.grid(row = 1 , column = 7 , rowspan = 3)
calculate = tk.Button(wn,text = "Calculate" , command = determinant)
calculate.grid(row = 4 , column = 1 , columnspan = 8)
ans = tk.Label(wn,text = " ")
ans.grid(row = 1 , column = 8 , rowspan = 3)
wn.mainloop()

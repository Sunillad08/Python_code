from tkinter import *
from tkinter import messagebox

def getbmi():
	h = height.get()
	w = weight.get()
	try:
		h = float(h)
		w=float(w)
		h = 0.02540000002590 * h
	except:
		bmi.configure(text = "Invalid")
	else :
		b = w / (h**2)
		b = round (b , 2)
		bmi.configure(text = b)
		if b < 18.5 :
			n = "underweight"
		elif b < 24.9:
			n = "normal"
		elif b < 29.9 :
			n = "overweight"
		else :
			n = "obese"
		wei.configure(text = n)
	
wn = Tk()

height = Entry(wn)
weight = Entry(wn)
bmi = Label(wn)
wei = Label(wn)
save = Button(wn ,text= "BMI" ,command = getbmi)

weight.pack()
height.pack()
save.pack()
bmi.pack()
wei.pack()

wn.mainloop()

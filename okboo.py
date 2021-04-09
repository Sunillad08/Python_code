from tkinter.ttk import *
from tkinter import *

#screen setup
root = Tk()
root.title("Boomer")
root.geometry("300x300")
wn = Tk()
wn.title("Boomer")
wn.geometry("300x300")
def clicked():
    combo = Combobox(wn)
    combo["values"] = (1,2,3,4,5,"text")
    combo.current(3)
    combo.pack()

def ok():
    
    chk = BooleanVar()
    chk.set(True)
    ch = Checkbutton(wn,text = "select" ,var = chk)
    ch.pack()
but1 = Button(root,text="clickewe",command = clicked)
but2 = Button(root,text="ok",command = ok) 
but1.pack()
but2.pack()



root.mainloop()

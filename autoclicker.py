import pyautogui
import tkinter as tk
from tkinter import messagebox
import time


wn = tk.Tk()
wn.title("Auto clicker")
global i,n
i = 0
n = 0
def clicker():
    global n
    n = clickes_demand.get()
    try:
        n = int(n)
    except:
        messagebox.showerror("Error", "Enter number only!")
    time.sleep(5)
    for i in range (n):
        pyautogui.click()
        test()
        #time.sleep(10)
def exit():
    wn.destroy()
    
def test():
    global i,n
    i += 1
    clickes_count.configure(text = str(i)+ "/" +str(n))

wn.listen()
wn.onkeypress(exit,"q")

no_of_clickes = tk.Label(wn , text = "No of clicks :" )
clickes_demand = tk.Entry(wn)
clickes_counter = tk.Label(wn , text = "Clicks :")
clickes_count = tk.Label(wn , text = "")
Test_buttton = tk.Button(wn , text = "Test Button", command  = test)
start = tk.Button(wn , text = "Start" , command = clicker)
exit_button = tk.Button(wn , text = "End" , command = exit )

no_of_clickes.grid(row = 0 , column = 0)
clickes_demand.grid(row = 0 , column = 1)
clickes_counter.grid(row = 1 , column = 0)
clickes_count.grid(row = 1 , column = 1)
Test_buttton.grid(row = 2 , column = 0)
start.grid(row = 2 , column = 1)
exit_button.grid(row = 3 , column = 1)

wn.mainloop()

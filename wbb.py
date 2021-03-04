import webbrowser as wb
import pyautogui as pyy
import time as t
import tkinter as tk
##while True:
##    x , y = pyy.position()
##    print(x,y) #341,93 #230,270# input()
global status,wn
status = False

def search_word():
    global status,wn,topic
    topic = search_bar.get()
    status = True
    start()
    wn.destroy()

def start():
    global topic
    wb.open('https://www.youtube.com/')
    t.sleep(5)
    pyy.click(341,93)
    for i in topic:
        pyy.press(i)
    pyy.press("enter")
    t.sleep(5)
    pyy.click(230,270)
    t.sleep(3)
    pyy.press("f")
    
if not status:
    wn = tk.Tk()
    search_bar = tk.Entry(wn)
    search = tk.Button(wn , text = "Search" , command = search_word , padx = 40 )
    search_bar.pack()
    search.pack()
    wn.mainloop()

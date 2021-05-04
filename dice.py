import random
import tkinter as tk
import time

# creating window
wn = tk.Tk()
wn.title("Roll a Dice!")
wn.geometry("400x400")
#wn.resizable(0,0)

# possible outcomes
outcomes = [1,2,3,4,5,6]
# designes
designs = ["""   \n • \n   """,
"""•  \n   \n  •""",
"""•  \n • \n  •""",
"""• •\n   \n• •""",
"""• •\n • \n• •""",
"""•••\n   \n•••"""]

def animation():
    global outcomes , designs
    for i in range(100):
        output = random.choice(outcomes)
        label_outcome.config(text=f"{designs[output-1]}", font = ("Times New Roman" , 50))
 

# roll_dice() : sets up text according to outcome
def roll_dice():
    global outcomes , designs
    animation()
    output = random.choice(outcomes)
    label_outcome.config(text=f"{designs[output-1]}", font = ("Times New Roman" , 50))
 
# creating widgets
header = tk.Label(wn , text = "Roll a Dice!" , height = 2 , bg = "white" , font = ("Times New Roman" , 20))
label_outcome = tk.Label(text = " " , height = 2 , bg = "white" , font = ("Times New Roman" , 20))
roll_button = tk.Button(wn,text = "Roll the die!" , command = roll_dice , height = 2 , bg = "white" , font = ("Times New Roman" , 20))

# set up weight
for i in range(3):
    tk.Grid.rowconfigure(wn,i,weight=1)
    tk.Grid.columnconfigure(wn,i,weight=1)

# place widgets
header.grid(row=0,column=0,columnspan=3,sticky="NESW")
label_outcome.grid(row=1,column=0 , columnspan=3,sticky="NESW")
roll_button.grid(row=2,column=0 , columnspan=3,sticky="NESW")

wn.mainloop()
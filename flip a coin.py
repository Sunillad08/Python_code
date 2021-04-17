import random
import tkinter as tk

# creating window
wn = tk.Tk()
wn.resizable(0,0)
wn.title("Flip a coin!")

# possible outcomes
outcomes = ["Heads" , "Tails"]

# assigning images
head = tk.PhotoImage(file=r"C:\Users\DELL\Documents\python programs\photos\coins\heads.png")
tail = tk.PhotoImage(file=r"C:\Users\DELL\Documents\python programs\photos\coins\tails.png")
wait = tk.PhotoImage(file=r"C:\Users\DELL\Documents\python programs\photos\coins\wait.png")


# flip_coin() : sets up images on canvas according to outcome
def flip_coin():
    canvas.delete()
    global outcomes , head , tail , wait
    canvas.create_image(200,140,anchor=tk.CENTER ,image=wait)
    output = random.choice(outcomes)
    if output == "Heads":
        canvas.create_image(200,140,anchor=tk.CENTER ,image=head)
    else:
        canvas.create_image(200,140,anchor=tk.CENTER ,image=tail)
    label_outcome.config(text = f"{output}")
    
# creating widgets
header = tk.Label(wn , text = "Flip a coin !" , height = 2 , bg = "white" , font = ("Times New Roman" , 20))
canvas = tk.Canvas(wn , bg="white")
label_outcome = tk.Label(text = " " , height = 1 , bg = "white" , font = ("Times New Roman" , 20))
flip_button = tk.Button(wn,text = "Flip a coin" , command = flip_coin , height = 2 , bg = "white" , font = ("Times New Roman" , 20))
canvas.create_image(200,140,anchor=tk.CENTER ,image=wait)

# set up weight
for i in range(3):
    tk.Grid.rowconfigure(wn,i,weight=1)
    tk.Grid.columnconfigure(wn,i,weight=1)

# place widgets
header.grid(row=0,column=0,columnspan=3,sticky="NESW")
canvas.grid(row=1,column=0,columnspan = 3,sticky="NESW")
label_outcome.grid(row=2,column=0 , columnspan=3,sticky="NESW")
flip_button.grid(row=3,column=0 , columnspan=3,sticky="NESW")

wn.mainloop()
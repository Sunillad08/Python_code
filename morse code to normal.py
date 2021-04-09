from tkinter import *
from tkinter import messagebox


## Design
wn = Tk()
wn.title("Converter")
wn.geometry("370x110")
wn.resizable(0,0)


## Declaration
global choice_num , morse_code , english_alpha
choice_num = -1
morse_code = [".−" ,"−...", "−.−.","−..",".","..−.","−−.","....","..",".−−−","−.−",".−..","−−","−.","−−−",".−−.",	
"−−.−",".−.","...","−","..−","...−",".−−","−..−","−.−−","−−.."," "]
english_alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]


## Calculation
def check_state(num):
    global choice_num
    if num == 0:
        choice_num = 0
    elif num == 1:
        choice_num = 1
def convert():
    global choice_num , morse_code , english_alpha
    if choice_num == -1:
        messagebox.showerror( "Conversion Error" , "Choose option to convert!")
    
    elif choice_num == 1:
        if len(input_num.get()) == 0:
            messagebox.showerror("Value Error" , "Enter a sentence!")
        else:
            eng_sen = list(str(input_num.get()).lower())
            morse_co = []
            for i in eng_sen :
                try:
                    n = english_alpha.index(i)
                except:
                    messagebox.showerror("Value Error" , "Enter Only English Word!")
                    break
                else:
                    morse_co.append(morse_code[n])
            morse_co = " ".join(morse_co)
            output_num.delete(0, "end")
            output_num.insert(0,morse_co)
            

    elif choice_num == 0:
        if len(input_num.get()) == 0:
            messagebox.showerror("Value Error" , "Enter a sentence!")
        else:
            morse_co = list(str(input_num.get()).split(" "))
##            morse_co =  []
##            morse_coder = list(str(input_num.get()))
##            for i in range (len(morse_coder)) :
##                if morse_coder[i] == " ":
##                    morse_co.append("".join(morse_coder[0:i]))
##                    morse_coder = morse_coder[i::]
            eng_sen = []
            for i in morse_co :
                try:
                    n = morse_code.index(i)
                except:
                    messagebox.showerror("Value Error" , "Enter Only Morse Code!")
                    break
                else:
                    eng_sen.append(english_alpha[n])
            eng_sen = "".join(eng_sen)
            output_num.delete(0, "end")
            output_num.insert(0,eng_sen)


## Componenets
calculate = Button(wn , text = "Convert" , command = convert)
input_label = Label(wn , text = "Enter value :" , width = 25)
output_label = Label(wn , text = "Converted answer :" , width = 25)
input_num = Entry(wn , width =25) 
output_num = Entry(wn , width = 25)
choice_1 = Button(wn, text="Morse Code to English",padx = 30 , command = lambda : check_state(0))
choice_2 = Button(wn, text="English to Morse Code",padx = 30 , command = lambda : check_state(1))


## Placement
input_label.grid( row = 2 , column =0)
output_label.grid(row = 3 , column =0)
input_num.grid(row = 2 , column = 1 )
output_num.grid(row = 3 ,column = 1 ,rowspan = 3 )
calculate.grid(row = 9 ,column = 0 ,columnspan = 2)
choice_1.grid( row = 0 , column =1 )
choice_2.grid( row = 0 , column =0 )
wn.mainloop()

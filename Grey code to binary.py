from tkinter import *
from tkinter import messagebox

wn = Tk()
wn.title("Converter")
wn.geometry("370x110")
wn.resizable(0,0)

global choice_num
choice_num = -1

def check_state(num):
    global choice_num
    if num == 0:
        choice_num = 0
    elif num == 1:
        choice_num = 1
def convert():
    global choice_num
    if choice_num == -1:
        messagebox.showerror( "Conversion Error" , "Choose option to convert !")
    
    elif choice_num == 1:
        if len(input_num.get()) == 0:
            messagebox.showerror("Value Error" , "Enter a value!")
        binary = list( "0" + input_num.get() )
        if binary.count("1") + binary.count("0") < len(binary):
            messagebox.showerror("Value Error" , "Enter Binary code only!")
        else:
            grey = []
            for i in range(len(binary)-1):
                temp = binary[len(binary)-2::]
                if temp[1] == temp[0]:
                    grey.append(str(0))
                else:
                    grey.append(str(1))
                binary = binary[:len(binary)-1]
            output_num.configure(text = "".join(grey[::-1]))

    elif choice_num == 0:
        if len(input_num.get()) == 0:
            messagebox.showerror("Value Error" , "Enter a value!")
        grey = input_num.get()
        if grey.count("1") + grey.count("0") < len(grey):
            messagebox.showerror("Value Error" , "Enter Grey code only!")
        else:
            binary =[]
            flag = 0
            for i in range (len(grey)):
                if flag == 0:
                    temp = grey[i]
                    binary.append(grey[i])
                    flag = 1
                else:
                    if temp == grey[i]:
                        temp = str(0)
                    else:
                        temp = "1"
                    binary.append(str(temp))
            output_num.configure(text = "".join(binary))
        
    


calculate = Button(wn , text = "Convert" , command = convert)
input_label = Label(wn , text = "Enter value :" , width = 25)
output_label = Label(wn , text = "Converted answer :" , width = 25)
input_num = Entry(wn , width =25) 
output_num = Label(wn , width = 25)
choice_1 = Button(wn, text="Grey code to Binary",padx = 30 , command = lambda : check_state(0))
choice_2 = Button(wn, text="Binary to Gray code",padx = 30 , command = lambda : check_state(1))

input_label.grid( row = 2 , column =0)
output_label.grid(row = 3 , column =0)
input_num.grid(row = 2 , column = 1 )
output_num.grid(row = 3 ,column = 1 )
calculate.grid(row = 7 ,column = 0 ,columnspan = 2)
choice_1.grid( row = 0 , column =1 )
choice_2.grid( row = 0 , column =0 )
wn.mainloop()

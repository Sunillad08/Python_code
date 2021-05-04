import tkinter as tk
import math

# created window
wn = tk.Tk()
wn.title("Scientific Calculator")
wn.config(bg = "black")

# calculator class : contains all possible operations
class calculator:

    # stated calculator
    def __init__(self):
        self.last_answer = "0"
        self.queries = []
        self.current_index = len(self.queries) - 1
        self.output = ""
        self.panel_status = 0

    # get_input : takes input as argument and adds it to display
    def get_input(self , i):
        Entry_input.insert("end" , i)

    # get_output_ready : replaces all conventional symbols with there python alternatives
    def get_output_ready(self):
        self.output = self.output.replace("x","*")
        self.output = self.output.replace("÷","/")
        self.output = self.output.replace("√","math.sqrt")
        self.output = self.output.replace("π","math.pi")
        self.output = self.output.replace("sin","math.sin")
        self.output = self.output.replace("math.sin-1","math.asin")
        self.output = self.output.replace("cos","math.cos")
        self.output = self.output.replace("math.cos-1","math.acos")
        self.output = self.output.replace("tan","math.tan")
        self.output = self.output.replace("math.tan-1","math.atan")
        self.output = self.output.replace("^","**")
        self.output = self.output.replace("log","math.log10")
        self.output = self.output.replace("ln","math.log")
        self.output = self.output.replace("rad","math.radians")
        self.output = self.output.replace("e","math.e")
        self.output = self.output.replace("dmath.eg","math.degrees")

    # get_answer : calculates and shows answer in input box
    def get_answer(self , event = None):
        self.output = str(Entry_input.get())
        self.queries.append(self.output)
        self.get_output_ready()
        try:
            answer = eval(self.output)
            answer = round(answer , 8)
        except SyntaxError:
            answer = "Syntax Error!"
        except Exception as message:
            print(message)
            answer = "Mathematical error"

        self.last_answer = answer # store last answer
        self.current_index = len(self.queries) # adds current operation in history
        self.clear_all() # clears display
        Entry_input.insert(0 , answer) # shows answer in input box

    # clear : clear deletes one element , works as backspace
    def clear(self):
        temp = Entry_input.get()
        self.clear_all()
        temp = temp[0:-1]
        Entry_input.insert(0,temp)

    # clear_all : clears everything on screen
    def clear_all(self):
        Entry_input.delete(0,"end")

    # get_last_answer : returns answer of last performed calculation
    def get_last_answer(self):
        return str(self.last_answer)
    
    # up_arrow : basically scroll up , shows last performed operation on screen
    def up_arrow(self):
        self.current_index -= 1
        Button_down["state"] = tk.NORMAL # make button clickable
        Button_up["state"] = tk.NORMAL
        if self.current_index < 0:
            self.current_index += 1
            Button_up["state"] = tk.DISABLED
        else:
            self.clear_all()
            Entry_input.insert(0 , self.queries[self.current_index])

    # down_arrow : basically scroll down , shows next performed operation on screen
    def down_arrow(self):
        self.current_index += 1
        Button_up["state"] = tk.NORMAL
        Button_down["state"] = tk.NORMAL
        if self.current_index >= len(self.queries):
            self.current_index -= 1
            Button_down["state"] = tk.DISABLED # make buttons disabled
        else:
            self.clear_all()
            Entry_input.insert(0 , self.queries[self.current_index])

    # open_advance_frame : opens advance calculation frame   
    def open_advance_frame(self):
        lower_frame.grid_forget()
        advance_frame.grid(row = 1 , column = 0)

    # open_lower_frame : closes advance frame and opens main frame again
    def open_lower_frame(self):
        advance_frame.grid_forget()
        lower_frame.grid(row = 1 , column = 0)

    # full_open : shows both basic and advance operation on screen 
    def full_open(self):
        if self.panel_status == 0:
            Button_Full_open["text"] = "Close"
            advance_frame.grid(row = 1, column = 1)
            self.panel_status = 1
            Entry_input["width"] = 110
            upper_frame.grid(row = 0 , column = 0 , columnspan = 2)
            Button_lower_frame["state"] = tk.DISABLED
            Button_advance_frame["state"] = tk.DISABLED
        else:
            Button_lower_frame["state"] = tk.NORMAL
            Button_advance_frame["state"] = tk.NORMAL
            Entry_input["width"] = 60
            upper_frame.grid(row = 0 , column = 0)
            self.panel_status = 0
            Button_Full_open["text"] = "Advance"
            advance_frame.grid_forget()
        
# creates calculator
operation = calculator()

# set up frames 
upper_frame = tk.Frame(wn , bg = "black")
lower_frame = tk.Frame(wn , padx = 10 , pady = 10 , bg = "black")
advance_frame = tk.Frame(wn , bg = "black")

upper_frame.grid(row = 0 , column = 0)
lower_frame.grid(row = 1 , column = 0)

# comman values for design
pady_value = 20
padx_value = 40
border_width = 8
button_color = "#D1D0CE"
font_configuration = ("",15)

## widgets for upper frame
'''Upper frame is frame where we see input and answer , we can scroll through history too!''' 
# input box
Entry_input = tk.Entry(upper_frame , width = 60 , borderwidth = 10 , font = (40))

# arrows so scroll through history
Button_up = tk.Button(upper_frame , text = '/\\', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = operation.up_arrow , font = font_configuration)
Button_down = tk.Button(upper_frame , text = '\\/', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color , command = operation.down_arrow , font = font_configuration)

# setting up everything on frame
Entry_input.grid(row = 1 , column = 1, rowspan = 2, pady = 0 , ipady = 30, sticky = tk.NSEW)
Button_up.grid(row = 1 , column = 2, ipady = 10, sticky = tk.NSEW)
Button_down.grid(row = 2 , column = 2, ipady = 10, sticky = tk.NSEW )


## widgets for advance frame 
'''Buttons and there name'''
# pi
Button_pi = tk.Button(advance_frame , text = 'π', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('π') , font = font_configuration)
# sin
Button_sin = tk.Button(advance_frame , text = 'sin', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('sin(') , font = font_configuration)
# cos
Button_cos = tk.Button(advance_frame , text = 'cos', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('cos(') , font = font_configuration)
# tan
Button_tan = tk.Button(advance_frame , text = 'tan', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('tan(') , font = font_configuration)
# e
Button_e = tk.Button(advance_frame , text = 'e', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('e') , font = font_configuration)
# sin inverse
Button_asin = tk.Button(advance_frame , text = 'sin-1', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('sin-1(') , font = font_configuration)
# cos inverse
Button_acos = tk.Button(advance_frame , text = 'cos-1', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('cos-1(') , font = font_configuration)
# tan inverse
Button_atan = tk.Button(advance_frame , text = 'tan-1', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('tan-1(') , font = font_configuration)
# degree to radian conversion
Button_degree = tk.Button(advance_frame , text = 'deg', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('deg(') , font = font_configuration)
# degree to radian conversion
Button_radians = tk.Button(advance_frame , text = 'rad', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('rad(') , font = font_configuration)
# square root
Button_sqrt = tk.Button(advance_frame , text = '√', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input("√(") , font = font_configuration)
# raised to 
Button_raised_to = tk.Button(advance_frame , text = '^', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('^') , font = font_configuration)
# absolute value
Button_abs = tk.Button(advance_frame , text = 'abs', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('abs(') , font = font_configuration)
# to open basic operation panel
Button_lower_frame = tk.Button(advance_frame , text = '>', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = operation.open_lower_frame , font = font_configuration)
# ln , log to base e
Button_ln = tk.Button(advance_frame , text = 'ln', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('ln(') , font = font_configuration)
# log to base 10
Button_log = tk.Button(advance_frame , text = 'log', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('log(') , font = font_configuration)

## putting every thing on grid 
'''row numbers are given in comment followed by columns numbers in ascending order'''
# row 0
Button_pi.grid(row = 0 , column = 0, sticky = tk.NSEW)
Button_sin.grid(row = 0 , column = 1, sticky = tk.NSEW)
Button_cos.grid(row = 0 , column = 2, sticky = tk.NSEW)
Button_tan.grid(row = 0 , column = 3, sticky = tk.NSEW)

# row 1
Button_e.grid(row = 1 , column = 0, sticky = tk.NSEW)
Button_asin.grid(row = 1 , column = 1, sticky = tk.NSEW)
Button_acos.grid(row = 1 , column = 2, sticky = tk.NSEW)
Button_atan.grid(row = 1 , column = 3, sticky = tk.NSEW)
# row 2
Button_degree.grid(row = 2 , column = 0, sticky = tk.NSEW)
Button_radians.grid(row = 2 , column = 1, sticky = tk.NSEW)
Button_ln.grid(row = 2 , column = 2, sticky = tk.NSEW)
Button_log.grid(row = 2 , column = 3, sticky = tk.NSEW)

# row 3
Button_sqrt.grid(row = 4 , column = 0, sticky = tk.NSEW)
Button_raised_to.grid(row = 4 , column = 1, sticky = tk.NSEW)
Button_abs.grid(row = 4 , column = 2, sticky = tk.NSEW)
Button_lower_frame.grid(row = 4 , column = 3, sticky = tk.NSEW)


## widgets for lower frame
'''can use for loop for number buttons but we need to add unique command with every button inside lambda function so gone for writing line for each'''
# 1
Button_1 = tk.Button(lower_frame , text = '1', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('1')  , font = font_configuration)
# 2
Button_2 = tk.Button(lower_frame , text = '2', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('2')  , font = font_configuration)
# 3
Button_3 = tk.Button(lower_frame , text = '3', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('3')  , font = font_configuration)
# 4
Button_4 = tk.Button(lower_frame , text = '4', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('4')  , font = font_configuration)
# 5
Button_5 = tk.Button(lower_frame , text = '5', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('5')  , font = font_configuration)
# 6
Button_6 = tk.Button(lower_frame , text = '6', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('6')  , font = font_configuration)
# 7
Button_7 = tk.Button(lower_frame , text = '7', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('7')  , font = font_configuration)
# 8
Button_8 = tk.Button(lower_frame , text = '8', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('8')  , font = font_configuration)
# 9
Button_9 = tk.Button(lower_frame , text = '9', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('9')  , font = font_configuration)
# 0
Button_0 = tk.Button(lower_frame , text = '0', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('0')  , font = font_configuration)
# . / decimal
Button_dot = tk.Button(lower_frame , text = '.', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('.')  , font = font_configuration)
# = / to get answer
Button_answer = tk.Button(lower_frame , text = '=', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = operation.get_answer , font = font_configuration)
# + / addition
Button_add = tk.Button(lower_frame , text = '+', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('+')  , font = font_configuration)
# - / subtraction
Button_sub = tk.Button(lower_frame , text = '-', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('-')  , font = font_configuration)
# x / multiplication
Button_mult = tk.Button(lower_frame , text = 'X', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('x')  , font = font_configuration)
# ÷ / division
Button_div = tk.Button(lower_frame , text = '÷', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input('÷')  , font = font_configuration)
# clear one character
Button_clear = tk.Button(lower_frame , text = 'DEL', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = operation.clear , font = font_configuration )
# clear everything
Button_clear_all = tk.Button(lower_frame , text = 'AC', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = operation.clear_all , font = font_configuration)
# open both basic as well as advance panel
Button_Full_open = tk.Button(lower_frame , text = 'Advance', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = operation.full_open , font = font_configuration)
# ( , open quotes
Button_open_quote = tk.Button(lower_frame , text = '(', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input("(") , font = font_configuration)
#  ) , close quotes
Button_close_quote = tk.Button(lower_frame , text = ')', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input(")") , font = font_configuration)
# Ans , gives answer of last question
Button_ans = tk.Button(lower_frame , text = 'Ans', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input(operation.get_last_answer()) , font = font_configuration)
# into 10 raise to something
Button_10_times = tk.Button(lower_frame , text = 'x10^', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = lambda : operation.get_input("x10^") , font = font_configuration)
# button to open sole advance frame
Button_advance_frame = tk.Button(lower_frame , text = '<', padx = padx_value , pady = pady_value ,bd = border_width, bg = button_color ,  command = operation.open_advance_frame , font = font_configuration)


## putting every thing on grid 
'''row numbers are given in comment followed by columns numbers in ascending order'''

# row 0
Button_7.grid(row = 0 , column = 0, sticky = tk.NSEW)
Button_8.grid(row = 0 , column = 1, sticky = tk.NSEW)
Button_9.grid(row = 0 , column = 2, sticky = tk.NSEW)
Button_clear.grid(row = 0 , column = 3, sticky = tk.NSEW)
Button_clear_all.grid(row = 0 , column = 4, sticky = tk.NSEW)
Button_open_quote.grid(row = 0 , column = 5, sticky = tk.NSEW)

# row 1
Button_4.grid(row = 1 , column = 0, sticky = tk.NSEW)
Button_5.grid(row = 1 , column = 1, sticky = tk.NSEW)
Button_6.grid(row = 1 , column = 2, sticky = tk.NSEW)
Button_mult.grid(row = 1 , column = 3, sticky = tk.NSEW)
Button_div.grid(row = 1 , column = 4, sticky = tk.NSEW)
Button_close_quote.grid(row = 1 , column = 5, sticky = tk.NSEW)

# row 2
Button_1.grid(row = 2 , column = 0, sticky = tk.NSEW)
Button_2.grid(row = 2 , column = 1, sticky = tk.NSEW)
Button_3.grid(row = 2 , column = 2, sticky = tk.NSEW)
Button_add.grid(row = 2 , column = 3, sticky = tk.NSEW)
Button_sub.grid(row = 2 , column = 4, sticky = tk.NSEW)
Button_Full_open.grid(row = 2 , column = 5, sticky = tk.NSEW)

# row 3
Button_0.grid(row = 3 , column = 0, sticky = tk.NSEW)
Button_dot.grid(row = 3 , column = 1, sticky = tk.NSEW)
Button_10_times.grid(row = 3 , column = 2, sticky = tk.NSEW)
Button_ans.grid(row = 3 , column = 3, sticky = tk.NSEW)
Button_answer.grid(row = 3 , column = 4, sticky = tk.NSEW)
Button_advance_frame.grid(row = 3 , column = 5, sticky = tk.NSEW)

# adding weight to every widget in wn window
# wn
for i in range(2):
    tk.Grid.rowconfigure(upper_frame , i , weight = 1)
for i in range(2):
    tk.Grid.columnconfigure(upper_frame , i , weight = 1)

# upper frame
for i in range(2):
    tk.Grid.rowconfigure(upper_frame , i , weight = 1)
for i in range(2):
    tk.Grid.columnconfigure(upper_frame , i , weight = 1)

# advance frame
for i in range(3):
    tk.Grid.rowconfigure(advance_frame , i , weight = 1)
for i in range(4):
    tk.Grid.columnconfigure(advance_frame , i , weight = 1)

# lower frame
for i in range(4):
    tk.Grid.rowconfigure(lower_frame , i , weight = 1)
for i in range(6):
    tk.Grid.columnconfigure(lower_frame , i , weight = 1)

wn.mainloop()
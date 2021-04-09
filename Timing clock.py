import tkinter as tk
from tkinter import messagebox

wn = tk.Tk()


def timeInWords(h, m):
    naming_time = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
    naming_session = ["one minute","two minutes","three minutes","four minutes","five minutes","six minutes","seven minutes","eight minutes","nine minutes",
"ten minutes","eleven minutes","twelve minutes","thirteen minutes","fourteen minutes","quarter", "sixteen minutes","seventeen minutes", "eighteen minutes",
"nineteen minutes","twenty minutes","twenty one minutes","twenty two minutes","twenty three minutes","twenty four minutes","twenty five minutes",
"twenty six minutes","twenty seven minutes","twenty eight minutes","twenty nine minutes"]
    if m == 0:
        return (naming_time[h-1] + " o' clock")
    elif m < 30:
        return (naming_session[m-1] + " past " + naming_time[h-1])
    elif m > 30:
        m = 60 - m
        return (naming_session[m-1] + " to " + naming_time[h])
    else:
        return ("half past " + naming_time[h-1])    
    
time_entry = tk.Entry(wn)
output_label = tk.Label(wn, text = " " , ) 


h , m = map(int, input().split(":"))

result = timeInWords(h, m)

print(result + '\n')

wn.mainloop()
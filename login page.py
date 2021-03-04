from tkinter import *
from tkinter import messagebox

wn = Tk()
wn.title("Login Page")
wn.geometry("280x150")
wn.resizable(0,0)

username_list = ["sunil1" , "sunil2" , "sunil3" ]
password_list = [ "sunil1" , "sunil2" , "sunil3" ]

def login_fun():
    global username_list , password_list
    username = username_entry.get()
    password = password_entry.get()
    if len(username) == 0 or len(password) == 0:
        messagebox.showwarning("Warning" , "Enter all Credentials")
    elif username in username_list:
        n = username_list.index(username)
        if password_list[n] == password:
            error.configure(text = "Login Successfull!")
        else:
            error.configure(text = "Invalid credentials!")
    else:
        error.configure(text = "Invalid credentials!")


logo = Label( wn , text = "HackerRank" , font = (40))
error = Label( wn , text = "Enter Username and Password")
username_label = Label( wn , text = "Username" , padx = 40)
password_label = Label ( wn , text = "Password" , padx = 40)
username_entry = Entry( wn )
password_entry = Entry ( wn )
Login_button = Button( wn , text = "Login" , padx = 40 , command = login_fun )


logo.grid(row = 0 , column = 1 , columnspan = 2)
error.grid(row = 1 , column = 1 , columnspan = 2)
username_label.grid( row = 2 , column = 1 )
username_entry.grid( row = 2 , column = 2 )
password_label.grid( row = 3 , column = 1 )
password_entry.grid( row = 3 , column = 2 )
Login_button.grid(row = 4 , column = 1 , columnspan = 2)

wn.mainloop()

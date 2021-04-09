from random import shuffle
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as tkk

global player_list , name_list , status , score1,score2,score3,score4,getnamess , player1 , player2 , player3, player4
player_list = [1,2,3,4]
name_list = ["King","Queen","Police","Thief"]
status = False
getnamess = True
score1,score2,score3,score4 = 0,0,0,0

## def functions
# get names
def getnames():
    global gatenamess , player1 ,player2 ,player3 ,player4 ,namelist
    savecheck = False
    count = 0
    player1 = play1.get()
    player2 = play2.get()
    player3 = play3.get()
    player4 = play4.get()
    namelist = [ player1 , player2 ,player3 ,player4]
    savecheck = True
    for i in namelist:
        if i == "":
            count +=1
    # if blank name
    if count != 0:
        messagebox.showerror("Blackname" , "{} players can't have Blank name".format(count))
        savecheck = False
    # if same name
    if savecheck:
        if len(namelist) != len(set(namelist)):
            sameename = len(namelist) -  len(set(namelist)) + 1
            messagebox.showerror("SameName" , "{} players can't have same name".format(sameename))
            savecheck = False
    # if got names
    if savecheck:
        playy1.destroy()
        playy2.destroy()
        playy3.destroy()
        playy4.destroy()
        play1.destroy()
        play2.destroy()
        play3.destroy()
        play4.destroy()
        save.destroy()
        getnamess = False
        getname()
    
    
def start_game():
    global player_list , thief_num , police_num , name_list , status ,king_num , queen_num , score1,score2,score3,score4 , player1 , player2 , player3, player4

    # if cheats are drawn
    if status == False:

        # score update
        score_1.configure(text = "{} = {}".format( player1 , score1) , font=("Times", 15 ))
        score_2.configure(text = "{} = {}".format(player2 , score2) , font=("Times", 15 ))
        score_3.configure(text = "{} = {}".format(player3,score3) , font=("Times", 15 ))
        score_4.configure(text = "{} = {}".format(player4,score4) , font=("Times", 15 ))
        
        draw["state"] = NORMAL

        # normalcy return
        draw.configure(text = "Redraw chits")
        Player1.configure(text = "{}".format(player1), bg = "white" , fg = "black")
        Player2.configure(text = "{}".format(player2), bg = "white" , fg = "black")
        Player3.configure(text = "{}".format(player3), bg = "white" , fg = "black")
        Player4.configure(text = "{}".format(player4), bg = "white" , fg = "black")
        status = True

        ### rondom shuffling
        for _ in range(10):
            shuffle(name_list)
        ### actual work

        # get chits alloted
        result.configure(text = "Guess the thief" , font=("Times", 15 ))
        for number , name in zip(player_list,name_list):
            if name == "Thief":
                thief_num = number
            if name == "King":
                king_num = number
            if name == "Queen":
                queen_num = number
            if name == "Police":
                police_num = number
                if number == 1:
                    Player1.configure(text = "Police " , bg = "brown" , fg = "white")
                elif number == 2:
                    Player2.configure(text = "Police " , bg = "brown" , fg = "white")
                elif number == 3:
                    Player3.configure(text = "Police " , bg = "brown" , fg = "white")
                else:
                    Player4.configure(text = "Police " , bg = "brown" , fg = "white")
        

        # if already drawn
        else:
            draw["state"] = DISABLED

            
# actual play process for finding thief
def get_theif(num):
    global police_num , thief_num , status , king_num , queen_num , score1,score2,score3,score4 , player1 , player2 , player3, player4 , namelist , player_list
    for i , j in zip(player_list , namelist):
        if i == thief_num:
            thief_name = j
        if i == police_num:
            police_name = j
     
    if status == True:

        # if police
        if num == police_num:
            messagebox.showerror("Wrong" , "Police can't be thief!!")

          # if not thief , wrong  
        elif num != thief_num :
            result.configure(text = "{} was thief ! {} lost".format(thief_name,police_name) ,  font=("Times", 15 ))
            if thief_num == 1:
                score1 += 100
            elif thief_num == 2:
                score2 += 100
            elif thief_num == 3:
                score3 += 100
            else:
                score4 += 100
            status = False
            
       # if thief , right 
        if num == thief_num :
            result.configure(text = "{} is thief ! {} won".format(thief_name,police_name) ,  font=("Times", 15 ))
            if police_num == 1:
                score1 += 100
            elif police_num == 2:
                score2 += 100
            elif police_num == 3:
                score3 += 100
            else:
                score4 += 100
            status = False
            
        # after selecting done   
        if status == False:
            draw["state"] = NORMAL
            if king_num == 1:
                Player1.configure(text = " King " , bg = "Red" , fg = "white")
                score1 += 1000
            elif king_num == 2:
                Player2.configure(text = " King " , bg = "Red" , fg = "white")
                score2 += 1000
            elif king_num == 3:
                Player3.configure(text = " King " , bg = "Red" , fg = "white")
                score3 += 1000
            else:
                Player4.configure(text = " King " , bg = "Red" , fg = "white")
                score4 += 1000
                
            if  queen_num == 1:
                Player1.configure(text = "Queen " , bg = "#FF69B4" , fg = "white")
                score1 += 500
            elif queen_num == 2:
                Player2.configure(text = "Queen " , bg = "#FF69B4" , fg = "white")
                score2 += 500
            elif queen_num == 3:
                Player3.configure(text = "Queen " , bg = "#FF69B4" , fg = "white")
                score3 += 500
            else:
                Player4.configure(text = "Queen " , bg = "#FF69B4" , fg = "white")
                score4 += 500
                
            if thief_num == 1:
                Player1.configure(text = " Thief " , bg = "black" , fg = "white")
            elif thief_num == 2:
                Player2.configure(text = " Thief " , bg = "black" , fg = "white")
            elif thief_num == 3:
                Player3.configure(text = " Thief " , bg = "black" , fg = "white")
            else:
                Player4.configure(text = " Thief " , bg = "black" , fg = "white")

            score_1.configure(text = "{} = {}".format( player1 , score1) , font=("Times", 15 ))
            score_2.configure(text = "{} = {}".format(player2 , score2) , font=("Times", 15 ))
            score_3.configure(text = "{} = {}".format(player3,score3) , font=("Times", 15 ))
            score_4.configure(text = "{} = {}".format(player4,score4) , font=("Times", 15 ))
            
    #if pressed start again
    else:
        messagebox.showerror("Redraw" , "First Draw chits!")

        
# to get winner         
def endscore():
    global score1,score2,score3,score4 , player1 , player2 , player3, player4
    score_list = [score1,score2,score3,score4]
    play_list = [player1,player2,player3,player4]
    winner = []
    max_score = max(score1,score2,score3,score4)
    for i , j in zip(play_list , score_list):
        if j == max_score:
            winner.append(i)
    winner = " & ".join(winner)
    result.configure(text = f"{winner} won" , font=("Courier",10 , "bold"))
    draw.configure(text = "Draw chits")
    
              
    
    
#screen setup
wn = Tk()
wn.title("Chor Chithya Game")
wn.geometry("300x300")
wn.resizable(0,0)



## component setup

# components after getting name
draw = Button(wn, text = "Draw Chits" , command = start_game, bg = "white" , fg = "black"  , padx = 40 , pady =10)
result = Label(wn , text = " " , height = 2)
Player1 = Button(wn , text = "" , command = lambda : get_theif(1) , padx = 50 , pady =2 , bg = "white" , fg = "black")
Player2 = Button(wn , text = "" , command = lambda : get_theif(2) , padx = 50 , pady =2 , bg = "white" , fg = "black")
Player3 = Button(wn , text = "" , command = lambda : get_theif(3) , padx = 50 , pady =2 , bg = "white" , fg = "black")
Player4 = Button(wn , text = "" , command = lambda : get_theif(4) , padx = 50 , pady =2 , bg = "white" , fg = "black")
score_1 = Label(wn , text = " " , height = 2)
score_2 = Label(wn , text = " " , height = 2)
score_3 = Label(wn , text = " " , height = 2)
score_4 = Label(wn , text = " " , height = 2)
end = Button(wn , text = "  End  " , padx = 40 , pady =2 , command =endscore, bg = "white" , fg = "black")
out = Button(wn, text = "  Exit " , command=lambda : wn.destroy(), padx = 40 , pady =2 , bg = "white" , fg = "black")


# components before getting names
playy1 = Label(wn , text = "Player1   :  "  , width =10 , height =3 )
playy2 = Label(wn , text = "Player2   :  "  , width =10 , height =3 )
playy3 = Label(wn , text = "Player3   :  "  , width =10 , height =3 )
playy4 = Label(wn , text = "Player4   :  "  , width =10 , height =3 )
play1 = Entry(wn)
play2 = Entry(wn)
play3 = Entry(wn)
play4 = Entry(wn)
save = Button(wn , text = "Save" , command = getnames)


## component placement

# after getting name
def getname():
    Player1.configure(text = "{}".format(player1), bg = "white" , fg = "black")
    Player2.configure(text = "{}".format(player2), bg = "white" , fg = "black")
    Player3.configure(text = "{}".format(player3), bg = "white" , fg = "black")
    Player4.configure(text = "{}".format(player4), bg = "white" , fg = "black")
    draw.grid(row =1 , column =1 , columnspan = 4 )
    Player1.grid(row = 2 , column =1 , columnspan = 2)
    Player2.grid(row = 2 , column =3 , columnspan = 2)
    Player3.grid(row = 4 , column =1 , columnspan = 2)
    Player4.grid(row = 4 , column =3 , columnspan = 2)
    score_1.grid(row= 3 , column = 1 , columnspan = 2)
    score_2.grid(row= 3 , column = 3 , columnspan = 2)
    score_3.grid(row= 5 , column = 1 , columnspan = 2)
    score_4.grid(row= 5 , column = 3 , columnspan = 2)
    result.grid(row = 6 , column = 1 , columnspan = 4)
    end.grid(row = 7 , column = 1 , columnspan = 2)
    out.grid(row = 7, column = 3 , columnspan = 2)


# before getting names
if getnamess:
    playy1.grid(row= 1 , column = 1)
    playy2.grid(row= 2 , column = 1)
    playy3.grid(row= 3 , column = 1)
    playy4.grid(row= 4 , column = 1)
    play1.grid(row= 1 , column = 2)
    play2.grid(row= 2 , column = 2)
    play3.grid(row= 3 , column = 2)
    play4.grid(row= 4 , column = 2)
    save.grid(row = 5, column =1 , columnspan = 2)
    
wn.mainloop()

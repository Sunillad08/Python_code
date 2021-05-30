# Importing all libraries
import re
import sys
import matplotlib.pyplot as plt
import scipy.stats as sp
import numpy as np
import datetime

# display average score
def avg_marks(marks):
    print(f"\nAverage score of your month is : {np.mean(marks)}\n")   

def display_count(marks):
    for i in range(1,11):
        print(f"{i} occured {marks.count(i)}")
 
def analysis_of_data(marks):
    print(f"\nLowest score was {min(marks)} and ocurred {marks.count(min(marks))} times")
    print(f"Highest score was {max(marks)} and ocurred {marks.count(max(marks))} times")
    print(f"\nBelow satisfaction : {len([i for i in marks if i <= 4 ])}")
    print(f"Satisfactory : {len([i for i in marks if i < 7 and i > 4 ])}")
    print(f"Good : {len([i for i in marks if i > 6 and i < 10])}")
    print(f"Best : {len([i for i in marks if i == 10 ])}")


# taking data as input :
print("Enter data and at End Press 2 times Enter and Ctrl + D : \n")
all_data = sys.stdin.readlines()

# getting data prepared for evaluation
data = " ".join(all_data)
del all_data
print(data)

# get name of month
try:
    match = re.search(r"\d+\s(\w*)\s:",data)
    start , end = match.span()
    month_name = data[start:end].split(" ")[1]
except Exception:
    print("Data given is not in right format!")
    sys.exit()

# get year
year = datetime.datetime.now().year

filter_data = re.findall(r"(\d)/10" , data)
marks = [int(i) for i in filter_data]
print(marks)

if len(data) == 0:
    raise ValueError("Data given is not in right format!") 

avg_marks(marks) # display average marks
display_count(marks) # display count of every marks
analysis_of_data(marks) # display all important details

# marks and x axis setup
x_axis = [ i for i in range(0,len(marks)+2)]
x_axis = np.array(x_axis)
marks.reverse()
marks = np.array(marks)

# mean and median lines setup
avg_marks = round(np.mean(marks),2)
avg = [avg_marks for i in range(len(x_axis))]
med_marks = round(np.median(marks))
med = [med_marks for i in range(len(x_axis))]

# line of regression
res = sp.linregress(x_axis[1:-1], marks)

# plotting everything
plt.figure(figsize = (10,7))

# plot 1 - 10 on y axis
plt.yticks([i for i in range(0,11)])
plt.ylim(0,10)

# trend line
plt.plot(x_axis, res.intercept + res.slope*x_axis, color = 'b', linewidth = 2 , linestyle = "-" , label='Trend')

# mean line
plt.plot(x_axis , avg , color = "k" , linewidth = 1, linestyle = "--" , label = f"Average Marks : {avg_marks}")

# median line
plt.plot(x_axis , med , color = "k" , linewidth = 1, linestyle = "-." , label = f"Median Marks : {med_marks}")

# marks line
plt.plot(x_axis[1:-1] , marks , color = "k" ,linewidth = 2,  marker = "o",markerfacecolor = "r" , label = "Marks")

# controling x and y axis
plt.ylim([0, 10])
plt.xlim([0,x_axis[-1]])

# grid
plt.grid()

# adding title and labels
plt.title("Daily Marks Analysis")
plt.ylabel("Daily Marks")
plt.xlabel("Days")
plt.legend()

# saving file
if len(marks) >=32:
    filename = str(datetime.datetime.now().day) + str(len(marks))
else:
    filename = "Figure_"+str(month_name)
#plt.show()
plt.savefig(f"C:\\Users\\DELL\\Pictures\\Monthly Evaluation\\{year}\\{filename}.png")
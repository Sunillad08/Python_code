import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.stats as sp
import numpy as np

intro = print("Enter data With marking as x/10 and at End Press 2 times Enter and Ctrl + D : \n")
data = sys.stdin.readlines()

data_temp = " ".join(data)
data = list(data_temp)
n = len(data)
marks = []  
marks_count = []

for i in range(0,n):
    if i+1 < n:
        j = i+1
    if(data[j] == "/"):
        try:
            marks.append(int(data[i]))
        except:
            raise Exception("error occured : check data!")
        
print("Average score of your month is : " + str(sum(marks)/len(marks)) + "\n" )        
    
for i in range(1,11):
    r = str(marks.count(i))
    marks_count.append(int(r))
    print(str(i) + " Occured " + r )

for i in range(1,11):
    if marks_count[i-1] > 0:
        print("\nLowest score was " + str(i) + " and ocurred " + str(marks_count[i-1]) + " times")
        break
for i in range(10,0,-1):
    if marks_count[i-1] > 0:
        print("Higest score was " + str(i) + " and ocurred " + str(marks_count[i-1]) + " times" )
        break
    
low_sum = 0
mid_sum = 0
high_sum = 0
for i in range(0,10):
    if i < 4:
        low_sum += marks_count[i]
    elif i < 7:
        mid_sum += marks_count[i]
    elif i < 9:
        high_sum += marks_count[i]
print("\nBelow satisfaction : " + str(low_sum) +"\n"+ "Satisfactory : " + str(mid_sum) +"\n"+ "Good : " + str(high_sum) +"\n"+ "Best : " + str(marks_count[i]))
x_axis = []
for i in range (1,len(marks)+1):
    x_axis.append(i)




marks = marks[::-1]
marks = np.array(marks)
x_axis_updated = x_axis
last_day = x_axis_updated[-1]
x_axis = np.array(x_axis)
x_axis_updated.append(x_axis[-1]+1)
x_axis_updated.append(0)
avg_marks = round(sum(marks)/len(marks),2)
avg = [avg_marks for i in range(len(x_axis_updated))]
med_marks = round(np.median(marks))
med = [med_marks for i in range(len(x_axis_updated))]
x_axis_updated = np.array(x_axis_updated)
res = sp.linregress(x_axis, marks)

plt.figure(figsize = (10,7))
plt.yticks([i for i in range(0,11)])
plt.plot(x_axis_updated, res.intercept + res.slope*x_axis_updated, color = 'b', linewidth = 2 , linestyle = "-" , label='Trend')
plt.plot(x_axis_updated , avg , color = "k" , linewidth = 1, linestyle = "--" , label = f"Average Marks : {avg_marks}")
plt.plot(x_axis_updated , med , color = "k" , linewidth = 1, linestyle = "-." , label = f"Median Marks : {med_marks}")
plt.plot(x_axis , marks , color = "k" ,linewidth = 2,  marker = "o",markerfacecolor = "r" , label = "Marks")
plt.ylim([0, 10])
plt.xlim([0,last_day+1])
plt.grid()
plt.ylim(0,10)
plt.title("Daily Marks Analysis")
plt.ylabel("Daily Marks")
plt.xlabel("Days")
plt.legend()
#plt.show()
plt.savefig("Graph.png")
# end

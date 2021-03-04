import sys

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
        marks.append(int(data[i]))
        
print("Average score of your month is : " + str(sum(marks)/len(marks)) + "\n" )        
    
for i in range(1,11):
    r = str(marks.count(i))
    marks_count.append(int(r))
    print(str(i) + " Occured " + r )

for i in range(1,11):
    if marks_count[i-1] > 0:
        print("\nLowest score was " + str(i) + " and ocurred " + str(marks_count[i-1]) + " times")
        break;
for i in range(10,0,-1):
    if marks_count[i-1] > 0:
        print("Higest score was " + str(i) + " and ocurred " + str(marks_count[i-1]) + " times" )
        break;
    
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





        

month_name = input("Enter month : ")
number_of_days = int(input("Enter no of days : "))
monday = int(input("Enter first monday date : "))
print("\n")
print(f"Average of {month_name} : ")
print("\n")

if monday > 1:
    middle = '⬛'*(7 - (monday - 1)) + '⬜'*(monday - 1)
    print(f'01 {middle} {monday-1:02} \n')
for i in range(monday,number_of_days+1,7):
    middle = '⬜'*(min(i+6,number_of_days) - i + 1) + '⬛'*(6 - (min(i+6,number_of_days) - i))
    print(f'{i:02} {middle} {min(i+6,number_of_days):02} \n')

for i in range(number_of_days,0,-1):
    print("\n--------------------------------------------------\n")
    print(str(i) +" "+ month_name +" : "+" /10")
    print("\nCompleted Task : ")
    print("•")
    print("\nMistakes and corrections : ")
    print("•")
    print("\nhow are you feeling today? :) ")
    print("•")
print("\n--------------------------------------------------\n")    
print("\nAdditional data : ")
print(f"\nFirst Monday : {monday}\n")
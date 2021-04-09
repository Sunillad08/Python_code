import random
import sys

print("This is guess the random number game!!")
print("\nThe number is in between 1 to 100")
hint_num = 6
num = random.randint(1,100)


def hint(hint,num):
	if hint == 5:
		num 
		
		

def information (n):
	if n % 2 == 0:
		print ("\nThe number is Even!")
	else:
		print("\nThe number is Odd!")
	if n > 50 :
		print("\nNumber is grater than 50")
	else:
		print("\nNumber is less than 50")
information (num)
print(num)
print("\nGuess the number!")

def main():
	guess_num = int(input())
	if num == guess_num:
		print("\nGuess is right")
		sys.exit()
	else:
		print("\nWant Help??\n1.For Hint \n2.Guess again")
		choice = input()
		if choice == 1 :
			hint_num -= 1
			print(hint(hint_num,num))
		else:
			condition = True
			 
while True:
	main()
	
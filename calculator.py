import math
import sys
#Calculator: Basic Calculation
def console_output():
	try:
		print(eval(input()))
	except Exception as e:
		print(e)
def ac():
	print("0:True or 1:False")
	ac= input()
	if ac == "0":
		main()
	elif ac == "1":
		sys.exit()
	else:
		ac()
def main(): 
	print("Hello user!")
	console_output()
	ac()
main()

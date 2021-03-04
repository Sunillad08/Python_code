print("Hello user!")
c=input("Enter your name : ")
print("Welcome", c,"!")
try:
     h=int(input("Please enter your age :"))
     print("Your age is",h)
except:
	print("Invalid input")
try: 
     open(c,".txt")
except:
	print("Invalid filename")
	print(c,".txt")
			 

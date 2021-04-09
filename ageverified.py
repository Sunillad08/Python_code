try:
	age=int(input("Enter your age = "))
	if age>17:
		 vote=input("choose from these:  \n 1.sunil\n2.gaurang\n3.Nota\n")
	else:
		print("Underage")
        
except:
	print("invalid input")
finally:
    print("thank!")
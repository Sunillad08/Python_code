num1=int(input("Enter a number = "))
num2=int(input("Enter a number = "))
print("Two numbers are",num1,"&",num2)
n1=num1
n2=num2
rem=0
while n2!=0:
	   rem=n1%n2
	   n1= n2
	   n2= rem
print("Gcd is ", n1)
lcm=(num1*num2)/n1
print("Lcm is",lcm) 
print("end")	   		   
#Fastest way to do work
class fastest_way():
	def palindrome(word):
		return bool(word.count(word[::-1]))

	def Armstrong(n):
		sum1,num =0,n
		while num > 0:
			sum1 = sum1 + (num%10)**3
			num = num//10
		return sum1 == n 
			
	def isprime(num):
		if num > 1 :
			i = 2
			while i*i <= num :
				if num % i == 0 :
					return False
				i += 1
			
			return True
		else:
			return False
		
			
		
def main():
	print("1. Palidrome \n2.prime\n3.Armstrong")
	choice = int(input())
	if choice == 1 :
		print(fastest_way.palindrome(input()))
	elif choice == 2 :
		print(fastest_way.isprime(int(input())))
	elif choice == 3:
		print(fastest_way.Armstrong(int(input())))
def check_fuc():
	pass
	
	
main()

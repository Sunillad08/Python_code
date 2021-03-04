def get_prime(n):
	if n == 1 :
		return "Not prime"
	i=2
	while i*i <= n:
		if n%i == 0:
			return "Not prime"
		i+=1
	return "Prime"
	
n=int(input("Enter a number = "))
result=get_prime(n)
print(result)
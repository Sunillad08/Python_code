


def dec_to_bin(num):
	dec = str(num).split(".")
	b = []
	i = dec[0]
	i = int(i)
	while i> 0:
		b.append(str(i%2))
		i = i//2
	'''b.insert(0 , ".")
	j = dec[1]
	j = int(j) 
	for _ in range(10):
		
		b.insert(0 , str())'''
	
	return "".join(b[::-1])
	
def bin_to_dec(num):
	num = list(str(num))
	l = len(num)
	sum = 0
	for k in range(0,l):
		sum += int(num[l-k-1])*(2**k)
	return sum
	
def 		
	
	
	
	
num1 = float(input())
print(dec_to_bin(num1))
num2 = float(input())

print(bin_to_dec(int(num2)))
	
		
		

	
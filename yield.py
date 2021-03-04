def getint(n):
	for i in range (n):
		t =  int(input())
		yield t
for i in getint(int(input())):
	num= i
	print(f"value is {num}")

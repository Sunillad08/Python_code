n=input().split()
list1=[]
list2=[]
for i in range(len(n)):
	list1=list(n[i])
	list2.append(list1)
for i in range(len(list2)):
    list2[i][0]=list2[i][0].upper()
for i in range(len(list2)):
	print("".join(list2[i]),end=" ")


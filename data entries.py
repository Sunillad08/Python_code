try:
    n=int(input("\nEnter number of entries you want = "))
    year=int(input("\nEnter starting year = "))
    k=int(input("\nEnter Quater of year = "))
    if k > 4: 
        print("\nInvalid Quarter No. // No. should be in between 1 to 4 ")
    else :  
          num1=[]
          ycou = k;
          print("\nData entries :\n")
          for i in range(n):
                 print("Year",year," Quarter ", k," =")
                 result=input()
                 num1.append(result)
                 ycou=ycou+1
                 k=k+1
                 if ycou == 5:
                     ycou = 1;
                     year+=1
                 if k>4:
                     k = 1
                     
except :
	print("Invalid input")        
finally:
	print(num1:)
 
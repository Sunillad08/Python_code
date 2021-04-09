grey = str(input())
binary =[]
flag = 0
for i in range (len(grey)):
    if flag == 0:
        temp = grey[i]
        binary.append(grey[i])
        flag = 1
    else:
        if temp == grey[i]:
            temp = str(0)
        else:
            temp = "1"
        binary.append(str(temp))
        
                
                
print( "".join(binary))
        
        
    
    

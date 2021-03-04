
def power_no_1(num):
    a = list( range(2,num+1))
    b = a
    c = []
    for i in a:
        for j in b:
            c.append(i**j)
    print( sorted(c))
    return len(set(c))
            
    




def power_no(num):
    count = 0
    a = list( range(2,num+1))
    b = [ i*i for i in a]
    for i in a:
        for j in b:
            if i == j:
                count+=1
    return (num-1)**2 - count
n = int(input("enter no"))
print(power_no(n) , power_no_1(n))

    

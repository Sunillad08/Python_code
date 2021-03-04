

def isprime(num):
    j = 2
    while j*j <= num:
        if num % j == 0:
            return False
        j += 1
    return True

def sum_of_prime(num):
    prime_list =[]
    sum1 = 0
    for i in range (2,num+1):
        if isprime(i):
            sum1 += i
            prime_list.append(str(i))
    return sum1,prime_list
        
def main():
    sum1 , prime_list = sum_of_prime(int(input("Enter a number = ")))
    prime_list = "+".join(prime_list)
    print(prime_list,"=",sum1)
main()
    
    
    

        
    
            
        
    

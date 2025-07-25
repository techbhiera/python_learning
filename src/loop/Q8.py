prime_num= int(input("Write the prime number"))
a=True
if prime_num>1:
    for i in range(2,prime_num):
        if prime_num%i==0:
            a=False
            
        
print(a)
            










#using Function


def prime_number(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**(0.5)+1),2): # type: ignore
        if n%i==0:
          return False
    return True
    
prime_num= float(input("Write the prime number"))

if prime_number(prime_num):
    print("The given number is a prime number",prime_num)
else:
    print("The given number is not a prime number", prime_num)



        
            
        
        
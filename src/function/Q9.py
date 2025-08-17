def generator_even(even: int):
    for i in range(1,even+1):
        yield(i*2)
    
        
        
        
for num in generator_even(10):print(num)
    
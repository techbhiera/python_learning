number=int(input("Write the number till do u want to add : \n"))
sum=0
for i in range(0,number+1,2):
    sum+=i
print(sum)






number=int(input("Write the number till do u want to add : \n"))
sum=0
for i in range(number+1):
    if i % 2 == 0:
        sum+=i

print(sum)



number=int(input("Write the number till do u want to add : \n"))
sum =0 
i = 2
while number>i:
    sum+=i
    i+=2
print(sum)



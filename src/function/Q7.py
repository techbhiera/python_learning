
def sum_all(*args: int) :
    return sum(args)

print(sum_all(1,2,4))

def __sum__(num:list):
    length=len(num)
    add=0
    for i in range(0,length):
        add+=int(num[i])
    
    return add


a = list((input("input")))
print(a)
b = __sum__(a)
print(b)

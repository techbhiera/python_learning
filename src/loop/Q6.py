factorial=int(input("give the number"))
factor=1
for i in range (factorial,1,-1): # you can keep range(start,end "1,0"both ,step) --------->>>> (5! = 5*4*3*2 or 5*4*3*2*1)'''
    factor *= i
print(f"{factorial}! is ",factor)







factorial=int(input("give the number"))
factor = factorial-1
i = factorial
while factor>=1:
    i *=factor
    factor-=1
print(f"{factorial}! is ",i)
    
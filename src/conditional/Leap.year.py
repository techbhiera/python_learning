year = int(input("write down year:"))
if year % 4 == 0 or year % 400 ==0 and year% 100 != 0   :
    print(year, "is a leap year")
else:
    print(year,"is not leap year")
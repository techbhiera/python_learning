number = int(input("Table of a number do you want: \n "))
for i in range(1,11):
    if i ==5 :
        continue
    table=number*i
    print(f" {number} * {i} =",table)
    
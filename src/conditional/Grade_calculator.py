while True:
    marks = input("enter your marks:")
    if marks.isdigit() and int(marks) >= 0 :
        print("thanks for entered marks")
        break
    else:
        print("enter your marks:")
        

if 100 >= int(marks) >= 90:
    print("your grade is:\n\t\"A\"")


elif 89 >= int(marks) >= 80:
    print("your grade is:\n\t\"B\"")
elif 79 >= int(marks) >= 70:
    print("your grade is:\n\t\"C\"")
elif 69 >= int(marks) >= 60:
    print("your grade is:\n\t\"B\"")
else:
    print("your grade is:\n\t\"F\"")



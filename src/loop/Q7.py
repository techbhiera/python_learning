while True:
    number = input("write the number :")
    if number.isdigit() and 1<int(number)<10:
        print("valid input")
        break
    else:
        print("Invalid input")
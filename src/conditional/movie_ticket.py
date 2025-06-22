def movie_ticket():
    from datetime import date

    age = int(input("Age:\n"))
    dinak = date.today()
    day = dinak.strftime("%A")  #  current day of the week

    # Base ticket price
    price = 12 if age >= 18 else 8
    print("Your ticket price is $", price)

    # Wednesday discount
    if day == "Wednesday":
        price -= 2
        print("You got $2 Rs discount!")

    print("Pay $", price)

    # according to the day, you will get a message
    week_info = {
        "Monday": {"god": "Lord Shiva", "discount": 0},
        "Tuesday": {"god": "Lord Hanuman", "discount": 0},
        "Wednesday": {"god": "Lord Ganesha", "discount": 2},
        "Thursday": {"god": "Lord Guru", "discount": 0},
        "Friday": {"god": "Goddess Lakshmi", "discount": 0},
        "Saturday": {"god": "Lord Shani & Hanuman", "discount": 0},
        "Sunday": {"god": "Lord Surya", "discount": 0}
    }
    info = week_info[day]
    print(f"Today is {day}, dedicated to {info['god']}. Discount: ${info['discount']}")

    if day != "Wednesday":
        print("Disclaimer:if u come on wednesday u will get 2$ discount for Lord Ganesha day")

    
# Call the function
price_final = movie_ticket()

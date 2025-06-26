color = input("enter your banana colour : \n")
match color.title():
    case "Green":
        print("Unripe")
        print("wait few more days !")
    case "Yellow":
        print("Ripe")
        print("Ready to Eat!")
    case "Brown":
        print("Overripe")

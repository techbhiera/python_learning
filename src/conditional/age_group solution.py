age_group = int(input("Enter your age: "))
if age_group < 13:
    print("You are a child.")
elif 13 <= age_group < 20:
    print("You are a teenager.")
elif 20 <= age_group < 59:
    print("You are an adult.")
elif age_group >= 60:
    print("You are a senior citizen.")
else:
    print("Invalid age input.")
    
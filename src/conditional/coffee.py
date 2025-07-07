Coffee_order =input("write down quantity 'Small''Medium''Large':""\t\n")
size = Coffee_order.title()
extra_shot = input("True or False")
if extra_shot.strip().lower() == "true":
    coffee= size + "\ncoffee with extraa shot"
    print(coffee) 
else:
    coffee= size + "coffee"
print(coffee)

breed = input("Type of your pet : Dog or Cat")
pet_age = float(input("Age of your pet in years :"))

if breed.title() == "Dog" and pet_age<2 :
    Suggest = "Puppy Food"
elif breed.title() == "Cat" and pet_age > 5:
    Suggest = "Senior Cat Food"
else :
    Suggest = "bread and milk"
print(Suggest)


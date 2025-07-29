items = ["apple", "banana", "orange", "apple", "mango"]
unique_items = set()

for i in items:
    print(i)
    if i in unique_items:
        print("duplicate",i)
        break
    unique_items.add(i)

print(unique_items) #Tell you where it breaks

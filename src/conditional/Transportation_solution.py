while True:
    distance = input("write the distance in Km :\t")
    try:
        final_distance=float(distance)
        if  final_distance>0:
            print("Thanks for input")
            print("Your given distance is :\n\t",final_distance,"km")

            break
        
    except ValueError:
        print("Write a valid numeric distance")


if final_distance < 3:
    print("Take a walk")
elif final_distance < 15:
    print("Take a bike")
else:
    print("Take a car")

def circle(radius: float):
    print("calculation of radius of the circle:",circle_stats,"cm")
    circumference = 2* (22/7)* radius
    area = (22/7) * radius**2
    
    return (circumference,area)




circle_stats=float(input("radius of the circle:"))
circumference,area=circle(circle_stats)
print(f"{circumference:.2f},{area:.2f}")


import math  
radius = float(input("Enter the radius of the sphere: "))
r_cubed = radius ** 3
volume = (4 / 3) * math.pi * r_cubed
print(f"The volume of the sphere with radius {radius} is {volume:.2f}")
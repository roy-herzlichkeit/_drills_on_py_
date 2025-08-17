import math

radius = float(input("Radius: "))

circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print(f"Cirumference: {round(circumference, 2)}")
print(f"Area: {round(area, 2)}")
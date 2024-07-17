import math

def find_cylinder_volume(r,h):
    return math.pi*(r**2)*h


r = float(input("radius = "))
h = float(input("height = "))
V = find_cylinder_volume(r,h)
print(f"Volume = {V:.2f}")
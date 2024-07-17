import math

def area_of_circle(k):
    return (k**2)*(math.pi)




d = input("Diameter: ")
d_float = float(int((d))/2)

area = area_of_circle(d_float)
print(f"area = {area:.3f}")
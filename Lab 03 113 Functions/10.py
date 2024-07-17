import math

def MiniHeart(x):
  
    return ((x)**2)+((x/2)**2)*(math.pi)

x=int(input("Please enter the value of L: "))
print(f"Area is {MiniHeart(x):.4f}")
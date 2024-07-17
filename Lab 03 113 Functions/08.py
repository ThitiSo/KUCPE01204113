def distance(a,t):
    return (1/2)*a*(t**2)


acceleration = int(input("Acceleration : "))
time = int(input("Time : "))
print(distance(acceleration,time))
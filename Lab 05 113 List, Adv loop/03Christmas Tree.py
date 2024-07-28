a=int(input("Enter number of bushes: "))
b=int(input("Enter size of each bush: "))
for i in range(a):
    z=0
    for j in range(b):
        print(" "*(b-1-z)+"*"*(1+z*2))
        z+=1
        

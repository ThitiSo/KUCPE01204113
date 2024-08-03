a=int(input())
z=1
for i in range(a):
    if i == 0 or i == a-1:
        #print(i)
        print("."*a)
        
    elif i== (a//2):
        #print(i)
        print(".",end="")
        print(" "*(i-1),end="")
        print(".",end="")
        print(" "*(i-1),end="")
        print(".")
    elif i>a//2:
        #print(i)
        print(".",end="")
        print(" "*(a-i-2),end="")
        print(".",end="")
        print(" "*(1+(i-(a//2)-1)*2),end="")
        print(".",end="")
        print(" "*(a-i-2),end="")
        print(".")  
        z-=1
    else:
        #print(i)
        print(".",end="")
        print(" "*(i-1),end="")
        print(".",end="")
        print(" "*(abs(a-(i*2))-2),end="")
        print(".",end="")
        print(" "*(i-1),end="")
        print(".")
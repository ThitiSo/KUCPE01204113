y=int(input("Enter the number of rows or columns : "))
z=0
for i in range(y):
    for j in range(y):
        print('%2d'%(j+1+z),end=" ")
    z+=1
    print("\n",end="")

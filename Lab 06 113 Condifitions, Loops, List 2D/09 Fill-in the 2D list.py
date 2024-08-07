y=int(input("Enter the number of rows or columns : "))

for i in range(y):
    for j in range(y):
        print('%2d'%(j+1+i),end=" ")
    print("\n",end="")

a=input("Grid Size: ").split()

b=int(input("Number of mine(s): "))
field=[]
for i in range(int(a[1])):
    field.append([])

    for j in range (int(a[0])):
        field[i].append(0)
for i in range (b):
    y,x= input(f"Mine#{i+1}: ").split()
    y, x =int(y),int(x)
    field[x][y]="X"


    if x-1 >= 0:
        
        if y-1 >= 0 and type(field[x-1][y-1])== int:
            # print("just enter")
            field[x-1][y-1]=field[x-1][y-1]+1
            # print("I try [x-1][y-1]")
        if y+1 >= 0 and y+1 <= int(a[0])-1 and type(field[x-1][y+1])== int : 
            field[x-1][y+1]=field[x-1][y+1]+1
            # print("I try [x-1][y+1]" )   
        if  type(field[x-1][y])== int: 
            field[x-1][y]=field[x-1][y]+1
            # print("I try [x+1][y]" )     
    if x+1 > 0 and x+1 <= len(field)-1:
        if y-1 >= 0 and type(field[x+1][y-1])== int:
            field[x+1][y-1]=field[x+1][y-1]+1
            # print("I try [x+1][y-1]" )   
        if y+1 >= 0 and y+1 <=int(a[0])-1 and type(field[x+1][y+1])== int:
            field[x+1][y+1]=field[x+1][y+1]+1
            # print("I try [x+1][y+1]" )  
        if  type(field[x+1][y])== int:     
            field[x+1][y]=field[x+1][y]+1
            # print("I try [x+1][y]" ) 
    if y-1 >= 0 and type(field[x][y-1])== int:
        field[x][y-1]=field[x][y-1]+1
        # print("I try [x][y-1]" ) 
    if y+1 >= 0 and y+1 <=int(a[0])-1 and type(field[x][y+1])== int:
        field[x][y+1]=field[x][y+1]+1
        # print("I try [x][y+1]" )    

for i in field:
    for j in i:
        print(j,end=" ")
    print("\n",end="")
  
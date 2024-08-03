y=int(input("Enter Rook's row position: "))
x=int(input("Enter Rook's column position: "))

chess=[]
for i in range(8):
    chess.append([])
    for j in range(8):
        chess[i].append(" ")
        if j == x and i == y:
            chess[i][j]="R"
        elif j == x:
            chess[i][j]="x"
        elif i == y:
            chess[i][j]="x"
z=0
for i in range(17):
    if i % 2==0:
        print("-"*17)
    else:
        print("|",end="")
        for j in range (8):
            print(chess[z][j]+"|",end="")
        z+=1
        print("\n",end="")







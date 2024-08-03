mode=input("Direction to flip square (V/H): ")
a=int(input("Input size of square: "))
matrix_first,matrix_second=[],[]
for i in range(a):
    matrix_first.append([])
    tmp=input().split()
    for k in tmp:
        matrix_first[i].append(k)
print("After flip:")
if mode=="V":
    for i in range(a-1,-1,-1):
        for j in range(a):
            print(matrix_first[i][j],end=" ")
        print("\n",end="")
elif mode=="H":
    for i in range(a):
        for j in range(a-1,-1,-1):
            print(matrix_first[i][j],end=" ")
        print("\n",end="")
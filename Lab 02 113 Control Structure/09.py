a=int(input("Input number: "))
for i in range(a+1):
    for j in range(i):
        print(str(j+1) , end=" ")
    if i!= 0:
        print('\n', end="")

A = list(map(int,input().split()))
while True:
    menu,x = input().split()
    if menu == "A":
        A.append(int(x))
    elif menu == "S":
        if len(A)-1< int(x):
            pass
        else:
            print(A[int(x)])
    elif menu == "R":
        A.pop(int(x))
    elif menu =="E" and x == "0":
        for i in A:
            print(i,end=" ")
        break
   

a=input().split()
b=[]
for i in a:
    b.append(int(i))
# print(b)
while True:
    f1,f2=input().split()
    f1,f2=int(f1),int(f2)
    # print(f1,f2)
    if (f1 < -len(b) or f1 > len(b)-1) and (f2 > len(b)-1 or f2 < -len(b)):
        print("x and y Bad Input")
    elif f1 < -len(b) or f1 > len(b)-1:
        print("x Bad Input")
    elif f2 > len(b)-1 or f2 < -len(b):
        print("y Bad Input")
    # elif f1 > f2:
    #     # print("")
    #     break
    else:
        if f1 < 0:
            f1=f1+len(b)
        if f2 < 0:
            f2=f2+len(b)
        if f2 < f1:

            break

        print(sum(b[f1:f2+1]))

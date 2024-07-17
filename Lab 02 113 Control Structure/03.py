a=int(input("x: "))
b=input("Operator: ")
c=int(input("y: "))
if b=="+":
    print(a+c)
elif b=="-":
    print(a-c)
elif b=="*":
    print(a*c)
elif b=="/":
    print('{0:.2f}'.format(a/c))
elif b=="%":
    print(a%c)
else:
    print("Unknown Operator")
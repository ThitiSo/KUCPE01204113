a=1
poscoll,negcoll=[],[]
while a != 0:
    a = float(input("Enter a number (or 0 to exit): "))
    if a > 0:
        poscoll.append(float(a))
    else:
        negcoll.append(float(a))
    
print(f"The sum of all positive numbers is {sum(poscoll):.2f}")
print(f"The sum of all negative numbers is {sum(negcoll):.2f}")

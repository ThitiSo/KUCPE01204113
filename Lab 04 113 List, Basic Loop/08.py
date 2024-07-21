a=int(input("Enter the depth of the well: "))
b=int(input("How high the frog can jump up? "))
c=int(input("How far the frog slips down? "))
count=1
if a-b!=0 and b<=c:
    print("The frog cannot get out of the well.")
else:
    while a >= 1:
        a=a-b
        if a <= 0:
            print(f"The frog is free on day {count}.")
            break
        print(f"On day {count} the frog leaps to the depth of {a} meters.")
        a=a+c
        print(f"At night he slips down to the depth of {a} meters.")
        count+=1
        

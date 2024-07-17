a=int(input("Minutes before due: "))
b=float(input("Temperature: "))
c=input("Is it raining (y/n)? ")

d =a/1440
if(1>d>=0.5):
    d=1
else :
    d = round(d)

if 5<d:
    print(">>>",d,"days before due.")
    print(">>> I will not do the assignment.")
elif 1<d:
    print(">>>",d,"days before due.")
    if b >40:
        print(">>> I will not do the assignment.")
    elif b >25 and c =="Y":
        print(">>> I will not do the assignment.")

    elif b >25 and c =="y":
        print(">>> I will not do the assignment.")

    
    else:
        print(">>> I will do the assignment.")
else:
    print(">>>",d,"days before due.")
    print(">>> I will do the assignment.")

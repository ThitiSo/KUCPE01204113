a=int(input("Enter year: "))
if a<1:
    print("Invalid year.")
elif a%400==0:
    print(a,"is a leap year.")
elif a%100==0:
    print(a,"is not a leap year.")
elif a%4==0:
    print(a,"is a leap year.")
else:
    print(a,"is not a leap year.")
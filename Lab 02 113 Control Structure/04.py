a=int(input("Weight: "))
c=int(input("Height: "))/100
print("Your BMI is",'{0:.1f}'.format(a/(c**2)),end=" ")
if a/(c**2)>=30:
    print("You're in the obese range.")
elif a/(c**2)>=25:
    print("You're in the overweight range.")
elif a/(c**2)>=18.6:
    print("You're in the healthy weight range.")
else:
    print("You're in the underweight range.")


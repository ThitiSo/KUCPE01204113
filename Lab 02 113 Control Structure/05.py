#target = 72
a=int(input("Enter your guess (0 - 100): "))
if a>100 or a<0:
    print("Sorry, out of range, try again later.")
elif a==target:
    print("Congratulations, your guess is correct.")
else:
    print("Sorry, your guess is wrong, try again later.")
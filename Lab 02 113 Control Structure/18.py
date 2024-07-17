a=int(input("Enter your guess (0 - 100): "))
if a>100 or a<0:
    print("Sorry, out of range, try again later.")
elif a>target:
    print("Sorry, your guess is too high, try again later.")
elif a<target:
    print("Sorry, your guess is too low, try again later.")
else:
    print("Congratulations, your guess is correct.")
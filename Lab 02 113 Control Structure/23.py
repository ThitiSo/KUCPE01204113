a=int(input("Enter your guess (0 - 100): "))
while a!=target :
    if a>100 or a<0:
        print("Sorry, out of range, try again later.")
        a=int(input("Enter your guess (0 - 100): "))
    elif a>target:
        print("Sorry, your guess is too high, try again later.")
        a=int(input("Enter your guess (0 - 100): "))
    elif a<target:
        print("Sorry, your guess is too low, try again later.")
        a=int(input("Enter your guess (0 - 100): "))

print("Congratulations, your guess is correct.")
        
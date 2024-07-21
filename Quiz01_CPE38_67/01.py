sec=int(input("secret number = "))
i=1
while i<4:
    guess=int(input("Enter your guess : "))
    if guess==sec:
        print("Congratulations, your guess is correct.")
        break
    elif i==3:
        print("You've used all your attempts.")
        break
    elif guess<sec:
        print("Sorry, your guess is too low, pls try again.")
    elif guess>sec:
        print("Sorry, your guess is too high, pls try again.")
    i+=1
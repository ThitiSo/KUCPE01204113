a=input("Enter your buffet choice: ")
if a =="Korean" or a=="Japanese":
    b=input("Is today Wednesday (yes/no)? ")
    if a =="Korean" and b=="yes":
        print("Your payment is 1275.00 Baht.")
    elif a=="Japanese" and b=="yes":
        print("Your payment is 850.00 Baht.")
    elif a =="Korean" and b=="no":
        print("Your payment is 1500.00 Baht.")
    elif a=="Japanese" and b=="no":
        print("Your payment is 1000.00 Baht.")
else:
    print("Sorry, there is no" ,a,"buffet.")
a=input("Is Bulotelli injured?(y/n) ")
if a=='n':
    b=input("Is Bulotelli late for the training?(y/n) ")
    if b=='y':
        c=input("Did Bulotelli perform well in training?(y/n) ")
        if c=="n":
            print("Not selected")
        else:
            print("Substitute")
    else:
        print("Starter")
else:
    print("Not available")

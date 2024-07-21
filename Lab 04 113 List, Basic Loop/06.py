count=0
while count != 3:
    a = input("Enter your password: ")
    if a != "I love programming":
        count+=1
        print(f"Wrong password, attempt #{count}")
        print("Access not allowed")
    else:
        print("Correct password")
        print("Access granted")
        break
    if count==3:
        print("Maximum attempts exceeded")

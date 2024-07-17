a=input("Username: ")
c=input("Password: ")
if a == ADMIN_USERNAME and c == ADMIN_PASSWORD:
    print("Welcome, admin.")
else:
    print("You are not admin.")
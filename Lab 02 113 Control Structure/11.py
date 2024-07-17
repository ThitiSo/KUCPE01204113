a=input("Enter a string: ")
b=int(input("Enter arrow's size (greater than 0): "))
if b%2==1:
    c=1
else:
    c=0
if b <= 0:
    print("Size must be greater than 0.")
else: 
    for i in range(0,int(b/2)+c):
        print(" "*(i)+str(a))
    for i in range(int(b/2),0,-1):
        print(" "*(i-1)+str(a))
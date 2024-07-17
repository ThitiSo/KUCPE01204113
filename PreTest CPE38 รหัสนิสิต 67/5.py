a=int(input("Input Level : "))
b=0
for i in range(a):
    print(" "*(((a+1-b)*2)-1) + "o"*(1+4*(i)))
    b+=1
for i in range(2*a+1):
    print(" "*3 + "o"*((a-1)*4+1))
for i in range(a):
    print("o"*((4*a)+3))
for i in range(a+2):
    print(" "*((a)+2) +"o"*((2*a)-1))
for i in range(a):
    print(" "*(3) +"o"*((4*(a-1)+1)))
print(" "*(a+2) +"o"*((2*a-1)))
p1p,p2p=0,0
t=1

def draw(a,b):

    if a== 1 and b == 1:
        print('__QQ'+" "*6+'__QQ')
        print("()\">"+"  VS  "+"()\">")
    elif a== 1 and b == 2:
        print('__QQ'+" "*6+' O ')
        print("()\">"+"  VS  "+"/|\\")
        print(" "*10 + "/ \\")
    elif a== 1 and b == 3:
        print("__QQ"+" "*6+' /\_/\ ')
        print("()\">"+"  VS  "+"( o.o )")
        print(" "*10 + " > ^ < ")
    elif a== 2 and b == 1:
        print(' O '+" "*6+'__QQ')
        print("/|\\"+"  VS  "+"()\">")
        print("/ \\")    
    elif a== 2 and b == 2:
        print(' O '+" "*6+' O ')
        print("/|\\"+"  VS  "+"/|\\")
        print("/ \\"+ " "*6+ "/ \\")
    elif a== 2 and b == 3:
        print(' O '+" "*6+' /\_/\ ')
        print("/|\\"+"  VS  "+"( o.o )")
        print("/ \\"+" "*6 + " > ^ < ")
    elif a== 3 and b == 1:
        print(' /\_/\ '+" "*6+'__QQ')
        print("( o.o )"+"  VS  "+"()\">")
        print(" > ^ < ")
    elif a== 3 and b == 2:
        print(' /\_/\ '+" "*6+' O ')
        print("( o.o )"+"  VS  "+"/|\\")
        print(" > ^ < "+" "*6 + "/ \\")
    elif a== 3 and b == 3:
        print(' /\_/\ '+" "*6+' /\_/\ ')
        print("( o.o )"+"  VS  "+"( o.o )")
        print(" > ^ < "+" "*6 + " > ^ < ")

def check(a,b):

    global p1p,p2p
    if a==1 and b==2:
        p1p+=1
    elif a==2 and b==1:
        p2p+=1
    elif a==2 and b==3:
        p1p+=1
    elif a==3 and b==2:
        p2p+=1
    elif a==3 and b==1:
        p1p+=1
    elif a==1 and b==3:
        p2p+=1
        
p1=input("Player1 name: ")
p2=input("Player2 name: ")

while(p1p!= 3 and p2p!= 3 and t <=5):

    print("")
    print(f"Round {t}!")
    print(f"{p1} {p1p} / {p2} {p2p}")
    a=int(input(f"{p1}'s choice (1/rat, 2/hunter and 3/lion): "))
    b=int(input(f"{p2}'s choice (1/rat, 2/hunter and 3/lion): "))
    draw(a,b)
    check(a,b)
    t+=1

print("")
print(f"{p1} {p1p} / {p2} {p2p}")
if p1p>p2p:
    print(f"{p1} win!")
elif p1p<p2p:
    print(f"{p2} win!")
elif p1p==p2p:
    print(f"Draw!")


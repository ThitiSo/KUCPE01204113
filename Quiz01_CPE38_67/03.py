p1p,p2p=0,0
def DrawRat():
  s='__QQ\n()">\n'
  print(s)
def DrawHunter():
  s=' O\n/|\ \n/ \ \n'
  print(s)
def DrawLion():
  s=' /\_/\ \n( o.o )\n > ^ <\n'
  print(s)
def case(n):
    if n ==1:
        DrawRat()
    if n ==2:
        DrawHunter()
    if n ==3:
        DrawLion()
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
print("")
print("Round 1!")
print(f"{p1} 0 / {p2} 0")
a=int(input(f"{p1}'s choice (1/rat, 2/hunter and 3/lion): "))
b=int(input(f"{p2}'s choice (1/rat, 2/hunter and 3/lion): "))
print("")
print(f"{p1}")
case(a)
print("VS")
print("")
print(f"{p2}")
case(b)
check(a,b)

print("Round 2!")
print(f"{p1} {p1p} / {p2} {p2p}")
a=int(input(f"{p1}'s choice (1/rat, 2/hunter and 3/lion): "))
b=int(input(f"{p2}'s choice (1/rat, 2/hunter and 3/lion): "))
print("")
print(f"{p1}")
case(a)
print("VS")
print("")
print(f"{p2}")
case(b)
check(a,b)
if p2p==2 or p1p==2 :
    print(f"{p1} {p1p} / {p2} {p2p}")
    if p1p>p2p:
        print(f"{p1} win!")
    elif p1p<p2p:
        print(f"{p2} win!")
else:
    print("Round 3!")
    print(f"{p1} {p1p} / {p2} {p2p}")
    a=int(input(f"{p1}'s choice (1/rat, 2/hunter and 3/lion): "))
    b=int(input(f"{p2}'s choice (1/rat, 2/hunter and 3/lion): "))
    print("")
    print(f"{p1}")
    case(a)
    print("VS")
    print("")
    print(f"{p2}")
    case(b)
    check(a,b)
    print(f"{p1} {p1p} / {p2} {p2p}")
    if p1p>p2p:
        print(f"{p1} win!")
    elif p1p<p2p:
        print(f"{p2} win!")
    else:
        print("Draw!")


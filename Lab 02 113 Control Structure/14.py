a=input("What's the result of Manchester city's match? ")
b=input("What's the result of Liverpool's match? ")
if a == "won" and b == "lost":
    print("Manchester city is the champion of Premier League.")
if b == "won" and a == "lost":
    print("Liverpool is the champion of Premier League.")
if a == b:
    c=input("What is the margin that Manchester city won by? ")
    d=input("What is the margin that Liverpool won by? ")
    if c>d:
        print("Manchester city is the champion of Premier League.")
    if d>c:
        print("Liverpool is the champion of Premier League.")
    if d==c:
        e=input("Which team won the play-off match?(Manchester city/Liverpool) ")
        print(e, "is the champion of Premier League.")

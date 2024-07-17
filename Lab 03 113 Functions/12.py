def eat(S,P,G):
    a = S//P
    b = (S%P)//G
    c = S-(S//P)*P-((S%P)//G)*G
    return a,b,c

S=int(input("Input starting food (S): "))
P=int(input("Input Paun's eating rate (P): "))
G=int(input("Input Gane's eating rate (G): "))
a,b,c=eat(S,P,G)
print(f"Paun eats {a} time(s)")
print(f"Gane eats {b} time(s)")
print(f"Remaining {c} for dog")

a=int(input("Insert amount of bottle of dragon's milk: "))
b=int(input("Insert amount of penguin's egg: "))
c=int(input("Insert amount of grimoire: "))
d=a*100+140*b+c*600
e=a*120+150*b+c*700
f=((e-d)/d)*100
print("The total cost price is",str(d)+".")
print("The total selling price is",str(e)+".")
print("The total profit is","%.2f" % f +"%")
if f<15:
    print("You can't make enough profit. You are fired!!")



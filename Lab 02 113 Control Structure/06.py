a=float(input("Enter buying amount: "))
if a>=3000 :
    print("Amount due after discount is",'{0:.2f}'.format(a*85/100), "baht.")
elif a>=1000:
    print("Amount due after discount is",'{0:.2f}'.format(a*90/100), "baht.")
else:
    print("Amount due after discount is",'{0:.2f}'.format(a*100/100), "baht.")
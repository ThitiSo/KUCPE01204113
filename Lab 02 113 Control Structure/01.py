a=int(input("Enter initial amount in Baht: "))
b=int(input("Enter interest rate in percent: "))
c=0
for i in range(1,21):
    a=a*(1+b/100)
    if i==1:
        print("Total amount after 1 year is",'{0:.2f}'.format(a),"Baht.")
    if i==5:
        print("Total amount after 5 years is",'{0:.2f}'.format(a),"Baht.")
    if i==10:
        print("Total amount after 10 years is",'{0:.2f}'.format(a),"Baht.")
    if i==20:
        print("Total amount after 20 years is",'{0:.2f}'.format(a),"Baht.")
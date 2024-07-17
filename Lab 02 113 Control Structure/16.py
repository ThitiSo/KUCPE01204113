a=int(input("How many TVs? "))
b=int(input("How many DVD players? "))
c=int(input("How many Audio Systems? "))

xbar=a*6000+b*1500+c*3000
print("Total price is", '{0:.2f}'.format(xbar),"baht.")
if xbar >= 24000:
    discount=xbar*20/100
    xbar=xbar*80/100
    print("You've got a discount of", '{0:.2f}'.format(discount), "baht.")
print("Your payment is", '{0:.2f}'.format(xbar), "baht. Thank you!")
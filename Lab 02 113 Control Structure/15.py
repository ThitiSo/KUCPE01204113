a=int(input("Input a: "))
b=int(input("Input b: "))
c=int(input("Input c: "))
d=int(input("Input d: "))
e=int(input("Input e: "))
xbar=(a+b+c+d+e)/5
print("mean:", '{0:.3f}'.format(xbar))
print("sd:",'{0:.3f}'.format(((((xbar-a)**2+(xbar-b)**2+(xbar-c)**2+(xbar-d)**2+(xbar-e)**2)/5)**(1/2))))
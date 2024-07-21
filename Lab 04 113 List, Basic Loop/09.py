a=int(input("How many food you have : "))
value=0
def plus(total,value):
    return total+value
def minus(total,value):
    return total-value
for i in range(a):
    b=input("").split()
    value+=int(b[0])*int(b[1])
print(value)
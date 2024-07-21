a=int(input("Enter a positive integer n: "))
print(f">call fac({a})")
def fac(n):
    a=1
    for i in range(n):
       a*=i+1
    return a
for j in range (a):
    print(" ",end="")
    for i in range (j+1):
        print(a-i,"* ",end="")
    print(f"fac({a-i-1})")
print(" ",end="")
for i in range (a):
    print(a-i,"* ",end="")
print(f"1")
print(f">fac({a})={fac(a)}")
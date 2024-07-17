def factorial(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a
value=0
n=int(input("Input k: "))
for i in range(1,n+1):
    print(f"{i}! = {factorial(i)}")
    value+=factorial(i)
print(f"Summation of factorial 1!-{n}! = {value}")
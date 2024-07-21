def factorial(n):
    a=1
    b=0
    if n==0:
        return 0
    else:
        for i in range(1,n+1):
            a*=i
            b+=a
        return b

n=int(input("Input k: "))
for i in range(1,n+1):
    print(f"{i}! = {factorial(i)-factorial(i-1)}")
print(f"Summation of factorial 1!-{n}! = {factorial(n)}")
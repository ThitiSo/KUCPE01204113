def fibo(n):
    a=[1,1]
    if n>2:
        for i in range (n-2):
            b=a[-2]+a[-1]
            a.append(b)
        return b
    else:
        return 1
n = int(input("Enter n: "))
print(f"fibo({n}) =",fibo(n))
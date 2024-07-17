n=int(input("Day: "))
a=[1,1]
if n>2:
    for i in range (n-2):
        b=a[-2]+a[-1]
        a.append(b)
for i in range (n):
    print(a[i],end=" ")
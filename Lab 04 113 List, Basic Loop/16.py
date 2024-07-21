def alter_sum(n):
    a=0
    for i in range (1,n+1):
        if i%2 == 1:
            a+=i
        else:
            a-=i
    return a

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n,alter_sum(n)))

n=int(input("N: "))
m=int(input("M: "))
coll=set()
for i in range (n):
    a=int(input(f"Input number {i+1}: "))
    coll.add(a%m)
print(len(coll))

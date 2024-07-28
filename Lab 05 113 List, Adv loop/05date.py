a=int(input("d: "))
b=int(input("m: "))-1
c=int(input("y: "))
month=[31,28,31,30,31,30,31,31,30,31,30,31]
if c%400==0:
    month[1]+=1
elif c%100==0:
    pass
elif c%4==0:
    month[1]+=1
day=0
for i in range(b):
    day+=month[i]
day=day+a
print(day)
        


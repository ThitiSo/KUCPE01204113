a=int(input(""))
b=int(input(""))
c=int(input(""))
d=[a,b,c]
while d[0]>d[1] or d[0]>d[2] or d[1]>d[2]:
    if d[0]>d[1]:
        d[0],d[1]= d[1],d[0]
    if d[1]>d[2]:
        d[1],d[2]= d[2],d[1]
    if d[0]>d[2]:
        d[0],d[2]= d[2],d[0]
print(d[0],d[1],d[2])

    

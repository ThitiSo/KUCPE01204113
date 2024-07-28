b=int(input("input: "))
if b % 2 !=0:
    b=b//2+1
else:
    b=b//2
z=0
for j in range(b):
    print(" "*(b-z-1)+"#"*(1+z*2))
    z+=1
z+=-2
for j in range(b):
    print(" "*(b-z-1)+"#"*(1+z*2))
    z+=-1
        


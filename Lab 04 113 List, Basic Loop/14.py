a=int(input(""))
b=int(input(""))
c=int(input(""))
prt=a
count=0
while prt<=b:
    if prt%c !=0:
        print(prt,prt%c,end=" " )
        count+=1
        prt+=1
    else:
        prt+=11
    if count==10:
        print("\n",end="")
        count=0

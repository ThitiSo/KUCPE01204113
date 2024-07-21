consec=""
countcon=0
current =0
incount=0
coll=[]
while True:
    a=int(input(""))
    coll.append(a)
    if a==0:
        break
    if current==a:
        incount+=1
        if incount>countcon:
            consec=a
            countcon=incount
    else:
        incount=1
    current=a
if consec=="":
    print(1)
    print(coll[0])
else:    
    print(countcon)
    print(consec)
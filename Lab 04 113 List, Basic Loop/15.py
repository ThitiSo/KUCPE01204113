consec=0
countcon=0
current =0
incount=0
while True:
    a=int(input(""))
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

print(countcon)
print(consec)
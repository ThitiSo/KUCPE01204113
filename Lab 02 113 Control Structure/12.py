b=int(input("How long have Buzz played ?: "))
c=b//60
if b%60>20:
    c=c+1
if c>=5:
    print("Total price is",int((c*900)*70/100),"baht.")
elif c==4:
    print("Total price is",int((c*900)*80/100),"baht.")  
elif c>=2:
    print("Total price is",int((c*900)*90/100),"baht.")  
else:
    print("Total price is",int(c*900),"baht.")  

a=1
b=0
coll=[]
gradecoll=[]
while a != "":
    a = input("Input student score (or just ENTER to finish): ")
    if a != "":
        coll.append(int(a))
average= sum(coll)/len(coll)
for i in coll:
    b+=(i-average)**2
sd=(b/(len(coll)-1))**(1/2)
print(f"Average score is {(average):.2f}")  
print(f"Standard deviation is {(sd):.2f}") 
for i in coll:
    if i >= average + 1.5*sd:
        gradecoll.append("A")
    elif i >= average + 1*sd:
        gradecoll.append("B+")
    elif i >= average + 0.5*sd:
        gradecoll.append("B")
    elif i >= average:
        gradecoll.append("C+")
    elif i >= average - 0.5*sd:
        gradecoll.append("C")
    elif i >= average - 1*sd:
        gradecoll.append("D+")
    elif i >= average - 1.5*sd:
        gradecoll.append("D")
    else:
        gradecoll.append("F")
for i in range(len(coll)):
    print(f"Student #{i+1} score: {coll[i]} grade: {gradecoll[i]}")
   

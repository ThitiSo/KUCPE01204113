a=1
coll=[]
while a != "":
    a = input("Input student score (or just ENTER to finish): ")
    if a != "":
        coll.append(int(a))
for i in range(len(coll)):
    print(f"Student #{i+1} score: {coll[i]}")
print(f"Average score is {(sum(coll)/len(coll)):.2f}")    
print(f"Minimum score is {min(coll)}")
print(f"Maximum score is {max(coll)}")
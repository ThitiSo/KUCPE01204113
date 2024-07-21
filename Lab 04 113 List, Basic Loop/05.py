a=1
coll=[]
while a != "":
    a = input("Input student score (or just ENTER to finish): ")
    if a != "":
        coll.append(int(a))
coll=sorted(coll,reverse=True)
for i in range(len(coll)):
    print(f"Rank #{i+1}: {coll[i]}")

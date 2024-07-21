a=input("Enter list of tuple: ").split()
coll,coll1,coll2=[],[],[]
for i in range(len(a)):
    for j in a[i]:
        res = tuple(map(int, a[i]))
    coll.append(res)
    coll2.append(a[i][-1])
    res=()
slist=sorted(coll2)
print("Input list:", coll)
newtuple=[]
for i in range(len(a)):
    for j in range(len(a)):
        if a[j][-1]==slist[i]:
            newtuple.append(coll[j])
print("Output list:", newtuple)



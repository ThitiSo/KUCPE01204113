a=int(input("initial index: "))
b=input("track chunk sizes: ").split()
coll=[]
tracksize=[]
for i in range(len(b)):
    coll.append([])
    tracksize.append(int(b[i]))
    for j in range(int(b[i])):
        coll[i].append(a)
        a+=1
for j in range(max(tracksize)):
    for i in range (len(coll)):
        if len(coll[i])!=0:
            print(coll[i][0],end=' ')
            coll[i].remove(coll[i][0])
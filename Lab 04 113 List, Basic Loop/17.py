A=int(input("A: "))
B=int(input("B: "))
C=int(input("C: "))
coll=[A,B,C]
alpha=["A","B","C"]
index=[0,1,2]
i=1

while coll[0]+coll[1]+coll[2]!=1:
    indexcopy=index[:]
    count=0
    while count<2: 
        for j in range(len(coll)):
            if coll[j] == max(coll):
                indexcopy.remove(j)
                coll[j]-=1
                count+=1
                #print(coll,j,count,indexcopy)
                if count==2:
                    break
    coll[indexcopy[0]]+=1
    #print(coll,j,count,indexcopy)
print(alpha[coll.index(max(coll))])
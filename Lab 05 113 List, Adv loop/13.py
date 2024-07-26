A =  list(enumerate(list(map(int,input().split()))))
kill=[]
count=0
for i in A:
    for j in A:
        if i[1]+j[1]== 4 and i!=j and (i[0] not in kill and j[0] not in kill):
            kill.append(i[0])
            kill.append(j[0])
            count+=1

    for j in A:
        if i[1]+j[1]== 3 and i!=j and (i[0] not in kill and j[0] not in kill):
            kill.append(i[0])
            kill.append(j[0])
   
            count+=1

for j in A:
    inbox=0
    for i in A:
        if inbox+i[1]<= 4 and i[0] not in kill:
            kill.append(i[0])
            inbox+=i[1]
            print(i,inbox,kill)
    if inbox !=0:
        count+=1
for i in A:
    if i[0] not in kill:
        count+=1
print(count)
            
            
            

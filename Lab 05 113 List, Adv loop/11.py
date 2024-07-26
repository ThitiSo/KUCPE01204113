a=int(input())
coll,ans=[],[]
deadzone,zombie=[],[]
for i in range(a):
    b=input()
    coll.append(b)

for i in range(a):
    for j in range(len(coll[i])):
        if coll[i][j] == "G":
            deadzone.append([i,j])
        elif coll[i][j] == "E":
            zombie.append([i,j])
count=0
for i in zombie:
    ans.append(0)
    for j in deadzone:
        if (i[0]<= j[0] +2 and i[0]>= j[0]-2) and (i[1]<= j[1] +2 and i[1]>= j[1]-2):
            #print(i[0],j[0])
            ans[count]=1
        
    count+=1
print(sum(ans))
            

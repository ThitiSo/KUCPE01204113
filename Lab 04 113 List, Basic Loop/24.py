# Enter list of number: 0 3 4 7 9
# Output list: [[0, 3], [4, 7]]

a=input("Enter list of number: ").split()
coll=[]
ans=[]
for i in a:
    coll.append(int(i))
for i in coll:
    if i+3 in coll:
        ans.append([i,i+3])
print("Output list:",ans)

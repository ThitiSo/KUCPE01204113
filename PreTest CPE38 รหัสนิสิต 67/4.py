coll=[0,1]
n=int(input("จำนวนขั้นบันได : "))
for i in range (n):
   coll.append(coll[-1]+coll[-2])
print(coll[-1])
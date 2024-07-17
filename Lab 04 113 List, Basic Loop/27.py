# InputList: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
import ast
a=input("InputList: ")
flat=ast.literal_eval(a)
coll=[]
current=""
for i in range(len(flat)):
    if current==flat[i]:
        incoll.append(current)
    else:
        if i!=0:
            coll.append(incoll)
        incoll=[]
        current=flat[i]
        incoll.append(flat[i])
coll.append(incoll)
print(coll)
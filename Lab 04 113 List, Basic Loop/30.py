# Input: [[1,3],[1,3],[13,15,17],[5,7],[9,11],[9,11],[9,11],[5,7]]
# [9, 11]: 3 
# [1, 3]: 2 
# [5, 7]: 2 
# [13, 15, 17]: 1
import ast
a=input("Input: ")
a=ast.literal_eval(a)
current=[]
count=[]
for i in range(len(a)):
    if a[i] in current:
        count[current.index(a[i])]+=1
    else:
        current.append(a[i])
        count.append(1)
    # print(a[i],current,count)
for i in range (len(current)):
    print(f"{current[i]}: {count[i]}")
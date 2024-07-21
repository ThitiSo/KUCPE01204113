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
mx=max(count)
for i in range (len(current)):
    # print(current,count)
    for j in range(len(current)):
        if count[j]==mx :
            # print(current,count)
            print(f"{current[j]}: {count[j]}")
            current.remove(current[j])
            count.remove (count[j])
            if mx not in count:
                mx-=1
            break

            
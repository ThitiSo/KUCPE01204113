a = input("String set1: ")
a=eval(a)
b = input("String set2: ")
b=eval(b)
atz="abcdefghijklmnopqrstuvwxyz"
ans=[]
for j in a:
    for k in b:
        for i in atz:
            if i not in j+k:
                break
            if i=="z" and i in j+k:
                ans.append(j+k)
print("Output:",len(ans))
print("The total complete pairs that are forming are:")
for i in ans:
    print("",i)

        

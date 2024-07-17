a=input("Enter a set of strings: ").split()
coll=[]
for i in range(len(a)):
    coll.append(a[i])
def countStr(l):
    alpha=[]
    count=[]
    for i in range(len(l)):
        inalpha=[]
        for j in range(len(l[i])):
           
            if l[i][j] not in alpha:
                alpha.append(l[i][j])
                count.append(1) 
            if l[i][j] not in inalpha:
                inalpha.append(l[i][j])
                count[alpha.index(l[i][j])]+=1
            #print(alpha,inalpha,count)
    return max(count)
print(countStr(coll))
            
x,y=input(f"Grid Size: ").split()
x,y=int(x),int(y)
nom=int(input(f"Number of mine(s): "))

minefield=[]
for i in range(y):
    minefield.append([])
    for j in range(x):
        minefield[i].append(0)
# print(minefield)
for i in range(nom):
    miney,minex=input(f"Mine#{i+1}: ").split()
    miney,minex=int(minex),int(miney)
    minefield[miney][minex]="X"
    for j in [1,0,-1]:
        for k in [1,0,-1]:
            if minex+k>len(minefield[0])-1 or minex+k<0:
                continue
            if miney+j>len(minefield)-1 or miney+j<0:
                continue            
            try:
                minefield[miney+j][minex+k]+=1
            except:
                pass
            # print(minefield)
for i in minefield:
    for j in i:
        print(j,end=" ")
    print("\n",end="") 

i1=input("ผลการสำรวจ: ").split()
print("แผนที่:")
intlist,intcopy=[],[]
level,levelcopy=[],[]
for i in i1:
    intlist.append(int(i))
    intcopy.append(int(i))
    level.append(0)
    levelcopy.append(0)
a=max(intlist)
for i in range(max(intlist)):
    for j in range (len(intlist)):
        if intlist[j] == a:
            if level[j]<4:
                print("o",end="")
            elif level[j]<8:
                print("=",end="")
            else:
                print("x",end="")
            intlist[j]-=1
            level[j]+=1
        else:
            print(" ",end="")
    print("\n",end="")
    a-=1
print("อาจารย์โตโต้เดินทางไปปักธงที่จุดยอดสูงสุด:")
flag1=[["+","-","-","-","-","-","-","-","+"],
["|"," ","C","P","E","3","8"," ","|"],
["+","-","-","-","-","-","-","-","+"]]
indexmax=intcopy.index(max(intcopy))

for i in range (3):
    print(" "*(indexmax),end="")
    for j in range (len(intcopy)-indexmax):
        if j >= len(flag1[i]):
            pass
        else:
            print(flag1[i][j],end="")
    print("\n",end="")
for i in range(3):
    print(" "*(indexmax),end="")
    print("|",end="")
    print("\n",end="")


a=max(intcopy)
for i in range(max(intcopy)):
    for j in range (len(intcopy)):
        if intcopy[j] == a:
            if levelcopy[j]<4:
                print("o",end="")
            elif levelcopy[j]<8:
                print("=",end="")
            else:
                print("x",end="")
            intcopy[j]-=1
            levelcopy[j]+=1
        else:
            print(" ",end="")
    print("\n",end="")
    a-=1

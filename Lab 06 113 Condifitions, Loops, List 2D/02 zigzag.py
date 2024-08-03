
a=input("Input sentence: ")
b=int(input("Input row: "))
coll=[[a[0]]]
for i in range(b-1):
    coll.append([])
row=0
down=True
for i in a[1:]:
    if down== True and row==b-1:
        down=False
    elif down == False and row==0:
        down=True 
    if down == True:
        row+=1
    if down == False:
        row-=1
    coll[row].append(i)
    # print(row,coll,down)
for i in coll:
    for j in i:
        print(j,end="")


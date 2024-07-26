def getMultilinesInput():
    text = ""
    while True:
        line = input().lower()
        if not line:
            break
        text += line + ' '
    return text


print("Parse a long paragraph (or text) below, following an ENTER as needed:")
ss = getMultilinesInput().lower()
k = int(input("Top K rank: "))
coll=ss.split()
dup={}
pos=0

while True:
    if coll[pos] not in dup.keys():
        dup[coll[pos]]=1
    elif coll[pos] in dup.keys():
        dup[coll[pos]]+=1
    pos+=1

    if pos>=len(coll):
        break
count=0
z=0
zin=""
newline=False
while count<=k-1:
    for i in dup.keys():
        if dup[i]==len(coll)-z:
            if zin==z:
                print(f", {i}: {dup[i]}",end="")
                
            else:
                count+=1
                print(f"{i}: {dup[i]}",end="")
                newline=True
            zin=z
        
    if newline == True:
        print("\n",end="")
        newline=False
    if 1==len(coll)-z:
        break
    z+=1
   



Shift=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Lower=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a=input("Enter text: ").split()
b=int(input("Enter step: "))
ans=""
for i in range (len(a)):
    for j in range(len(a[i])):
        if a[i][j].islower():
            ans=ans+Lower[((Lower.index(a[i][j]))+b)%26]
        elif a[i][j].isupper():
            ans=ans+Shift[((Shift.index(a[i][j]))+b)%26]
        elif a[i][j]==".": 
            ans=ans+"."
    if i != len(a)-1:
        ans=ans+" "
print(ans)
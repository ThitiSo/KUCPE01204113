y=int(input("Enter horizontal shift size: "))
x=int(input("Enter vertical shift size: "))
print("Enter image:")
img=[]
while True:
    a=input()
    if a == "-1":
        break
    img.append(a)
print("After shift:")
real=[]
for i in range(x):
    real.append("0"*len(img[1]))
for i in range(len(img)-x):
    real.append("0"*y+img[i][:len(img[1])-y])
for i in real:
    for j in i:
        print(j,end="")
    print("\n",end="")
    

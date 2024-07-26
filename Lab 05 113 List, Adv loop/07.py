a = input("Enter lucky number : ")
b= int(input("Enter amount of candidates : "))
coll=[]
win=[]
for i in range(b):
    x=input(f"Enter ID card number {i+1}: ")
    coll.append(x)
z=0
for i in coll:
    win.append(0)
    for j in i:
        if j == a:
            win[z]+=1
    z+=1

real=[]
for i in range(len(win)):
    if win[i] == max(win):
        real.append(i)

num=0
for i in real:
    if num< int(coll[i]):
        num=int(coll[i])

print(f"Winner: {num}")

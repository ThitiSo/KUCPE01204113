a,b = input().split()
a=int(a)
b=int(b)
c=[]
for i in range(a):
    hu=int(input())
    c.append(hu)
time=0
coll=c[:]
while b>0:
    time+=1
    for i in range(a):
        coll[i]=coll[i]-1
        if coll[i]==0:
            coll[i]=c[i]
            b-=1
print(time)

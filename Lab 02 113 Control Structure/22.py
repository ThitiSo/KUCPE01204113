a=int(input("How many day : "))
b=[]
for i in range (1,a+1):
    c=float(input("Input price in day {i} : ".format(i=i)))
    b.append(c*(96-i)/100)
print("Summary price =",'{0:.2f}'.format(sum(b)))
a=int(input("Estimated time : "))
least=a*2.5
week = a//8
check=[a*2.5,a*2.5,a*2.5]
for i in range (week):
    print(f"Week{i+1}")
    physical=int(input("Physical therapy : "))
    check[0]=check[0]-physical
    weight=int(input("Weight training : "))
    check[1]=check[1]-weight
    Fitness=int(input("Fitness training : "))
    check[2]=check[2]-Fitness
if check[0] > 0:
    print("Buzzy has not recovered in time.")
elif check[1] > 0:
    print("Buzzy has not recovered in time.")
elif check[2] > 0:
    print("Buzzy has not recovered in time.")
else:
    print("Buzzy has recovered in time.")
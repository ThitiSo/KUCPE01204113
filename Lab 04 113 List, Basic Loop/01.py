a=1
coll=[]
while a != "":
    a = input("Enter a number (to quit, just [Enter]): ")
    if a != "":
        coll.append(float(a))
if coll!=[]:    
    print(f"The maximum is {max(coll):.2f}")
    print(f"The minimum is {min(coll):.2f}")
    print(f"The average is {(sum(coll)/len(coll)):.2f}")
else:
    print("Nothing to do.")
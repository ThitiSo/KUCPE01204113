a = input("Input list1: ")
a= eval(a)
b = input("Input list2: ")
b= eval(b)
col1=[]
for i in a:
    if i not in b:
        col1.append(i)
col2=[]
for i in b:
    if i not in a:
        col2.append(i)
print(f"Missing values in list1 = {col2}\nAdditional values in list1 = {col1}\nMissing values in list2 = {col1}\nAdditional values in list2 = {col2}")
        
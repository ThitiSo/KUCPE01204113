a = input("Input string: ")
b = input("Input string: ")
col1=""
for i in a:
    if i not in b:
        col1+=i
for i in b:
    if i not in a:
        col1+=i
print(f"{col1}")
        

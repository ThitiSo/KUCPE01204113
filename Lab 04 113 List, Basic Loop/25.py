# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

import ast
a= input("Original list: ")
flat=[]
def flatin(str):
    global flat
    for i in str:
        if type(i) == type([1,2]):
            flatin(i)
        else:
            flat.append(i)
    return flat
print(flatin(ast.literal_eval(a)))
        

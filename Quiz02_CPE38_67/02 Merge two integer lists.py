def getInput():
    a = eval(input('Enter list a: '))
    b = eval(input('Enter list b: '))
    return a,b

a,b=getInput()


def merge(a,b):
    for i  in b:
        a.append(i)
    for j in range(len(a)):
        for i in range (len(a)-1):
            if a[i] > a[i+1]:
                a[i],a[i+1]= a[i+1] , a[i]
    return a
res = merge(a,b)
print(res)
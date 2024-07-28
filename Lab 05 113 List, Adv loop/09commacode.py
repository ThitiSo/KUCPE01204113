def commaCode(mylist):
    coll=mylist
    if len(coll)==1:
        return coll[-1]
    elif len(coll)==0:
        return ""
    else:
        ans=""
        for i in coll:
            if i == coll[-1]:
                ans+=f"and {i}"
            else:
                ans+=f"{i}, "
        return ans  
a=input("Input: ")
print(commaCode(a.split()))

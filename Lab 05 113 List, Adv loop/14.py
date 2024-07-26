a = input("Enter a list of objects: ")
a= eval(a)
def countConsec(flat):
    if len(flat)==0:
        return "Nothing to do."
    else:
        ans=[]
        count=0
        current=None
        for i in flat:
            if current!=i:
                if current != None:
                    ans.append((current,count))
                current = i
                count=0
            if current == i:
                count+=1 
            # print(ans) 
        ans.append((current,count))
        # print(ans)
    return ans
# print(countConsec(a))
max_value=0
count_max=0
if len(a)==0:
    print("Nothing to do.")
else:
    for i in countConsec(a):
        # print(i[1])
        if i[1]>count_max:
            max_value=i[0]
            count_max=i[1]
    print(max_value)
    print(count_max)
        
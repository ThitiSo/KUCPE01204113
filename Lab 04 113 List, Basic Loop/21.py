a=input("Enter a set of strings: ").split()
def countStr(l):
    count=0
    for i in l:
        if len(i)>1:
            if i[0]==i[-1]:
                count+=1
    return count
print(countStr(a))
            

# a=input("Enter a set of strings: ").split()
# coll=[]
# for i in range(len(a)):
#     coll.append(a[i])
# def countStr(l):
#     alpha=[]
#     count=[]
#     for i in range(len(l)):
#         inalpha=[]
#         for j in range(len(l[i])):
#             if len(l[i])<2:
#                 pass
#             else:
#                 if l[i][j] not in alpha:
#                     alpha.append(l[i][j])
#                     count.append(0) 
#                 if l[i][j] not in inalpha:
#                     inalpha.append(l[i][j])
#                     count[alpha.index(l[i][j])]+=1
           
#     return max(count)
# print(countStr(a))
            
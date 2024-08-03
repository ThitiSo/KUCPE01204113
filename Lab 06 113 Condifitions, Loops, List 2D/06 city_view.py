a,b = input("City Size: ").split()
a,b = int(a),int(b)
first_array=[]
for i in range(a):
    first_array.append([])
    inarray= input().split()
    for j in range(b):
        first_array[i].append(int(inarray[j]))
# print(first_array)

#West side
count_west=0
for i in first_array:
    current=0
    for j in i:
        if j > current:
            current= j
            count_west+=1
            
#East side
count_east=0
for i in first_array:
    current=0
    for j in range(len(i)-1,-1,-1):
        if i[j] >current:
            # print(current,i[j])
            current=i[j]
            count_east+=1
    # print("Change Column")
#North Side
count_north = 0
for i in range(len(first_array[0])):
    current=0
    for j in range(len(first_array)):
        if first_array[j][i]> current:
            #print(current,first_array[j][i])
            current=first_array[j][i]
            count_north+=1
    #print("Change Column")
            

#South Side
count_south= 0
for i in range(len(first_array[0])):
    current=0
    for j in range(len(first_array)-1,-1,-1):
        if first_array[j][i]>current:
            current=first_array[j][i]
            count_south+=1
max_count=max(count_east,count_west,count_north,count_south)
if count_north==max_count:
    print("N",end=" ")
if count_south==max_count:
    print("S",end=" ")
if count_east== max_count:
    print("E",end=" ")
if count_west==max_count:
    print("W",end=" ")

# print(count_east,count_west,count_north,count_south)
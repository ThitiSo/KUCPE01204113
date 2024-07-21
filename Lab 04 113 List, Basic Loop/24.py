# Enter list of number: 0 3 4 7 9
# Output list: [[0, 3], [4, 7]]

a = input("Enter list of number: ").split()
coll = []
ans = []

for i in a:
    coll.append(int(i))
for i in coll:
    if i + 3 in coll and [i, i + 3] not in ans and [i + 3, i] not in ans:
        ans.append([i, i + 3])
    if i - 3 in coll and [i, i-3] not in ans and [i - 3, i] not in ans:
        ans.append([i, i-3])

print("Output list:", ans)

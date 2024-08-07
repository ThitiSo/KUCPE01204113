n=int(input(""))
print("."*n)
for i in range(int((n-3)/2)):
    print("."+" "*(i)+"."+" "*(n-4-2*i)+"."+" "*(i)+".")
print("."+" "*int((n-3)/2)+"."+" "*int((n-3)/2)+".")
for i in range(int((n-5)/2),-1,-1):
    print("."+" "*(i)+"."+" "*(n-4-2*i)+"."+" "*(i)+".")
print("."*n)

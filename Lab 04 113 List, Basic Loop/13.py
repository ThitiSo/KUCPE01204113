pole,crim,i=0,100,1
while pole < crim:
    pol=int(input("Input distance: "))
    pole+=pol
    print(f"Police distance: {pole}")
    crim+=2*i
    print(f"Criminal distance: {crim}")
    i+=1
print("Caught him!")
a=int(input("Distance from starting point(m.): "))
count=0
initial=0
if initial==a:
    print(0,end="")
while initial!= a:
    while initial < a:
        print(initial+5, end=" ")
        print(initial+3, end=" ")
        initial+=3
        count+=1
    while initial > a:
        print(initial-4, end=" ")
        print(initial-1, end=" ")
        initial+=-1
        count+=1
print(f"\nBuzz moved {count} set(s)")

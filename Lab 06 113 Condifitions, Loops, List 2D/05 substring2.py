# Text: acabababababcbabab
# Substring: aba
# ac[aba]b[aba]babcb[aba]b
a=list(map(str,input("Text: ")))
b=list(map(str,input("Substring: ")))
b_in_a=False
for i in range(len(a)-len(b)):
    sub=True
    insub=""
    for j in range(len(b)):
        if a[i+j] != b[j]:
            sub=False
            break
        elif a[i+j] == b[j]:
            sub=True
            insub+=a[i+j]
    if sub == True:
        for k in range(len(b)):
            a[i+k]=""
        b_in_a=True
        a[i]=f"[{insub}]"

if b_in_a == False:
    lista=[]
    for i in range(len(b)):
        c=b[:]
        c[i]="?"
        lista.append(c)
    
    for i in range(len(a)-len(b)):
        

        for k in lista:
            sub=True
            insub=""
            for j in range(len(k)):
                if k[j] =="?":
                   insub+="?"
                elif a[i+j] != k[j]:
                    sub=False
                    break
                elif a[i+j] == k[j]:
                    sub=True
                    insub+=a[i+j]
            if sub == True:
                for j in range(len(k)):
                    a[i+j]=""
                b_in_a=True
                a[i]=f"[{insub}]"
    


for i in a:
    print(i,end="")




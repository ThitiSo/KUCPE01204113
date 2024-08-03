max_word=0
b=list(map(str,input("Text: ").split()))
# print(b)
z=0
chain=1
current=0
stop=len(b)
count_stop=0
# for i in range(len(a)):
while True:
    
    a=b[z:len(b)]
    # print(a)
    word=1
    for j in range(len(a)-1):
        count=0
        for k in range(len(a[j])):
            if a[j][k] == a[j+1][k]:
                count+=1
            # print("count",a[j],a[j+1],count)
        z+=1
        if count>=len(a[j])-2:
            word+=1
        else:
            chain+=1
            break
        # print("word",word,count)
    
    if word> max_word:
        max_word=word
    # print("max_word",word,max_word)
    if max_word>current:
        current=max_word
        # print("break chain")
    count_stop+=1
    if stop == count_stop:
        break
print(f"{chain} Chain(s). Maximum length is {max_word} word(s).")
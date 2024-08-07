max_word=0
word=1
b=list(map(str,("SUN TON BOW GOD LOT KID FAX BAT FAT CAR EAT FEE SEA MAP DRY SPY TAP").split()))
chain=1
for i in range(len(b)-1):
    correct_pos=0
    for j in range(len(b[i])):
        if b[i][j]==b[i+1][j]:
            correct_pos+=1
    # print(b[i],b[i+1],correct_pos)
    if correct_pos>= len(b[i])-2:
        word+=1
    else:
        word=1
        chain+=1
    if word> max_word:
        max_word=word
    # print(word,max_word)
print(f"{chain} Chain(s). Maximum length is {max_word} word(s).")

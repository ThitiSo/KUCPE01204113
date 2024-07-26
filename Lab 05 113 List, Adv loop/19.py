a=input("Enter a string: ").lower().split()
vowel=["a","e","i","o","u"]
vowelset=[]
conset=[]
for i in a:
    for j in i:
        if j in vowel and j not in vowelset:
            vowelset.append(j)
        elif j not in vowel and j not in conset:
            conset.append(j)

print(f"Unique vowels:  {vowelset}\nUnique consonants:  {conset}")
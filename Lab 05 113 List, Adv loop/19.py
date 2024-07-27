a=input("Enter a string: ").lower().split()
vowel=["a","e","i","o","u"]
Lower=[ 'b', 'c', 'd', 'f', 'g', 'h',  'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowelset=[]
conset=[]
for i in a:
    for j in i:
        if j in vowel and j not in vowelset:
            vowelset.append(j)
        elif j in Lower and j not in conset:
            conset.append(j)

print(f"Unique vowels:  {vowelset}\nUnique consonants:  {conset}")

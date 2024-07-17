s=int(input("s: "))
def caltime(s):
    a = s//3600
    b = (s-(a*3600))//60
    c = s%60
    return a,b,c
a,b,c=caltime(s)
print(f"{s} seconds equals {a} hour(s) {b} minute(s) and {c} second(s)")
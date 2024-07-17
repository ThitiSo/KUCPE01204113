def digit(n):
    return int(str(n)[-1])
def tens(n):
    if len(str(n))>1:
        return int(str(n)[-2])
    else:
        return 0
def hundreds(n): 
    if len(str(n))>2:
        return int(str(n)[-3])
    else:
        return 0
def thousands(n):
    if len(str(n))>3:
        return int(str(n)[-4])
    else:
        return 0
def sum_digits(n):
    return int(digit(n))+int(tens(n))+int(hundreds(n))+int(thousands(n))
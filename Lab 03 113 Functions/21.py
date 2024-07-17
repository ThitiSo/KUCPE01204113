import math
def nb_year(p0, percent, aug, p):
    a=0
    while p0<p:
        p0=math.floor(p0+p0*percent/100+aug)
        a+=1
    return a
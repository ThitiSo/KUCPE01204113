def isPrime(number):

    
    value= True
    if number == 2:
        return True
    for i in range(2,number-1):
        if number%i==0:
            value = False
    return value



def printAllPrimes(limit):

  
    
    coll=""
    for i in range (2,limit+1):
        if isPrime(i):
            coll+=f"{i} "
    print(coll)
    return coll



number = int(input("Input n: "))
printAllPrimes(number)

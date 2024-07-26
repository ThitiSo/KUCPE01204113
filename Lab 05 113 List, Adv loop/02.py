def list_factors(n):

   
    coll=""
    for i in range (1,n+1):
        if n%i==0:
            coll+=f"{i} "

    return coll



def find_sum_and_num_factors(n):
  
   
    coll=0
    count=0
    for i in range (1,n+1):
        if n%i==0:
            coll+=i
            count+=1

    return coll,count


def isPrime(number):

    value= "is"
    if number == 1:
        return "is not"
    if number == 2:
        return "is"
    for i in range(2,number-1):
        if number%i==0:
            value = "is not"
    return value

a=int(input("Enter positive number: "))
print(f"Factors of {a} are")
print(list_factors(a))
coll,count=find_sum_and_num_factors(a)
print(f"Sum of {list_factors(a)}is {coll}")
print(f"Number of factors is {count}")
print(f"{a} {isPrime(a)} prime number.")


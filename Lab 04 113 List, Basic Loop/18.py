def count_digits(number):

    i,count=0,0
    if number==0:
        count=1
    if number<0:
        number=-number
    while number//(10**i) != 0 :
        count+=1
        i+=1

    return count

# Main
number = int(input("Enter number: "))
print(f"There are {count_digits(number)} digits in {number}")
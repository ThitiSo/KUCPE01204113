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


def get_last_digit(n):
    """
    Get last digit in number
    :params number is an integer
    :return last digit in number

    >>> get_last_digit(41)
    1
    >>> get_last_digit(394)
    4
    >>> get_last_digit(1020)
    0
    """
    if count_digits(n) == 1:
        return n

    return n-(10*(n//10))


def get_distribution(number):
    """
    Return string showing distribution of number
    :params number (int): a number to find distribution
    :return string
    >>> get_distribution(21)
    '1x10^0 + 2x10^1'
    >>> get_distribution(306)
    '6x10^0 + 0x10^1 + 3x10^2'
    >>> get_distribution(12201)
    '1x10^0 + 0x10^1 + 2x10^2 + 2x10^3 + 1x10^4'
    """
    for i in range(count_digits(number)):
        prt=get_last_digit(number)
        number=(number-prt)/10
        print(f"{prt}x10^{i}",end= " ")
    return ""
   


# Main
number=int(input("Input number: "))
print(f"{number} = ",end="")
print(get_distribution(number))
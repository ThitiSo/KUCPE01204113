a=int(input("Enter your age: "))
b=int(input("Enter your net income: "))
if a > 60 or a <15:
    print("Invalid age.")
else:
    if b>79999:
        print( "Invalid income." )
    else:
        if b<=30000:
            c=b*20/100
        else:
            c=30000*20/100-((b-30000)*12/100)
        print('Your negative income tax is {} Baht.'.format('{0:.2f}'.format(c)))
        

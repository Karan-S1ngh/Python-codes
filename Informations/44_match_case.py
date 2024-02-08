# a new addition from python 3.10 onwards is the match case statement

# match case statement is used to compare the value of a variable with multiple values
# It is similar to switch case statement in other programming languages

# example
x = int(input("Enter a number: "))
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case 4:
        print("x is 4")
    case 5:
        print("x is 5")
    case _ if x == 0:
        print("x is 0")
    case _ if x > 5 and x < 10:
        print("x is not 1, 2, 3, 4, or 5  but less than 10 ")
    case _:
        print("x is not 1, 2, 3, 4, 5, 0, or less than 10")    
    # case _ is used to match any value(default case)
    # there can be multiple case _ statements in a match case statement
# here break statement is not required as the match case statement automatically breaks after the first match




'''OUTPUT
Enter a number: 5
x is 5

Enter a number: 0
x is 0

Enter a number: 10
x is not 1, 2, 3, 4, or 5  but less than 10

Enter a number: 11
x is not 1, 2, 3, 4, 5, 0, or less than 10
'''    

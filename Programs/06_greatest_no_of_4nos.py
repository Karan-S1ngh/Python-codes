# Find greatest number among of the 4 numbers given as input by the user

# Two ways to do this

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
d = int(input("Enter 4th number : "))

# First method
if (a > b):
    if (a > c):
        if (a > d):
            print("1 : 1st number is greatest")
        else:
            print("1 : 4th number is greatest")
    else:
        if (c > d):
            print("1 : 3rd number is greatest")
        else:
            print("1 : 4th number is greatest")
else:
    if (b > c):
        if (b > d):
            print("1 : 2nd number is greatest")
        else:
            print("1 : 4th number is greatest")
    else:
        if (c > d):
            print("1 : 3rd number is greatest")
        else:
            print("1 : 4th number is greatest")


# Second method (easier way)           
if(a>b):
    f1 = a
else:
    f1 = b
    
if(c>d):
    f2 = c
else:
    f2 = d
    
if(f1>f2):
    print("2 :",f1,"is greatest")
else:
    print("2 :",f2,"is greatest")
    



'''OUTPUT
Enter 1st number : 5
Enter 2nd number : 6
Enter 3rd number : 4
Enter 4th number : 1
1 : 2nd number is greatest
2 : 6 is greatest
'''

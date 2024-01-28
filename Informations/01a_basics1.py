# to comment out multiple together using # then use (ctrl+/)

# This is a single line comment 

''' This is a 
multi line comment'''

print("1  : Hello")    # we use "" if we have '' in the string


print('''2  : Hi
How are you''')
# prints multiple line

print()
# prints a blank line

'''
PascalCase and camelCase are two types of methods to represent a variable,etc
PascalCase = First letter of every word is capital
camelCase = First letter of every word except first word is capital
'''

a = "Karan"
b = 'Singh'
c = '''Karan 
Singh'''                     # used when both '' and "" are used in string and/or the string is multi-line
d = 9
e = 9.8
f = True
g = None
h = False
# no need to specify datatype, python automatically decides the correct datatype

print("3  :",type(a),type(e))
# prints the type of variable

print("4  : Value of 6+4 is", 10)
print("5  : Value of 5+4 is", 5+4)
 
print("6  :",14>7)     # will print true if correct and false if incorrect

# Logical operation not,and,or
# and = true if both operands are true else false
# or = true if any one operand is true else false
# not = true if operand is false else true
print("7  :",not h)
print("8  :",not g)
print("9  :",not f) 
print("10 :",f and h)           # and = true if both operands are true else false
print("11 :",f or h)            # or = true if any one operand is true else false
print("12 :",f and g)
print("13 :",f or g)
print("14 :",h and g)   
print("15 :",h or g)
# we can use & in place of and and | in place of or   

print("16 :",int(e))          # typecasting
print("17 :",int("33"))       # string to integer
print("18 :",float(45))       # int to float

i = input("Enter your name : ")           # Takes input and stores in variable 'i' 
print("19 : Name is ",i)
print("20 :",type(i))
# It stores the input taken in form of a string

# i = int(i) or i = int(input("Enter number"))     
# This makes the input i to be int only
# to make it float only use float instead of int 
# same for other datatypes

# int('32') = 32
# String to int conversion

# str(32) = "32"
# Int to string conversion

# float(32) = 32.0
# Int to float conversion

# float('32') = 32.0
# String to float conversion

# str(32.0) = "32.0"
# Float to string converson 

# Can also print mathematical functions
import math
print("21 :",math.sin(90))         # prints value of sin 90 in radian
print("22 :",math.pi)              # prints value of pi upto certain decimal points
print("23 :",math.e)               # prints value of e upto certain decimal points
print("24 :",math.sqrt(25))        # prints square root of 5
print("25 :",math.log2(10))        # prints value of log of 10 to the base 2
print("26 :",math.factorial(5))    # prints factorial of 5


# f is used if u dont want to indicate string everytime differently while printing
# f is used to print the value of variable in the string
print(f"27 : Sum of {3} and {4} is {3+4}")


# By default new line is printed at the end of print statement
# To avoid this, use end="" in print statement
print("28 : Hello    ", end="")
print("29 : Hi")
print("30 : How are you")


import random
n = random.randint(1,4)
# prints random integer between 1 and 4


# to print power of a number we use **
print("31 : 2 raised to power 3 is equal to ",2**3)
# prints 2 to the power 3


# floor division
# prints integer value of division
print("32 : Floor division of 9 by 2 is",9//2)


# \n for new line
# \t for printing tab
# \' for '
# \" for "
# \\ for \
# \b for backspace
 
 


''' OUTPUT
1  : Hello
2  : Hi
How are you

3  : <class 'str'> <class 'float'>
4  : Value of 6+4 is 10
5  : Value of 5+4 is 9
6  : True
7  : True
8  : True
9  : False
10 : False
11 : True
12 : None
13 : True
14 : False
15 : None
16 : 9
17 : 33
18 : 45.0
Enter your name : Karan
19 : Name is  Karan
20 : <class 'str'>
21 : 0.8939966636005579
22 : 3.141592653589793
23 : 2.718281828459045
24 : 5.0
25 : 3.321928094887362
26 : 120
27 : Sum of 3 and 4 is 7
28 : Hello    29 : Hi
30 : How are you
31 : 2 raised to power 3 is equal to  8
32 : Floor division of 9 by 2 is 4
'''

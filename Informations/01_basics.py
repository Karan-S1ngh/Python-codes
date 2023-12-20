# to comment out multiple together using # then use (ctrl+/)

# This is a single line comment 

''' This is a 
multi line comment'''

print("1  : Hello")    # we use "" if we have '' in the string

print('''2  : Hi
How are you''')
# prints multiple line

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
print("7  :",not h)
print("8  :",not g)
print("9  :",not f) 
print("10 :",f and h) 
print("11 :",f or h)     
print("12 :",f and g)
print("13 :",f or g)
print("14 :",h and g)   
print("15 :",h or g)   

print("16 :",int(e))   # typecasting
print("17 :",int("33"))       # string to integer
print("18 :",float(45))       # int to float

i = input("Enter your name : ")           # Takes input and stores in variable 'i' 
print("19 : Name is ",i)
print("20 :",type(i))
# It stores the input taken in form of a string

# i = int(i)       
# This makes the input i to be int only

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
'''

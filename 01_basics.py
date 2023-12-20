# to comment out multiple together using # then use (ctrl+/)

# This is a single line comment 

''' This is a 
multi line comment'''

print("Hello")    # we use "" if we have '' in the string

print('''Hi
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

print(type(a),type(e))
# prints the type of variable

print("Value of 6+4 is", 10)
print("Value of 5+4 is", 5+4)
 
print(14>7)     # will print true if correct and false if incorrect

print(not h, f and h, f or h, f and g, h and g, f or g, h or g, not h)  
# Logical operation not,and,or(True, False, True, None, False, True, None, True)

print(int(e))   # typecasting
print(int("33"))       # string to integer
print(float(45))       # int to float

i = input("Enter your name : ")           # Takes input and stores in variable 'i' 
print(i)
print(type(i))
# It stores the input taken in form of a string
i = str(i)       #this makes the input i to be string only
i = int(i)       #this makes the input i to be int only   

# \n for new line
# \t for printing tab
# \' for '
# \" for "
# \\ for \
# \b for backspace
 
# Functions 
# two types : built-in and user defined
# built-in functions are already defined in python eg, print(), len()
# user defined functions are defined by the user
# created using 'def' keyword

# Creating a function without an argument 
def my_function():
    return("Hello from a function")
# Calling a function
print(f"1  : {my_function()}")
# if u are calling function in print() then use return() in function 
# and if used print() in function then call it directly no need to put it in print() function while calling it

# Creating a function with argument
def my_function(fname, lname):
    return(fname + " " + lname)
print(f"2  : {my_function('Karan', 'Singh')}")

# Arbitrary Arguments, *args
def my_function(*kids):
    return("The youngest child is " + kids[2])
print(f"3  : {my_function('Karan', 'Kunal', 'Rohan')}")
# no of argument not decided so can pass as many argument as needed but can be mentioned using * while creating it

# Keyword Arguments
def my_function(child3, child2, child1):
    return("The youngest child is " + child3)
print(f"4  : {my_function(child1 = 'Karan', child2 = 'Kunal', child3 = 'Rohan')}")

# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
    return("His last name is " + kid["lname"])
print(f"5  : {my_function(fname = 'Karan', lname = 'Singh')}")

# Default Parameter Value
def my_function(country = "India"):
    return("I am from " + country)
print(f"6  : {my_function('Sweden')}")
print(f"7  : {my_function('Brazil')}")
print(f"8  : {my_function()}")
# if no argument passed then it will take the default value mentioned

# Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
print("9  :")
my_function(fruits)

# The pass Statement
def myfunction():
    pass
# having an empty function definition like this, would raise an error without the pass statement

# Recursion
# Recursion is a common mathematical and programming concept. It means that a function calls itself.
# This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power.
# However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# Example of recursion
# factorial program is a an example of recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(f"10 : {factorial(5)}")


# Functions 
# two types : built-in and user defined
# built-in functions are already defined in python eg, print(), len()
# user defined functions are defined by the user
# created using 'def' keyword


'''If there are multiple return statements in a function 
then the function will return the first return statement 
and then exit the function'''


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
# The above functions takes required arguments


# 4 types of arguments for functions in python
# 1. Keyword arguments
# 2. Default arguments
# 3. Required arguments
# 4. Arbitrary(variable length) arguments


# Keyword Arguments
def my_function(child3, child2, child1):
    return("The youngest child is " + child3)
print(f"3  : {my_function(child1 = 'Karan', child2 = 'Kunal', child3 = 'Rohan')}")
# with keyword argument, the order of the arguments does not matter


# Default Parameter Value
def my_function(country = "India"):
    return("I am from " + country)
print(f"4  : {my_function('Sweden')}")
print(f"5  : {my_function('Brazil')}")
print(f"6  : {my_function()}")
# if no argument passed then it will take the default value mentioned

def my_function(a=9, b=7):  
    return a+b
print(f"7  : {my_function(5, 3)}")
# overwriting the default value
print(f"8  : {my_function(5)}")
print(f"9  : {my_function(b=5)}")
# if only one value is passed then it will take the default value of second argument
print(f"10 : {my_function()}")
# if no value is passed then it will take the default value of both the arguments


# Required Arguments
# most common type of argument and used in most of the functions
def my_function(fname, lname):
    return(fname + " " + lname)
print(f"11 : {my_function('Karan', 'Singh')}")
# if no value is passed then it will give an error
# required arguments are the arguments passed to a function in correct positional order
# the number of arguments must match exactly the function definition


# Arbitrary Arguments, *args
def my_function(*kids):
    return("The youngest child is " + kids[2])
print(f"12 : {my_function('Karan', 'Kunal', 'Rohan')}")
# no of argument not decided so can pass as many argument as needed but can be mentioned using * while creating it

def my_function(*numbers):
    sum = 0 
    for i in numbers:
        sum = sum + i
    return sum
print(f"13 : {my_function(1, 2, 3, 4, 5)}")
# can pass as many argument as needed and can be mentioned using * while creating it



# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
    return("His last name is " + kid["lname"])
print(f"14 : {my_function(fname = 'Karan', lname = 'Singh')}")
# basically takes the arguments as key value pair and stores them in a dictionary


# Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
print("15 :")
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
print(f"15 : {factorial(5)}")




'''OUTPUT
1  : Hello from a function
2  : Karan Singh
3  : The youngest child is Rohan
4  : I am from Sweden
5  : I am from Brazil
6  : I am from India
7  : 8
8  : 12
9  : 14
10 : 16
11 : Karan Singh
12 : The youngest child is Rohan
13 : 15
14 : His last name is Singh
15 :
apple
banana
cherry
15 : 120
'''

# Global keyword
# The global keyword is used to create global variables from a non-global scope i.e inside a function.


# Example 1 (global variable defined using global keyword and defined within a function)
def func():
    global x
    x = 10
    print(x)

# printing x will give error as there is no global definition of it yet
 
print("1 : ",end="")
func()
# function is called and x is defined as global variable inside the function

print("2 :",x)
# if we hadnt define global x then print(x) would have given error
print()


# Example 2 (global keyword defined without using the global keyword and defined outside any function)
x = 38
def func():
    x = 50
    print(x)
    
print("3 : ",end="")
func()

print("4 :",x)
# here x is a global variable and x is also defined inside the function
# so the x inside the function is a local variable
# the value of x inside the function will be printed since this is not printed using the function
# but the value of x will not be changed since we have not used global keyword
print()


# Example 3 (global keyword defined using the global keyword and defined outside any function)
x = 78
def func():
    global x
    print("6 :",x)
    x = 80
    print("7 :",x)
    
print("5 :",x)
# global variable will be printed since function is not called

func()
# there are two print statement in function
# first print statement will print the value of x globally (78)
# second print statement will print the value of x locally (80) as x is being defined global in this class 
# so x global definition changes to 80 from 78

print("8 :",x)
# 80(class variable) will be printed as when function is called x value in function is defined as global
# so the value of x globally will be changed to 78(class variable) instead of its defined value 80
# so instead of 78, 80 is printed




'''OUTPUT
1 : 10
2 : 10

3 : 50
4 : 38

5 : 78
6 : 78
7 : 80
8 : 80
'''

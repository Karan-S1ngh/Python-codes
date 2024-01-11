# Global keyword
# The global keyword is used to create global variables from a non-global scope i.e inside a function.


# Example 1 (global variable defined using global keyword and defined within a function)
def func():
    global x
    x = 10
    print(x)
    
print("1 : ",end="")
func()

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
    x = 80
    print(x)
    
print("5 :",x)
# global variable will be printed since function is not called

print("6 : ",end="")
func()
# function is called so class variable will be printed
# but x here is defined as global x so x value globally will be changed to class variable 78 instead of its defined value 80

print("7 :",x)
# 80(class variable) will be printed as when function is called x value in function is defined as global
# so the value of x globally will be changed to 78(class variable) instead of its defined value 80
# so instead of 78, 80 is printed




'''OUTPUT
1 : 10
2 : 10

3 : 50
4 : 38

5 : 78
6 : 80
7 : 80
'''

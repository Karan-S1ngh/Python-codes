# Class name is represented in PascalCase (not necessary just prefered)
# Method and attribute name is represented in camelCase (not necessary just prefered)


class TestSum:
    test = 'Hello'
    def Sum(self):
        return self.a + self.b
    
num = TestSum()
num.a = 3
num.b = 4
print(f"1 : Sum of 3 and 4 is '{num.Sum()}'")

print(f"2 : Value of variable test is '{num.test}'")

# to call a variable or method we use object but to change it we use class name

TestSum.test = 'Hi, how are you'
# this will change the class attribute (here, test)
print(f"3 : Value of variable test now is '{num.test}'")

num.test = 'Hola'
# This is an instance attribute
# It will not change the value of class attribute (here, test)
print(f"4 : Value of variable test now after adding instance definition for it is '{num.test}'")

n = TestSum()
# new object created 
print(f"5 : Value of variable test in original class is '{n.test}'")

# We can also delete the attribute of a class
del TestSum.test
print(f"6 : Value of variable test after deleting it from original class is '{num.test}'")
# since the attribute is deleted this will print the instance definiton instead

# We can also delete the instance attribute
del num.test
# since the attribute is deleted this will print the class definiton instead
# but if class definiton and instance definition both are deleted then printing this will give error

# We can also delete the instance
del num
# since the instance is deleted, printing anything related to instance will give error

# We can also delete the class definiton
del TestSum
# since the class is deleted, printing anything related to class will give error

# if u use object to call a attribute then preference for assignment and retrival will be given to instance definition
# if there is no instance definition then class definition will be taken
# if there is no class definition then error will be given

# if u use class name to call a attribute then preference for assignment and retrival will be given to class definition
# if there is no class definition then error will be given

# __init__ method
# it is a constructor
# it is called automatically when an object is created
# it is used to initialize the instance attributes and class attributes



# self paramter
# it refers to instance of class
# used to access the instance attributes and methods but not used to access class attributes and methods
# it is automatically passed with a function call from object

# if u dont use self then it will be a local variable and will not be accessible outside the method
# if u use self then it will be an instance variable and will be accessible outside the method
# if u use class name then it will be a class variable and will be accessible outside the method

class Pass :
    def passing(self):
        pass
# self is necesaary to use 
# if self is not used then there will be a a error if we call the method using object
# if we call the method using class name then there will be a error if we use self 

# n=Example()
# n.example()
# the error while not using self is due to argument
# n.example() is converted to Example.example(n)
# and here there is one argument but if we dont use self then originally there is no argument so conflict occurs
# error = Example.example() takes 0 positional arguments but 1 was given

# Example.example()
# if we call the method like this then if we dont pass self then it is ok as here no argument is passed
# but this will give error if we pass self to method
# error = Example.example() missing 1 required positional argument: 'self'

# inside the class if u call a method which has self as an argument then it will require a argument
# and if u havent pass self then no need for any argument passing inside class

# if u dont use self then it will be a local variable and will not be accessible outside the method
# if u use self then it will be an instance variable and will be accessible outside the method
# if u use class name then it will be a class variable and will be accessible outside the method

# in short if we call a method outside the class using class name then self is not required to be pass
# if we call a method outside the class using object then self is required to be pass


class ExampleOne:
    def first(self):
        print("7 : Hello")
# example of calling a method outside class having self passed as an argument
n1 = ExampleOne()
n1.first()                          # will not give error 
# ExampleOne.first()                # will give error        

class ExampleTwo:
    def second():
        print("8 : Hi")
n2 = ExampleTwo
# n2.second()                       # will give error 
ExampleTwo.second()                 # will not give error
        
class ExampleThree:
    def third(self):
        print("9 : Hola")
    n
    third(n)                        # will not give error
#   third()                         # will give error
        
class ExampleFour:
    def fourth():
        print("10 : Namaste")
    fourth()                        # will not give error
    n
#   fourth(n)                       # will give error




'''OUTPUT
1 : Sum of 3 and 4 is '7'
2 : Value of variable test is 'Hello'
3 : Value of variable test now is 'Hi, how are you'
4 : Value of variable test now after adding instance definition for it is 'Hola'
5 : Value of variable test in original class is 'Hi, how are you'
6 : Value of variable test after deleting it from original class is 'Hola'
7 : Hello
8 : Hi
9 : Hola
10 : Namaste
'''

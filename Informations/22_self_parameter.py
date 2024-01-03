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

# if u create a method in class by passing self then to call and define the attributes in that method use self.attribute_name
# eg, self.name 
# if u create a method in class by not passing self then to call and define the attributes in that method use attribute_name
# eg, name

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
        print(f"1  : Hello, I am '{self.name}'")
# example of calling a method outside class having self passed as an argument
n1 = ExampleOne()
n1.name = 'Karan'
n1.first()                          # will not give error 
# ExampleOne.first()                # will give error        

class ExampleTwo:
    def second():
        print("2  : Hi")
n2 = ExampleTwo
# n2.second()                       # will give error 
ExampleTwo.second()                 # will not give error

n = ''     
class ExampleThree:
    def third(self,greeting):
        print(f"3  : {greeting}")
    n
    third(n,'Hola')                         # will not give error
#   third('Hola')                           # will give error
        
class ExampleFour:
    def fourth():
        print("4  : Namaste")
    fourth()                        # will not give error
    n
#   fourth(n)                       # will give error


# while passing using object to call method object.method is converted to class.method(object)




'''OUTPUT
1  : Hello, I am 'Karan'
2  : Hi
3  : Hola
4 : Namaste
'''

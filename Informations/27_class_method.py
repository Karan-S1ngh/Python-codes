class Example:
    salary = 100
    
    def changeSalary(self, sal):
        self.salary = sal
        
obj = Example()

print("1  :",obj.salary)
# prints 100
obj.changeSalary(500)
# added instance attribute not changing class attribute
print("2  :",obj.salary)
# prints 500
print("3  :",Example.salary)
# prints 100 as instance attribute was changed not class
print()



# In above eg we changes instance attribute not class
# to change class attribute we use class method


# Method 1
# we use __class__ 
# __class__ is a class method which is used to access class attributes
# eg, self.__class__.salary can be used in above eg to access class attribute
class a:
    salary = 200
    
    def changeSalary(self, sal):
        self.__class__.salary = sal
        
obj = a()

print("4  :",obj.salary)
# prints 100
obj.changeSalary(600)
# changes salary to 500 
print("5  :",obj.salary)
# prints 500
print("6  :",a.salary)
# prints 500 as class attribute was changed using __class__
print()


# Method 2 
# we use @classmethod decorator
# @classmethod decorator is used to define class method
# use @classmethod before defining the class to access class attribute
# then instead of self use cls
# eg, cls.salary can be used in above eg to access class attribute

class b:
    salary = 300
    
    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

obj = b()

print("7  :",obj.salary)
# prints 100
obj.changeSalary(800)
# changes salary to 500
print("8  :",obj.salary)
# prints 500
print("9  :",b.salary)
# prints 500 as class attribute was changed using @classmethod decorator
print()


# Method 3
# we use @staticmethod decorator
# Refer to Informations/23_static_method.py


# Method 4
# we use class name
# eg, Example.salary can be used in above eg to access class attribute
class c:
    salary = 400
    
    def changeSalary(self, sal):
        c.salary = sal
        
obj = c()

print("10 :",obj.salary)
# prints 100
obj.changeSalary(900)
# changes salary to 500
print("11 :",obj.salary)
# prints 500
print("12 :",c.salary)
# prints 500 as class attribute was changed using class name



# There are more methods then this to change class defintion instead of instance change
 




'''OUTPUT
1  : 100
2  : 500
3  : 100

4  : 200
5  : 600
6  : 600

7  : 300
8  : 800
9  : 800

10 : 400
11 : 900
12 : 900
'''

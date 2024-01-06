class Base:
    pass
# this is base class

class Derived(Base):
    pass
# this is derived class with base class being mentioned in bracket(here, base)

# we can use methods and attributes of base class in derived class
# we can also overwrite the methods of base class in derived class
# we can also add new methods and attributes in derived class


print("1 :",issubclass(Derived, Base))
# this will print true as Derived is subclass of base 


d = Derived()
b = Base()
# creating objects of both classes

print("2 :",isinstance(d, Base))
# this will print true as d is instance of base class


class Exployee :
    company = "Google"
    def showDetails(self):
        print("This is an employee")
        
class Programmer(Exployee):
    language = 'Python'
    def getLanguage(self):
        print(f"The language is {self.language}")
        
    def showDetails(self):
        print("This is a programmer")
        
e = Exployee()
p = Programmer()
# creating objects of both classes

print("3 :",e.company)

print("4 :",p.company)
# this will print company name as it is inherited from base class

print("5 :",p.language)
# this will print language as it is present in derived class

print("6 : ",end='')
p.getLanguage()
# this will print language as it is present in derived class

print("7 : ",end='')
p.showDetails()
# this will print showDetails() of derived class as it is present in derived class
# this is called method overriding

print("8 : ",end='')
e.showDetails()
# this will print showDetails() of base class as it is present in base class
# here no method overriding

# print(e.getLanguage()) and print(e.language)
# both will give error as they are not present in base class

    

# There are 5 types of inheritance 
# 1. Single inheritance, Multiple inheritance, Multilevel inheritance, Hierarchical inheritance, Hybrid inheritance


# Single inheritance
# When a child class inherits from only one parent class, it is called single inheritance.
class a:
    pass
class b(a):
    pass
# here b is child class and a is parent class
# b will inherit all the methods and attributes of a
# but a will not inherit any methods and attributes of b


# Multiple inheritance
# When a child class inherits from multiple parent classes, it is called multiple inheritance.
# if there are same methods or attributes in both classes and one of them is called 
# then the attribute/method of first class mentioned in bracket will be called
class a:
    company = 'Google'
class b:
    company = 'Microsoft'
class c(b,a):
    pass
three = c()
print("9 :",c.company)
# here c will inherit company from b as it is mentioned first in bracket
# so c.company here will print microsoft as b is mentioned first in c(b,a)


# Multilevel inheritance
# When we have a child and grand child relationship.
class a:
    pass
class b(a):
    pass
class c(b):
    pass
# here c is grand child of a
# c will inherit all the methods and attributes of b and a
# b will inherit all the methods and attributes of a
# a will not inherit any methods and attributes of b and c

# Hierarchial inheritance
# When we have more than one child classes derived from a single parent.
class a:
    pass
class b(a):
    pass
class c(a):
    pass
# here b and c are child classes of a
# b and c will inherit all the methods and attributes of a
# a will not inherit any methods and attributes of b and c

# Hybrid inheritance
# This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.
class a:
    pass
class b(a):
    pass
class c(b):
    pass
class d(a):
    pass
# here b and d are child classes of a
# c is child class of b
# b and c will inherit all the methods and attributes of a
# a will not inherit any methods and attributes of b,c and d
# d will inherit all the methods and attributes of a

  
  
  
'''OUTPUT
1 : True
2 : True
3 : Google
4 : Google
5 : Python
6 : The language is Python
7 : This is a programmer
8 : This is an employee
9 : Microsoft
''' 
 
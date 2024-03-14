# Explain types of inheritance with examples


# Single Inheritance
class Parent:
    def func1(self):
        print("This is function 1")

class Child(Parent):
    def func2(self):
        print("This is function 2")
        
ob = Child()
ob.func1()
ob.func2()
print()


# Multiple Inheritance
class Parent1:
    def func1(self):
        print("This is function 1")

class Parent2:
    def func2(self):
        print("This is function 2")
        
class Child(Parent1, Parent2):
    def func3(self):
        print("This is function 3")
        
ob = Child()
ob.func1()
ob.func2()
ob.func3()
print()

    
# Multilevel Inheritance
class Parent:
    def func1(self):
        print("This is function 1")
        
class Child(Parent):
    def func2(self):
        print("This is function 2")
        
class GrandChild(Child):
    def func3(self):
        print("This is function 3")
        
ob = GrandChild()
ob.func1()
ob.func2()
ob.func3()
print()


# Hierarchical Inheritance
class Parent:
    def func1(self):
        print("This is function 1")

class Child1(Parent):
    def func2(self):
        print("This is function 2")
        
class Child2(Parent):
    def func3(self):
        print("This is function 3")
        
ob1 = Child1()
ob2 = Child2()
ob1.func1()
ob1.func2()
ob2.func1()
ob2.func3()
print()


# Hybrid Inheritance
class Parent1:
    def func1(self):
        print("This is function 1")
        
class Parent2:
    def func2(self):
        print("This is function 2")
        
class Child1(Parent1, Parent2):
    def func3(self):
        print("This is function 3")
        
class Child2(Parent1):
    def func4(self):
        print("This is function 4")
        
ob1 = Child1()
ob2 = Child2()
ob1.func1()
ob1.func2()
ob1.func3()
ob2.func1()
ob2.func4()




'''OUTPUT
This is function 1
This is function 2

This is function 1
This is function 2
This is function 3

This is function 1
This is function 2
This is function 3

This is function 1
This is function 2
This is function 1
This is function 3

This is function 1
This is function 2
This is function 3
This is function 1
This is function 4
'''

# Method overloading and method overriding


# Method overloading is the ability to define multiple methods with the same name in the same class.
# The methods will have different parameters.
# The methods will have different implementations.
# The methods will have different return types.
# The methods will have different number of parameters.

# Example:
class ClassName:
    def method1(self, a, b, c=None, d=None):
        if c is None and d is None:
            print(a + b)
        elif c is not None and d is None:
            print(a + b + c)
        elif c is not None and d is not None:
            print(a + b + c + d)

obj = ClassName()
obj.method1(1, 2)       
obj.method1(1, 2, 3)    
obj.method1(1, 2, 3, 4) 
print()


# Method overriding is the ability to define a method in the child class which is already defined in the parent class.
# The method will have the same name.
# The method will have the same parameters.
# The method will have the same implementation.
# The method will have the same return type.
# The method will have the same number of parameters.

# Example:
class Parent:
    def method1(self):
        print("This is method 1")

class Child(Parent):
    def method1(self):
        print("This is method 1")
        
ob = Child()
ob.method1()
print()




'''OUTPUT
3
6
10

This is method 1
'''

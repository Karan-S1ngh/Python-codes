# What are constructors? types of constructors?


# Constructors are special type of methods which are automatically called when an object of a class is created.
# Constructors are used to initialize the object's state.
# Constructors are of two types:
# 1. Default Constructor
# 2. Parameterized Constructor


# Default Constructor:
# A constructor which has no parameters is called default constructor.
# It is the constructor which is automatically called when an object is created.
# It initializes the object's state with default values.

# Example:
class ClassName:
    def __init__(self):
        self.data = "Hello"
        print("This is default constructor")
        
    def display(self):
        print(self.data)
        
object_name = ClassName()
object_name.display()
print()


# Parameterized Constructor:
# A constructor which has parameters is called parameterized constructor.
# It is used to initialize the object's state with the given values.

# Example:
class ClassName:
    def __init__(self, data):
        self.data = data
        print("This is parameterized constructor")
        
    def display(self):
        print(self.data)
        
object_name = ClassName("Hello")
object_name.display()
print()




'''OUTPUT
This is default constructor
Hello

This is parameterized constructor
Hello
'''

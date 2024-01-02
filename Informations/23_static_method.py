# static method
# it is used to create a method which is not dependent on any attribute of class or instance

# using static method, object.method() is converted to class.method()
# without using static object.method() will be converted to class.method(object)

class StaticExample :
    @staticmethod
    def staticMethod(self) :
        print("This is static method")

StaticExample.staticMethod()
# calling using class

n = StaticExample()
n.staticMethod()
# calling using object

# now passing self is not needed 




'''OUTPUT
This is static method
This is static method
'''

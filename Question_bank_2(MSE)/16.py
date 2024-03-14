# Wap to implement single inheritance using two base classes


class A:
    def __init__(self):
        print("Class A constructor")
    def method1(self):
        print("Method 1 of class A")
        
class B(A):
    def __init__(self):
        A.__init__(self)
        print("Class B constructor")
    def method2(self):
        print("Method 2 of class B")
        
obj = B()
print()

obj.method1()
obj.method2()




'''OUTPUT
Class A constructor
Class B constructor

Method 1 of class A
Method 2 of class B
'''

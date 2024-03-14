# Wap to implement Multiple inheritance using two base classes 


class A:
    def __init__(self):
        print("Class A constructor")
    def method1(self):
        print("Method 1 of class A")
        
class B:
    def __init__(self):
        print("Class B constructor")
    def method2(self):
        print("Method 2 of class B")
        
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("Class C constructor")
    def method3(self):
        print("Method 3 of class C")
        
obj = C()
print()

obj.method1()
obj.method2()
obj.method3()




'''OUTPUT
Class A constructor
Class B constructor
Class C constructor

Method 1 of class A
Method 2 of class B
Method 3 of class C
'''

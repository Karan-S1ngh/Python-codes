# Wap to implement method overriding in python


class A:
    def __init__(self):
        print("Class A constructor")
    def method1(self):
        print("Method 1 of class A")

class B:
    def __init__(self):
        print("Class B constructor")
    def method1(self):
        print(f"Method 1 of class B")

            
obj = B()
obj.method1()




'''OUTPUT
Class B constructor
Method 1 of class B
'''

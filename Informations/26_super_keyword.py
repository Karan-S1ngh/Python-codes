# super() keyword is used to call the methods of parent class


class A:
    def __init__(self):
        print("This is init function from class A")
        
    company = 'Google'
    
    def example(self):
        print("This is example function from class A")
        
class B(A):
    def __init__(self):
        super().__init__()
        print("This is init function from class A")
    
    company = 'Microsoft'
    
    def example(self):
        super().example()
        print("This is example function from class B")



print("1 :")  
obj = B()
# creating objects instantly calls the init function
# it also calls the init function from class A (parent class) using super keyword

print("2 :",obj.company)
# compnay attribute is called from class B  

print("3 :")
obj.example()
# example function is called from class B
# it also calls the example function from class A (parent class) using super keyword




'''OUTPUT
1 :
This is init function from class A
This is init function from class A
2 : Microsoft
3 :
This is example function from class A
This is example function from class B
'''

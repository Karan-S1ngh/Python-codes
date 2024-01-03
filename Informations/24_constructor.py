# __init__ method
# it is a constructor
# it is called automatically when an object is created
# it is used to initialize the instance attributes and class attributes
# it is used to pass arguments to the class

class ConstructorExample :
    def __init__(self, name, age) :
        print("This is constructor")
        self.name = name
        self.age = age
    def getDetails(self):
        print(f"Name : {self.name} \nAge : {self.age}")

print("1 : ", end='')           # using end we can make sure the next thing is printed on same line
n = ConstructorExample('Karan', 19)
# here using this already the __init__ method (constructor) will be printed
# argument directly passed while creating object 
# instead of passing argument by calling method using object after object is created like we do with normal methods

# n.__init__('Karan', 19)
# this will give error

print("2 :")
n.getDetails()

print("3 :",n.name)
print("4 :",n.age)




'''OUTPUT
1 : This is constructor
2 :
Name : Karan
Age : 19
3 : Karan
4 : 19
'''
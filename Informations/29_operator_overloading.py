# operator overloading allows us to change the behavior of an operator depending upon the operands.
# operators can be overloaded using dunder/magic(__name__) methods [Eg, __init__ , __class__ are an example of dunder method]
# These methods are called when a given operator is used on the objects


n1 = int(input("Enter First number : "))
n2 = int(input("Enter Second number : "))

print()

print("User input numbers :",n1,"and",n2)
print("Predefined numbers : 10 and 20")

print()


# operator overloading for addition
class a:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return self.x + other.x
    
obj1 = a(n1)
obj2 = a(n2)
print(f"1 : Addition of user input numbers = {obj1 + obj2}")
obj1 = a(10)
obj2 = a(20)
print(f"2 : Addition of predefined numbers = {obj1 + obj2}")
print()


# operator overloading for multiplication
class b:
    def __init__(self, x):
        self.x = x
    def __mul__(self, other):
        return self.x * other.x
    
obj1 = b(n1)
obj2 = b(n2)
print(f"3 : Multiplication of user input numbers = {obj1 * obj2}")
obj1 = b(10)  
obj2 = b(20)  
print(f"4 : Multiplication of predefined numbers = {obj1 * obj2}")
print()


# operator overloading for greater than
class c:
    def __init__(self, x):
        self.x = x
    def __gt__(self, other):
        if self.x > other.x:
            return True
        else:
            return False

obj1 = c(n1)
obj2 = c(n2)
print(f"5 : Is {n1} greater than {n2} from user input numbers = {obj1 > obj2}")
obj1 = c(10)
obj2 = c(20)
print(f"6 : Is 10 greater than 20 from predefined numbers = {obj1 > obj2}")



# operator overloading can be done similarly for subtraction, division, less than and equal to


# operators in python can be overloaded using following methods
# __add__(self, other) : Addition of two objects
# __sub__(self, other) : Subtraction of two objects
# __mul__(self, other) : Multiplication of two objects
# __truediv__(self, other) : Division of two objects
# __floordiv__(self, other) : Floor division of two objects
# __mod__(self, other) : Modulus of two objects
# __pow__(self, other) : Exponentiation of two objects
# __and__(self, other) : Logical AND of two objects
# __xor__(self, other) : Logical XOR of two objects
# __or__(self, other) : Logical OR of two objects
# __lt__(self, other) : Less than comparison
# __le__(self, other) : Less than or equal to comparison
# __eq__(self, other) : Equal to comparison
# __ne__(self, other) : Not equal to comparison
# __gt__(self, other) : Greater than comparison
# __ge__(self, other) : Greater than or equal to comparison
# __getitem__(self, other) : Index operator
# __setitem__(self, other) : Assign value to index operator
# __len__(self) : Length operator
# __del__(self) : Delete operator
# __str__(self) : String conversion operator
# __repr__(self) : Eval operator




'''OUTPUT
Enter First number : 7
Enter Second number : 4

User input numbers : 7 and 4
Predefined numbers : 10 and 20

1 : Addition of user input numbers = 11
2 : Addition of predefined numbers = 30

3 : Multiplication of user input numbers = 28
4 : Multiplication of predefined numbers = 200

5 : Is 7 greater than 4 from user input numbers = True
6 : Is 10 greater than 20 from predefined numbers = False
'''

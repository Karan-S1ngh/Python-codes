# Write a class calculator capable of finding square, cube and square root of a number


class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"Square of {self.num} is {self.num ** 2}")

    def cube(self):
        print(f"Cube of {self.num} is {self.num ** 3}")

    def sqroot(self):
        print(f"Square root of {self.num} is {self.num ** 0.5}")
        
    @staticmethod
    def greet():
        print("Hello")
    # self not needed as it is static


num = int(input("Enter a number : "))
obj = Calculator(num)
obj.square()
obj.cube()
obj.sqroot()
obj.greet()


# 2 methods
# 1st is printing the sq,cube,sqroot outside the class
# 2nd is printing the sq,cube,sqroot inside the class 



'''OUTPUT
Enter a number : 25
Square of 25 is 625
Cube of 25 is 15625
Square root of 25 is 5.0
Printed

Enter a number : 5
Square of 5 is 25
Cube of 5 is 125
Square root of 5 is 2.23606797749979
Printed
'''

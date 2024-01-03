# Write a class calculator capable of finding square, cube and square root of a number

class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3

    def sqroot(self):
        return self.num ** 0.5

num = int(input("Enter a number : "))
obj = Calculator(num)
print("Square of", num, "is", obj.square())
print("Cube of", num, "is", obj.cube())
print("Square root of", num, "is", obj.sqroot())




'''OUTPUT
Enter a number : 25
Square of 25 is 625
Cube of 25 is 15625
Square root of 25 is 5.0

Enter a number : 5
Square of 5 is 25
Cube of 5 is 125
Square root of 5 is 2.23606797749979
'''

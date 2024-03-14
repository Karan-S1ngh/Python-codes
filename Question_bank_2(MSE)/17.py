# Wap to implement method overloading in python


# Method 1
class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

# Create an instance of MathOperations
math = MathOperations()

# Call the add method with different number of arguments
print(math.add(2, 3))       # Output: 5 (a=2, b=3, c=0)
print(math.add(2, 3, 4))    # Output: 9 (a=2, b=3, c=4)
print()


# Method 2
class MathOperations:
    def add(self, *args):
        return sum(args)

# Create an instance of MathOperations
math = MathOperations()

# Call the add method with different numbers of arguments
print(math.add(2, 3))            # Output: 5
print(math.add(2, 3, 4))         # Output: 9
print(math.add(2, 3, 4, 5, 6))   # Output: 20




'''OUTPUT
5
9

5
9
20
'''

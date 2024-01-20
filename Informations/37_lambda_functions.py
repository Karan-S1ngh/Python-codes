# Lambda functions

# Lambda functions are anonymous functions that can be used to create simple functions that are not needed to be used again in the code.

# They are used to create functions that are only needed once, and are not needed to be used again.
# They are also used to create functions that are passed as arguments to other functions.
# They are also used to create functions that are returned from other functions.
# They are also used to create functions that are stored in data structures such as lists, tuples, dictionaries, etc.   

# Syntax:
# lambda arguments : expression

# Example 1:
# A lambda function that takes one argument and returns its square.
square = lambda x : x ** 2
# This is same as
# def square(x):
#     return x ** 2
a = 5
print("1 :",square(a))

# Example 2:
# A lambda function that takes three arguments and returns their average.
average = lambda x, y, z : (x + y + z) / 3
print("2 :",average(5, 6, 7))

# Example 3:
# A lambda function that takes a list of numbers and returns their average.
average = lambda numbers : sum(numbers) / len(numbers)
print("3 :",average([1, 2, 3, 4, 5]))




'''OUTPUT
1 : 25
2 : 6.0
3 : 3.0
'''

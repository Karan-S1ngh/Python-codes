# Reduce

# It applies a rolling computation to a sequential pair of elements
# It is useful for computing a sum over a sequence data
# The function can be a lamda function also

# Syntax: reduce(function_to_apply, list_of_inputs)
# reduce first has to be imported from functools module

# reduce() works like this:
# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and the number just succeeding the second element
# the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.

# in short it adds the first two numbers
# then adds the result of first two numbers with third number
# and so on till there is no number left to add and prints the result


# Example 1
from functools import reduce
def sum(a, b):
    return a+b

l = [1, 2, 3, 4, 5]

print("1 :",reduce(sum, l))
# using reduce



# Example 2
g = lambda a, b : a*b
l = [1, 2, 3, 4, 5]
print("2 :",reduce(g, l))




'''OUTPUT
1 : 15
2 : 120
'''

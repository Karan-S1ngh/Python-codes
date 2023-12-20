# Dictionary is collection of key-value pairs
# Dictionary is mutable, unordered, indexed(can access element through index) and cannot contain duplicate keys
# Dictionary is represented by curly braces {}
# Dictionary is also known as associative array, hash table, map, etc.

# Creating a dictionary
d = {}
print("1  :",d)         # prints empty list
print("2  :",type(d))   # prints type which is dict

# Creating dictionary with mixed values
d = {1: 'apple', 22: 'ball', 'cde': 'cat', 'd': 4, 'e': {'Test': 345}}
print("3  :",d)                # prints dictionary
print("4  :",d[22])            # prints the value of key whose key is 22
print("5  :",d['d'])           # prints the value of key 'd'
print("6  :",d['e'])           # prints the value of key 'e' (which is a list)
print("7  :",d['e']['Test'])   # prints the value of key 'Test' of key 'e'

# Creating dictionary with dict() constructor
d = dict({1: 'apple', 22: 'ball', 'cde': 'cat', 'd': 4, 'e': {'Test': 345}})
print("8  :",d)                # prints dictionary

# Creating dictionary with dict() constructor and keyword arguments
d = dict(a=1, b=2, c=3)
print("9  :",d)                # prints dictionary

# Creating dictionary with dict() constructor and list of tuples
d = dict([(1, 'apple'), (22, 'ball'), ('cde', 'cat'), ('d', 4), ('e', {'Test': 345})])
print("10 :",d)                # prints dictionary

d = {1: 'apple', 22: 'ball', 'cde': 'cat', 'd': 4, 'e': {'Test': 345}}
print("11 :",d)
d[1] = {1,2,3}          # changes the value of key '1'
print("12 :",d)




'''OUTPUT
1  : {}
2  : <class 'dict'>
3  : {1: 'apple', 22: 'ball', 'cde': 'cat', 'd': 4, 'e': {'Test': 345}}
4  : ball
5  : 4
6  : {'Test': 345}
7  : 345
8  : {1: 'apple', 22: 'ball', 'cde': 'cat', 'd': 4, 'e': {'Test': 345}}
9  : {'a': 1, 'b': 2, 'c': 3}
10 : {1: 'apple', 22: 'ball', 'cde': 'cat', 'd': 4, 'e': {'Test': 345}}
11 : {1: 'apple', 22: 'ball', 'cde': 'cat', 'd': 4, 'e': {'Test': 345}}
12 : {1: {1, 2, 3}, 22: 'ball', 'cde': 'cat', 'd': 4, 'e': {'Test': 345}}
'''

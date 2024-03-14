# Differentiate between List, Tuple & Set with suitable examples of each.

# List:
# List is a collection of items. It is ordered and changeable. It allows duplicate members.
# Example:
fruits = ["apple", "banana", "cherry"]
print("List :",fruits)
print(type(fruits))
print()

# Tuple:
# Tuple is a collection of items. It is ordered and unchangeable. It allows duplicate members.
# Example:
fruits = ("apple", "banana", "cherry")
print("Tuple :",fruits)
print(type(fruits))
print()

# Set:
# Set is a collection of items. It is unordered and unindexed. It does not allow duplicate members.
# Example:
fruits = {"apple", "banana", "cherry"}
print("Set :",fruits)
print(type(fruits))


# The difference between List, Tuple & Set is that 
# List is ordered and changeable, Tuple is ordered and unchangeable and Set is unordered and unindexed. 
# List and Tuple allow duplicate members while Set does not allow duplicate members.




'''OUTPUT
List : ['apple', 'banana', 'cherry']
<class 'list'>

Tuple : ('apple', 'banana', 'cherry')
<class 'tuple'>

Set : {'banana', 'apple', 'cherry'}
<class 'set'>
'''

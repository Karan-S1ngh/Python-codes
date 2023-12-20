# Dictionary methods

d = {1: 'apple', 22: 'ball', 'cde': 'cat', 'd': 4, 'e': {'Test': 345}}

print("1  :",d.keys())         
# Prints all the keys of dictionary
print("2  :",type(d.keys()))
# Prints the type of d.key which is dict_key
print("3  :",list(d.keys()))
# Makes the d.key a list and prints it

print("4  :",d.values())
# Prints all the values of dictionary

print("5  :",d.items())
# Prints all the key-value pairs of dictionary

print("6  :",d.get(22))
# Prints the value of key '22'
# print(d[22]) also does the same thing
# but if the key asked is not present then the .get method will print none but the [] will give error

print("7  :",d.pop(22))
# Removes the key-value pair of key '22' and returns the value removed

print("8  :",d.popitem())
# Removes the last key-value pair of dictionary and returns the value removed

print("9  :",d.clear())
# Removes all the key-value pairs from dictionary

d = {1: 'apple', 22: 'ball', 'cde': 'cat', 'd': 4, 'e': {'Test': 345}}
print("10 :",d)
d.update({'xyz': 'dog', 'qwe': 489, 'ejg': ['Exam' , 987]})
print("11 :",d)
# Updates the dictionary with given new key-value pairs

print("12 :",d.fromkeys([1,'e',3], 'apple'))
# Creates a new dictionary with keys from list and values as 'apple' for all the keys

print("13 :",d.setdefault(22, 'ball'))
# Returns the value of key '22' if present else sets the value as 'ball' for key '22' and returns the value

# For more methods visit python.docs

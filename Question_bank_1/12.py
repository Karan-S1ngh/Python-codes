# Explain any three collection data types of Pythons with suitable examples of each


# There are four collection data types in Python:

# 1. List: A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
# Example:
thislist = ["apple", "banana", "cherry"]
print("1 :",thislist)
print(type(thislist))
print()

# 2. Tuple: A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# Example:
thistuple = ("apple", "banana", "cherry")
print("2 :",thistuple)
print(type(thistuple))
print()

# 3. Set: A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# Example:
thisset = {"apple", "banana", "cherry"}
print("3 :",thisset)
print(type(thisset))
print()

# 4. Dictionary: A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# Example:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("4 :",thisdict)
print(type(thisdict))




'''OUTPUT
1 : ['apple', 'banana', 'cherry']
<class 'list'>

2 : ('apple', 'banana', 'cherry')
<class 'tuple'>

3 : {'banana', 'apple', 'cherry'}
<class 'set'>

4 : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
<class 'dict'>
'''

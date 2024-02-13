# Explain the various data types in python


# There are various data types in Python. Some of the important data types are:
# 1. Numeric: int, float, complex
# 2. Sequence: list, tuple, range
# 3. Text: str
# 4. Set: set, frozenset
# 5. Mapping: dict
# 6. Boolean: bool
# 7. Binary: bytes, bytearray, memoryview

# Example:
# int
x = 5
print("1  :",type(x))
print()

# float
y = 5.0
print("2  :",type(y))
print()

# complex
z = 5+3j
print("3  :",type(z))
print()

# list
thislist = ["apple", "banana", "cherry"]
print("4  :",type(thislist))
print()

# tuple
thistuple = ("apple", "banana", "cherry")
print("5  :",type(thistuple))
print()

# range
thisrange = range(6)
print("6  :",type(thisrange))
print()

# str
a = "Hello, World!"
print("7  :",type(a))
print()

# set
thisset = {"apple", "banana", "cherry"}
print("8  :",type(thisset))
print()

# dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("9  :",type(thisdict))
print()

# bool
b = True
print("10 :",type(b))
print()

# bytes
c = b"Hello"
print("11 :",type(c))
print()

# bytearray
d = bytearray(5)
print("12 :",type(d))
print()

# memoryview
e = memoryview(bytes(5))
print("13 :",type(e))




'''OUTPUT
1  : <class 'int'>

2  : <class 'float'>

3  : <class 'complex'>

4  : <class 'list'>

5  : <class 'tuple'>

6  : <class 'range'>

7  : <class 'str'>

8  : <class 'set'>

9  : <class 'dict'>

10 : <class 'bool'>

11 : <class 'bytes'>

12 : <class 'bytearray'>

13 : <class 'memoryview'>
'''

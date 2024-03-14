# What are the properties of Dictionary Keys?


# The dictionary keys have the following properties:
# 1. The keys of a dictionary are unique.
# 2. The keys of a dictionary are immutable.
# 3. The keys of a dictionary are case sensitive.
# 4. The keys of a dictionary are unordered.
# 5. The keys of a dictionary can be of any data type.
# 6. The keys of a dictionary can be of different data types.

# Example:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  1: "one",
  2.0: "two",
  (3,4): "three four"
}
print(thisdict["brand"])
print(thisdict[1])
print(thisdict[(3, 4)])




'''OUTPUT
Ford
one
three four
'''

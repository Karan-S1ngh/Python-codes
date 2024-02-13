# Explain append () and copy () methods of list with suitable examples of each


# The append() method adds an item to the end of the list.
# Example:
thislist = ["apple", "banana", "cherry"]
print("1 :",thislist)
thislist.append("orange")
print("2 :",thislist)

# The copy() method returns a copy of the specified list.
# Example:
mylist = thislist.copy()
print("3 :",mylist)
thislist.append("mango")
print("4 :",thislist)
print("5 :",mylist)




'''OUTPUT
1 : ['apple', 'banana', 'cherry']
2 : ['apple', 'banana', 'cherry', 'orange']
3 : ['apple', 'banana', 'cherry', 'orange']
4 : ['apple', 'banana', 'cherry', 'orange', 'mango']
5 : ['apple', 'banana', 'cherry', 'orange']
'''

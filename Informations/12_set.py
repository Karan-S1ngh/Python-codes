# Set is a collection of non repetitive elements

# Sets are unordered, unindexed, cannot contain duplicate values, cannot have items in them changed

a = {1, 3, 7, 1}
print(a)            
# prints {1, 3, 7} as it cannot have duplicate values
print("1 :",type(a))      
# prints type as set

a = {}              
# This will create empty dictionary not empty set
print("2 :",type(a))      
# This will print type as dictionary

a = set()           
# This will create empty set
print("3 :",type(a))      
# This eill print type as set


# to convert list to set
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = set(a)
# similarly we can convert tuple to set, tuple to list, list to tuple, set to tuple, set to list




'''OUTPUT
1 : <class 'set'>
2 : <class 'dict'>
3 : <class 'set'>
'''

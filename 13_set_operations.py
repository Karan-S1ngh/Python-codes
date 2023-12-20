# Set operations

s = {1, 2, 6, 4}
s.add(5)
s.add(5)    
# This will add element to the set only once
# U cannot add list,dictionary in a set as they are mutable but u can add tuple as it cannot be modified
s.add((7,8,9))  
# adding a tuple in set
print("1  :",s)
# Prints set in ordered manner without repetition

s = {1, 2, 6, 4}
s.update((7,8,9))
# Adds the mentioned elements to the set
# All the elements will be added separately unlike the add method
print("2  :",s)

s = {1, 2, 6, 4}
s.update([5,9],{7,8})
# Adds the mentioned elements to the set
# All the elements will be added separately (not as tuple like it did in add method)
print("3  :",s)

s = {1, 2, 6, 4}
print("4  :",len(s))
# Prints length of set

s = {1, 2, 6, 4}
s.remove(2)
# Removes the mentioned element from set, if it is not present then it will give error
print("5  :",s)
# Prints the ordered set after removing the mentioned element 

s = {1, 2, 6, 4}
s.discard(2)
# Removes the mentioned element from set, if it is not present then it will not give error
print("6  :",s)
# Prints the ordered set after removing the mentioned element

s = {1, 2, 6, 4}
s.pop()
# Removes a random element from the set
# But the random removed is not changed everytime we run program, it will be the same element regardless of time program has run
print("7  :",s)
# Prints the ordered set after removing a random element 

s = {1, 2, 6, 4}
s.clear()
# Removes all the elements from the set
print("8  :",s)
# Prints empty set

s = {1, 2, 6, 4}
print("9  :",s.union({5,9}))
# Prints the ordered set after removing the mentioned element, i.e, prints the union of mentioned elements and the set

s = {1, 2, 6, 4}
print("10 :",s.intersection({2,6}))
# Prints the common element, i.e, prints the intersection of mentioned elements and the set

s = {1, 2, 6, 4}
print("11 :",s.difference({2,6}))
# Prints the difference of elements, i.e, prints the elements of set which are not present in mentioned elements

s = {1, 2, 6, 4}
print("12 :",s.issubset({2,6}))
# Prints True if set is subset of mentioned elements else prints False

s = {1, 2, 6, 4}
print("13 :",s.issuperset({2,6}))
# Prints True if set is superset of mentioned elements else prints False

s = {1, 2, 6, 4}
print("14 :",s.isdisjoint({2,6}))
# Prints True if set has no common elements with mentioned elements else prints False


# Many other set operations can be performed

# For more methods visit python.docs




'''OUTPUT
1  : {1, 2, 4, 5, 6, (7, 8, 9)}
2  : {1, 2, 4, 6, 7, 8, 9}
3  : {1, 2, 4, 5, 6, 7, 8, 9}
4  : 4
5  : {1, 4, 6}
6  : {1, 4, 6}
7  : {2, 4, 6}
8  : set()
9  : {1, 2, 4, 5, 6, 9}
10 : {2, 6}
11 : {1, 4}
12 : False
13 : True
14 : False
'''

# main difference from list is u can't update tuple but u can update a list
t = ()
print("1  :",t)
# prints empty tuple

t=(1)
print("2  :",t)
# prints 1 as it is not a tuple, it is an integer
# wrong way to print a tuple with a single value

t=(1,)
print("3  :",t)
# prints (1,) as it is a tuple
# right way to print a tuple with a single value

t = (1,2,89,78)
print("4  :",t)
# prints tuple in the order already defined

# t[0] = 34
# print(t)
# del t[0]
# print(t)
# both gives error as tuple is immutable, i.e, u can't change the elements of tuple

# here everything we did with string and list in respect to slicing is applicable
# [:3], [1:], [-4:-1] are all valid
print("5  :",t[0])
# prints 0th element of tuple
print("6  :",t[0:3])
# prints all elements from 0th index to 2nd index
print("7  :",t[0:])
# prints all elements from 0th index to last index
print("8  :",t[:3])
# prints all elements from first index to 2nd index
print("9  :",t[-1])
# prints last element of tuple
print("10 :",t[-4:-1])
# prints all elements from 4th last index to 2nd last index
print("11 :",t[-4:])
# prints all elements from 4th last index to last index
print("12 :",t[:-1])
# prints all elements from first index to last index except last element
# the above are same for string, list, tuples




'''OUTPUT
1  : ()
2  : 1
3  : (1,)
4  : (1, 2, 89, 78)
5  : 1
6  : (1, 2, 89)
7  : (1, 2, 89, 78)
8  : (1, 2, 89)
9  : 78
10 : (1, 2, 89)
11 : (1, 2, 89, 78)
12 : (1, 2, 89)
'''

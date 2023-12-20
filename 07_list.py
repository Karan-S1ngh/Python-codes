a = [1,9,6,7]
print("1  :",a)
# prints all elements in a in the same of order as defined

print("2  :",a[0])
# prints 0th element of a
# if u try to print index which exceeds max index of list, error will occur

a[0] = 98
print("3  :",a)
# changes 0th element of a to 98

# we can create a list with elements of different data types
b = [1,2,'Karan',9.8,True]
print("4  :",b)

# we can print certain parts of list like we did with string
b = [1,2,'Karan',9.8,True]
# here everything we did with string in respect to slicing is applicable
# [:3], [1:], [-4:-1] are all valid
print("5  :",b[0])
# prints 0th element of tuple
print("6  :",b[0:3])
# prints all elements from 0th index to 2nd index
print("7  :",b[0:])
# prints all elements from 0th index to last index
print("8  :",b[:3])
# prints all elements from first index to 2nd index
print("9  :",b[-1])
# prints last element of tuple
print("10 :",b[-4:-1])
# prints all elements from 4th last index to 2nd last index
print("11 :",b[-4:])
# prints all elements from 4th last index to last index
print("12 :",b[:-1])
# prints all elements from first index to last index except last element
# the above are same for string, list, tuples

# we can create a list inside a list
c = [1,2,[3,4,5],6]
print("13 :",c)
print("14 :",c[2])

# we can change elements of list inside a list  
c = [1,2,[3,4,5],6]
c[2][1] = 9
print("15 :",c)



'''OUTPUT
1  : [1, 9, 6, 7]
2  : 1
3  : [98, 9, 6, 7]
4  : [1, 2, 'Karan', 9.8, True]
5  : 1
6  : [1, 2, 'Karan']
7  : [1, 2, 'Karan', 9.8, True]
8  : [1, 2, 'Karan']
9  : True
10 : [2, 'Karan', 9.8]
11 : [2, 'Karan', 9.8, True]
12 : [1, 2, 'Karan', 9.8]
13 : [1, 2, [3, 4, 5], 6]
14 : [3, 4, 5]
15 : [1, 2, [3, 9, 5], 6]
'''
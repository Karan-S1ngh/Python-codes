# list methods

n = [35,6,67,1,45.7]
print("1  :",n)

n.sort()
print("2  :",n)
# sorts the list in ascending order
# can't print n.sort() as n itself is getting changed 
# print(n.sort()) will give 'none' as output
# if list contains elements of different data types then error will occur
# int and float wont give error as both are numbers
# string and int/float will give error as both are different data types

n = [35,6,67,1,45.7]
n.reverse()
print("3  :",n)
# reverses the list

n = [35,6,63,1,45.7]
n.append(49)
print("4  :",n)
# adds element at the end of list

n.insert(2, 67)
print("5  :",n)
# inserts element 67 at index 2
# but no element will be deleted/replaced

n.pop()
print("6  :",n)
# removes last element of list

n.pop(2)
print("7  :",n)
# removes element at index 2

n.remove(63)
print("8  :",n)
# removes element 67 from list
# if the element is not present in list then error will occur

n.clear()
print("9  :",n)
# clears the list

n = [35,6,63,1,45.7]
del n[2]
print("10 :",n)
# deletes element at index 2
# same as pop

n = [35,6,63,1,45.7]
del n
# deletes the entire list
# if u try to print n after deleting it then error will occur, i.e, print(n) will give error in this case
# not same as clear as in clear list is present but all elements are deleted but in this whole list is deleted

n = [35,6,63,1,45.7]    
print("11 :",n.count(6))
# prints how many times 6 is present in list

n = [35,6,63,1,45.7]
print("12 :",n.index(6))
# prints index of 6 in list
# if 6 is not present in list then error will occur

n = [35,6,63,1,45.7]
print("13 :",len(n))
# prints length of list 

print("14 :",sum(n))
# prints sum of all elements of list

print("15 :",max(n))
# prints maximum element of list
print("16 :",min(n))
# prints minimum element of list


a = [1,2,3]
b = [4,5,6]
print("17 :", a == b)
# prints True if both lists are equal
# prints False if both lists are not equal
# if one list is subset of other then also False will be printed


l = [35,6,67,1,45.7]
# to copy we cant use m = l as it will change both the lists
m = l.copy()
# copies the list
# if u change m then l will not change and vice versa
m[0] = 100
print("18 :",l)
print("19 :",m)


l = [35,67,1,45.7]
print("20 :",l)
m = [100,6]
l.extend(m)
# prints the content of m at the end of l
print("21 :",l)
# this changes the list
# if u use k = l + m then it will not change the original list
# rather it will create a new list and store the result in it



# printing methods like append, pop, etc were giving error as they were doing operation
# printing methods like length, index, etc are producing output bcz they are not performing operation 
# they are returning a certain integer value


# For more methods visit python.docs




'''OUTPUT
1  : [35, 6, 67, 1, 45.7]
2  : [1, 6, 35, 45.7, 67]
3  : [45.7, 1, 67, 6, 35]
4  : [35, 6, 63, 1, 45.7, 49]
5  : [35, 6, 67, 63, 1, 45.7, 49]
6  : [35, 6, 67, 63, 1, 45.7]
7  : [35, 6, 63, 1, 45.7]
8  : [35, 6, 1, 45.7]
9  : []
10 : [35, 6, 1, 45.7]
11 : 1
12 : 1
13 : 5
14 : 150.7
15 : 63
16 : 1
17 : False
18 : [35, 6, 67, 1, 45.7]
19 : [100, 6, 67, 1, 45.7]
20 : [35, 67, 1, 45.7]
21 : [35, 67, 1, 45.7, 100, 6]
'''

# enumerate function 
# enumerate function is used to iterate through the container keeping track of the index of the current item.
# Syntax: enumerate(iterable, start=0)
# Parameters:
# Iterable: any object that supports iteration
# Start: the index value from which the counter is to be started, by default it is 0
# Return Type: an enumerate object


# Example 1
l1 = ["eat","sleep","repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("1 : Return type =",type(obj1))
print()

print("2 :",list(enumerate(l1)))
# prints the elements in list each having a index starting from 0
print()

# changing start index to 2 from 0
print("3 :",list(enumerate(s1,2)))
# prints the elements in list each having a index starting from 2
print()


# Example 2
# Python program to illustrate
# enumerate function in loops
l1 = ["eat","sleep","repeat"]

# printing the tuples in object directly
print("4 :")
for e in enumerate(l1):
    print(e)
# prints the elements in separate lines with each having index starting from 0
print()


# changing index and printing separately
print("5 :")
for count,l in enumerate(l1,100):
    print(count,l)
# prints the elements in separate lines with each having index starting from 100




'''OUTPUT
1 : Return type = <class 'enumerate'>

2 : [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

3 : [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

4 :
(0, 'eat')
(1, 'sleep')
(2, 'repeat')

5 :
100 eat
101 sleep
102 repeat
'''   

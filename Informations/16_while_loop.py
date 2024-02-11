# While loop

print("1 :")
i = 0
while i < 5:
    print('Karan',i)
    i += 1

# While loop is used to execute a block of code repeatedly until a given condition is satisfied
# If the condition never becomes false, the loop keeps getting executed


# Use while loop to print content of a list 
print("2 :")
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
# we can also print contents of tuple, set and dictionary like this


# an optional else can also be used with while loop
print("3 :")
i = 0
while i < 5:
    print('i',i)
    i += 1
else:
    print("Loop ended")
# the else block is executed when the condition in the while loop becomes false

# do while loop is not present in python
# but we can achieve the same functionality using while loop




'''OUTPUT
1 :
Karan 0
Karan 1
Karan 2
Karan 3
Karan 4
2 :
apple
banana
cherry
3 :
i 0
i 1
i 2
i 3
i 4
'''

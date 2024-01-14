# List Comprehension

# List Comprehension is a way to create a list using a for loop in one line.
# elegant way to create lists based on exisiting list
# In general we can say it filters out a list in other list in terms of our need



# Example

# Create a list of even numbers from a list containing random numbers
# using list comprehension


# Method 1 (Shortcut)
# list containing random numbers
random_numbers = [1, 2, 3, 4, 5, 6, 60, 69, 70, 77, 89, 90]

# list of even numbers from random_numbers
even_numbers = [x for x in random_numbers if x % 2 == 0]

# print the list
print("1 :",even_numbers)


# Method 2
# list containing random numbers
random_numbers = [1, 2, 3, 4, 5, 6, 60, 69, 70, 77, 89, 90]

# list of even numbers from random_numbers
even_numbers = []
for x in random_numbers:
    if x % 2 == 0:
        even_numbers.append(x)
        
# print the list
print("2 :",even_numbers)



# We can also do set, dictionary, tuple comprehension in similar way
# also we can create a one of them using others
# for example we can create a set using list comprehension
# or we can create a dictionary using set comprehension
# and many more things


# Set Comprehension 
# list containing random numbers
random_numbers = [1, 2, 3, 4, 5, 6, 60, 69, 70, 77, 89, 90]

# set of even numbers from random_numbers
even_numbers = {x for x in random_numbers if x % 2 == 0}

# print the set
print("3 :",even_numbers)


# Dictionary Comprehension
# list containing random numbers
random_numbers = [1, 2, 3, 4, 5, 6, 60, 69, 70, 77, 89, 90]

# dictionary of even numbers from random_numbers with their squares
even_numbers = {x: x**2 for x in random_numbers if x % 2 == 0}

# print the dictionary
print("4 :",even_numbers)


# Tuple Comprehension
# set containing random numbers
random_numbers = {1, 2, 3, 4, 5, 6, 60, 69, 70, 77, 89, 90}

# tuple of even numbers from random_numbers
even_numbers = tuple(x for x in random_numbers if x % 2 == 0)
# since a generator eqn is used, by default it will be generator object
# so we need to convert it into tuple, this is done by using tuple()

# if we use list() then it will be converted into list
# and so on

# print the tuple
print("5 :",even_numbers)



# List Comprehension with if else
# list containing random numbers
random_numbers = [1, 2, 3, 4, 5, 6, 60, 69, 70, 77, 89, 90]

# list of even numbers from random_numbers
# and odd numbers as -1
even_numbers = [x if x % 2 == 0 else -1 for x in random_numbers]
# prints -1 in place of odd numbers

# print the list
print("6 :",even_numbers)


# List Comprehension with nested if else
# list containing random numbers
random_numbers = [1, 2, 3, 4, 5, 6, 60, 69, 70, 77, 89, 90]

# list of even numbers from random_numbers
# and odd numbers as -1
even_numbers = [x if x % 2 == 0 else -1 for x in random_numbers if x % 3 == 0]
# prints -1 in place of odd numbers
# prints -1 in place of numbers not divisible by 3

# print the list
print("7 :",even_numbers)




'''OUTPUT
1 : [2, 4, 6, 60, 70, 90]
2 : [2, 4, 6, 60, 70, 90]
3 : {2, 4, 70, 6, 90, 60}
4 : {2: 4, 4: 16, 6: 36, 60: 3600, 70: 4900, 90: 8100}
5 : (2, 4, 6, 70, 90, 60)
6 : [-1, 2, -1, 4, -1, 6, 60, -1, 70, -1, -1, 90]     
7 : [-1, 6, 60, -1, 90]
'''

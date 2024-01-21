# Map 

# It applies a function to all the items in an input_list
# The function can be a lamda function also

# Syntax: map(function_to_apply, list_of_inputs)


def square(num):
    return num*num

l =[1, 2, 3]

# Method 1
l2 = []
for item in l:
    l2.append(square(item))
print(l2)
# using for loop

# Method 2
print(list(map(square, l)))
# using map and typecasting it into list




'''OUTPUT
[1, 4, 9]
[1, 4, 9]
'''    

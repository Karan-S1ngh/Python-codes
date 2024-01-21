# Filter

# It creates a list of items for which function returns true
# The function can be a lamda function also

# Syntax: filter(function_to_apply, list_of_inputs)


def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False
    
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Method 1
l2 = []
for item in l:
    if greater_than_5(item):
        l2.append(item)
print(l2)
# using for loop

# Method 2
print(list(filter(greater_than_5, l)))
# using filter and typecasting it into list




'''OUTPUT
[6, 7, 8, 9]
[6, 7, 8, 9]
'''

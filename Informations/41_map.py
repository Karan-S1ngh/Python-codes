# Map 

# It applies a function to all the items in an input_list
# The function can be a lamda function also

# Syntax: map(function_to_apply, list_of_inputs)


# Example 1
def square(num):
    return num*num

l =[1, 2, 3]

# Method 1
l2 = []
for item in l:
    l2.append(square(item))
print("1 :",l2)
# using for loop

# Method 2
print("2 :",list(map(square, l)))
# using map and typecasting it into list



# Example 2
g = lambda num : num*num*num
l = [1, 2, 3]
print("3 :",list(map(g, l)))




'''OUTPUT
1 : [1, 4, 9]
2 : [1, 4, 9]
3 : [1, 8, 27]
'''    

# User-defined program to display and find sum of lists of numbers using while loop
 
# Function to input elements into a list
def input_list():
    lst = []
    n = int(input("Enter number of elements: "))
    i = 0
    while i < n:
        lst.append(int(input(f"Enter element at index {i}: ")))
        i += 1
    return lst

# Function to display list elements and their sum
def display_and_sum_list(lst):
    print("List is:", lst)
    print("Sum of the list is:", sum(lst))

# Input and display list 1
print("List 1:")
list1 = input_list()
display_and_sum_list(list1)
print()

# Input and display list 2
print("List 2:")
list2 = input_list()
display_and_sum_list(list2)
print()

# Calculate the sum of the two lists
combined_list = list1 + list2
print("Combined list is:", combined_list)
print("Sum of the combined list is:", sum(combined_list))




'''OUTPUT
List 1:
Enter number of elements: 2
Enter element at index 0: 1
Enter element at index 1: 2
List is: [1, 2]
Sum of the list is: 3

List 2:
Enter number of elements: 3
Enter element at index 0: 2
Enter element at index 1: 3
Enter element at index 2: 4
List is: [2, 3, 4]
Sum of the list is: 9

Combined list is: [1, 2, 2, 3, 4]
Sum of the combined list is: 12
'''

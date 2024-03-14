# User-defined program to display and find sum of lists of numbers using for loop


list1 = []
n = int(input("Enter number of elements for list 1: "))
for i in range(n):
    list1.append(int(input(f"Enter element at index {i} for list 1: ")))

print("List 1 is:", list1)
print("Sum of list 1 is:", sum(list1))
print()

list2 = []
n = int(input("Enter number of elements for list 2: "))
for i in range(n):
    list2.append(int(input(f"Enter element at index {i} for list 2: ")))

print("List 2 is:", list2)
print("Sum of list 2 is:", sum(list2))
print()

# Calculate the sum of the two lists
combined_list = list1 + list2
print("Combined list is:", combined_list)
print("Sum of the combined list is:", sum(combined_list))




'''OUTPUT
Enter number of elements for list 1: 2
Enter element at index 0 for list 1: 1
Enter element at index 1 for list 1: 2
List 1 is: [1, 2]
Sum of list 1 is: 3

Enter number of elements for list 2: 3
Enter element at index 0 for list 2: 2
Enter element at index 1 for list 2: 3
Enter element at index 2 for list 2: 4
List 2 is: [2, 3, 4]
Sum of list 2 is: 9

Combined list is: [1, 2, 2, 3, 4]
Sum of the combined list is: 12
'''

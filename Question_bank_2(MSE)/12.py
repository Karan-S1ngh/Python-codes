# Wap to linear search an element in the lists of elements
 
# Function to input elements into a list
def input_list():
    lst = []
    n = int(input("Enter number of elements: "))
    i = 0
    while i < n:
        lst.append(int(input(f"Enter element at index {i}: ")))
        i += 1
    return lst

# Function to search for an element in a list
def search_list(lst, element):
    if element in lst:
        print(f"{element} is present in the list at index {lst.index(element)}")
    else:
        print(f"{element} is not present in the list")
        

list1 = input_list()
element = int(input("Enter element to search in list 1: "))
search_list(list1, element)
print("List is:", list1)




'''OUTPUT
Enter number of elements: 2
Enter element at index 0: 1
Enter element at index 1: 3
Enter element to search in list 1: 3
3 is present in the list at index 1
List is: [1, 3]

Enter number of elements: 3
Enter element at index 0: 1
Enter element at index 1: 2
Enter element at index 2: 3
Enter element to search in list 1: 4
4 is not present in the list
List is: [1, 2, 3]
'''

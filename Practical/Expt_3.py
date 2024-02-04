def List():
  list = []
  n = int(input("Enter number of elements : "))
  for i in range(n):
      list.append(int(input(f"Enter {i} index element : ")))
  print("List :",list)
  
  print("1. Sort List")
  print("2. Reverse List")
  print("3. Insert an element in list at a specific position")
  print("4. Remove an element from a specific position from list")
  print("5. Count and Index of Element in List")
  print("6. Sum of elements in list")
  print("7. Maximum and Minimum element in list")
  print("8. Search an element in list")

  choice = int(input("Enter your choice : "))

  if choice == 1:
    print("Sorted List: ", sorted(list))
  elif choice == 2:
    print("Reversed List: ", list.reverse())
  elif choice == 3:
    a = int("Enter the element to be inserted: ")
    b = int(input("Enter the position to insert: "))
    list.insert(b, a)
    print("List after insertion: ", list)
  elif choice == 4:
    a = int(input("Enter the element to be removed: "))
    if a in list:
      list.remove(a)
    else:
      print("Element not found in list")
    print("List after removal: ", list)
  elif choice == 5:
    a = int(input("Enter the element to be counted: "))
    if a in list:
      print("Count of element in list: ", list.count(a))
      print("Index of element in list: ", list.index(a))
    else:
      print("Element not found in list")
  elif choice == 6:
    print("Sum of elements in list: ", sum(list))
  elif choice == 7:
    print("Maximum element in list: ", max(list))
    print("Minimum element in list: ", min(list))
  elif choice == 8:
    a = int(input("Enter the element to be searched: "))
    if a in list:
      print("Element found in list")
    else:
      print("Element not found in list")
  else:
    print("Invalid choice")


def Tuple():
  tuple1 = []
  n = int(input("Enter number of elements : "))
  for i in range(n):
      tuple1.append(int(input(f"Enter {i} index element : ")))
  tuple1 = tuple(tuple1)
  print("Tupple :",tuple1)
  
  print("1. Count of an Element in Tuple")
  print("2. Maximum and Minimum element in Tuple")
  print("3. Sum of elements in Tuple")
  print("4. Index of an Element in Tuple")
  print("5. Sorted Tuple")
  print("6. Search an element in tuple")

  choice = int(input("Enter your choice : "))

  if choice == 1:
    a = int(input("Enter the element to be counted: "))
    if a in tuple1:
      print("Count of element in tuple: ", tuple1.count(a))
    else:
      print("Element not found in tuple")
  elif choice == 2:
    print("Maximum element in tuple: ", max(tuple1))
    print("Minimum element in tuple: ", min(tuple1))
  elif choice == 3:
    print("Sum of elements in tuple: ", sum(tuple1))
  elif choice == 4:
    a = int(input("Enter the element to be counted: "))
    if a in tuple1:
      print("Index of element in list: ", tuple1.index(a))
    else:
      print("Element not found in list")
  elif choice == 5:
    print("Sorted Tuple: ", sorted(tuple1))
  elif choice == 6:
    a = int(input("Enter the element to be searched: "))
    if a in tuple1:
      print("Element found in tuple")
    else:
      print("Element not found in tuple")
  else:
    print("Invalid choice")


def Dictionary():
  dict = {}
  n = int(input("Enter number of elements : "))
  for i in range(n):
      key = input(f"Enter {i} index key : ")
      value = input(f"Enter {i} index value : ")
      dict[key] = value
  print("Dictionary :",dict)
  
  print("1. All keys in Dictionary")
  print("2. Value of a key in Dictionary")
  print("3. Add a new key-value pair in Dictionary")
  print("4. Remove a key-value pair in Dictionary")
  print("5. Update a value in Dictionary")
  print("6. Search a key in Dictionary")

  choice = int(input("Enter your choice : "))

  if choice == 1:
    print("All keys in Dictionary: ", dict.keys())
  elif choice == 2:
    a = input("Enter the key to get value: ")
    if a in dict:
      print("Value of key in Dictionary: ", dict[a])
    else:
      print("Key not found in Dictionary")
  elif choice == 3:
    key = input("Enter the key to be added: ")
    value = input("Enter the value to be added: ")
    dict[key] = value
    print("Dictionary after addition: ", dict)
  elif choice == 4:
    key = input("Enter the key to be removed: ")
    if key in dict:
      del dict[key]
    else:
      print("Key not found in Dictionary")
    print("Dictionary after removal: ", dict)
  elif choice == 5:
    key = input("Enter the key to be updated: ")
    value = input("Enter the new value: ")
    if key in dict:
      dict[key] = value
    else:
      print("Key not found in Dictionary")
    print("Dictionary after update: ", dict)
  elif choice == 6:
    key = input("Enter the key to be searched: ")
    if key in dict:
      print("Key found in Dictionary")
    else:
      print("Key not found in Dictionary")
  else:
    print("Invalid choice")



print("1. List")
print("2. Tuple")
print("3. Dictionary")

choice = int(input("Choose on which u want to operate: "))
  
if choice == 1:
  List()
elif choice == 2:
  Tuple()
elif choice == 3:
  Dictionary()
else:
  print("Invalid choice")
  



'''OUTPUT'''
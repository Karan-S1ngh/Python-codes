# String Functions

name = 'Karan is chilling'
print("1 :",len(name))               
# prints total length of string

print("2 :",name.endswith('an'))
# if given characters are present at the end of string then it prints true otherwise false

print("3 :",name.count('a'))
# gives how many time the given character has appeared in the string


new = 'hello how are u'

print("4 :",new.capitalize())
# this makes the first character of the string capital

print("5 :",new.find('ll'))
# this finds the given character in the string and gives the index of first occurence
# if the character is not present then it gives -1

print("6 :",new.replace('ll','m'))
# this replaces the first character with the second character in the string
# if the character is not present then it returns the exact same string back


# u can even replace something in a string with a user input
new = 'hello "insert_name", how are u'
trying = input("Enter name : ")
new = new.replace('insert_name',trying)
print("7 :",new)




'''OUTPUT
1 : 17
2 : False
3 : 2
4 : Hello how are u
5 : 2
6 : hemo how are u
Enter name : Karan
7 : hello "Karan", how are u
'''

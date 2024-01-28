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

n = '    Hello,   I am    Karan    '
print("8 :",n)
print("9 :",n.strip())
# strip removes the extra spaces from both side 
# rstrip removes the extra spaces from right side
# lstrip removes the extra spaces from left side

n = 'Karan'
s = slice(3)
print("10 :",n[s])
# slice is used to slice a string
# it takes 3 arguments
# 1st is starting index
# 2nd is ending index
# 3rd is step size
# if u give only one argument then it will take it as ending index
# if u give two arguments then it will take it as starting and ending index
# if u give three arguments then it will take it as starting, ending and step size




'''OUTPUT
1 : 17
2 : False
3 : 2
4 : Hello how are u
5 : 2
6 : hemo how are u
Enter name : Karan
7 : hello "Karan", how are u
8 :     Hello,   I am    Karan
9 : Hello,   I am    Karan
10 : Kar
'''

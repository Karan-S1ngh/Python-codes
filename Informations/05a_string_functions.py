# String Functions/Methods

name = 'Karan is chilling'
print("1  :",len(name))               
# prints total length of string

print("2  :",name.endswith('an'))
# if given characters are present at the end of string then it prints true otherwise false

print("3  :",name.endswith('is',2,8)) 
# if given characters are present at the end of mentioned index of the string then it prints true otherwise false

print("4  :",name.count('a'))
# gives how many time the given character has appeared in the string


new = 'hello How are u'

print("5  :",new.capitalize())
# this makes the first character of the string capital
# also makes all other capital characters small

print("6  :",new.find('ll'))
# this finds the given character in the string and gives the index of first occurence
# if the character is not present then it gives -1

print("7  :",new.replace('ll','m'))
# this replaces the first character with the second character in the string
# if the character is not present then it returns the exact same string back


# u can even replace something in a string with a user input
new = 'hello "insert_name", how are u'
trying = input("Enter name : ")
new = new.replace('insert_name',trying)
print("8  :",new)

n = '    Hello,   I am    Karan    '
print("9  :",n)
print("10 :",n.strip())
# strip removes the extra spaces from both side 
# rstrip removes the extra spaces from right side
# lstrip removes the extra spaces from left side

n = 'Karan'
s = slice(3)
print("11 :",n[s])
# slice is used to slice a string
# it takes 3 arguments
# 1st is starting index
# 2nd is ending index
# 3rd is step size
# if u give only one argument then it will take it as ending index
# if u give two arguments then it will take it as starting and ending index
# if u give three arguments then it will take it as starting, ending and step size

n = 'hello'
print("12 :",n.upper())
# this makes all the characters of the string capital

n = 'HELLO'
print("13 :",n.lower())
# this makes all the characters of the string small

n = 'hello'
print("14 :",n.islower())
# this checks whether all the characters of the string are small or not

n = 'HELLO'
print("15 :",n.isupper())
# this checks whether all the characters of the string are capital or not

n = 'Hello'
print("16 :",n.isalpha())
# this checks whether all the characters of the string are alphabets or not

n = '123'
print("17 :",n.isdigit())
# this checks whether all the characters of the string are digits or not

n = 'Hello'
print("18 :",n.split('l'))
# this splits the string with the given character

n = 'Hello'
print("19 :",n.rsplit('l'))
# this splits the string with the given character from the right side
# same for left 




'''OUTPUT
1  : 17
2  : False
3  : True
4  : 2
5  : Hello how are u
6  : 2
7  : hemo How are u
Enter name : Karan 
8  : hello "Karan", how are u
9  :     Hello,   I am    Karan
10 : Hello,   I am    Karan
11 : Kar
12 : HELLO
13 : hello
14 : True
15 : True
16 : True
17 : True
18 : ['He', '', 'o']
19 : ['He', '', 'o']
'''

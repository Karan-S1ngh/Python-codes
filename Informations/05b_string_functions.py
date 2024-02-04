n = 'Hello'
print("1  :",n.swapcase())
# this swaps the case of the characters of the string
# capital becomes small and small becomes capital

n = 'Hello'
print("2  :",n.title())
# this makes the first character of each word capital

n = 'Hello'
print("3  :",n.center(20))
# this centers the string in the given length
# if the length is not given then it takes the length of the string

n = 'Hello'
print("4  :",n.zfill(10))
# this fills the string with zeros from the left side
# the length of the string is given as argument

n = 'Hello'
print("5  :",n.startswith('H'))
# this checks whether the string starts with the given character or not

n = 'Hello'
print("6  :",n.endswith('o'))
# this checks whether the string ends with the given character or not

n = 'Hello'
print("7  :",n.isalnum())
# this checks whether the string is alphanumeric or not
# alphanumeric means it contains alphabets and digits

n = 'Hello'
print("8  :",n.isdecimal())
# this checks whether the string is decimal or not
# decimal means it contains only digits

n = 'Hello'
print("9  :",n.isidentifier())
# this checks whether the string is identifier or not
# identifier means it contains alphabets, digits and underscore

n = 'Hello'
print("10 :",n.isprintable())
# this checks whether the string is printable or not
# printable means it contains only printable characters

n = 'Hello'
print("11 :",n.isspace())
# this checks whether the string is space or not
# space means it contains only spaces

n = 'Hello'
print("12 :",n.istitle())
# this checks whether the string is title or not
# title means it contains only title characters

n = 'Hello'
print("13 :",n.join('123'))
# this joins the string with the given character

n = 'Hello'
print("14 :",n.partition('l'))
# this partitions the string with the given character

n = 'Hello'
print("15 :",n.rpartition('l'))
# this partitions the string with the given character from the right side

n = 'Hello'
print("16 :",n.splitlines())
# this splits the string with the new line character

n = 'Hello'
print("17 :",n.ljust(10))
# this left justifies the string in the given length
# same for rjust and center




'''OUTPUT
1  : hELLO
2  : Hello
3  :        Hello
4  : 00000Hello
5  : True
6  : True
7  : True
8  : False
9  : True
10 : True
11 : False
12 : True
13 : 1Hello2Hello3
14 : ('He', 'l', 'lo')
15 : ('Hel', 'l', 'o')
16 : ['Hello']
17 : Hello
'''

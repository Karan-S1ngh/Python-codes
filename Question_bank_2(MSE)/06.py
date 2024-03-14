# What is String and solve any 5 method


# String is a sequence of characters. It is a data type in python. It is immutable. 
# It is a collection of characters inside single quotes or double quotes. It is a sequence of Unicode characters.

# Example:
string = "Hello World"
print("1:", string)  
print("2:", string[0])  
print("3:", string[1:5]) 
print("4:", string[-5:-2]) 
print()

print("5:", string.upper())  
print("6:", string.lower())  
print("7:", string.strip())  
print("8:", string.replace("H", "J"))  
print("9:", string.split(" "))  
print("10:", len(string))  
print("11:", string.count("l"))  
print("12:", string.find("o"))  




'''OUTPUT
1: Hello World
2: H
3: ello
4: Wor

5: HELLO WORLD
6: hello world
7: Hello World
8: Jello World
9: ['Hello', 'World']
10: 11
11: 3
12: 4
'''

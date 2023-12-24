# Foor loop

# For loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# Iterating over a sequence is called traversal.

# Use for loop to print content of a list
fruits = ["apple", "banana", "cherry"]
print("'1' :")
for item in fruits:
    print(item)
# We can also print contents of tuple, set and dictionary like this

# Use for loop to print content of a string
print("'2' :")
for char in "Har":
    print(char)
    
# Use for loop to print content of a range
print("'3' :")
for i in range(3):
    print(i)
# here only one number in range function so 3 numbers from 0 will be printed (3 being excluded)
    
print("'4' :")
for i in range(1, 3):
    print(i)
# here two numbers in range function so numbers from 1 till 3 will be printed (3 being excluded)


# range(start, stop, step-size)
# the first number in range is the starting number to be printed 
# and it will be printed till the second number in range function (second number excluded)
# the third number in range is the incrementation of the number to be printed 

# if first number numbert given, i.e, only one number in range function so numbers will be printed from 0 
# and total number will be equal to the number in range funtion
# if the third number is not given then the default value is 1

# Example
# In c and java 
# for(i=0;i<5;i++){
#     printf("Karan");
# }
# In python 
# for i in range(0,5,1)
#   printf("Karan");


# an optional else can also be used with for loop
print("'5' :")
for i in range(1, 10, 2):
    print(i)
else:
    print("Loop ended")
# else will be executed after for loop is over successfully




'''OUTPUT
'1' :
apple
banana
cherry
'2' :
H
a
r
'3' :
0
1
2
'4' :
1
2
'5' :
1
3
5
7
9
Loop ended
'''

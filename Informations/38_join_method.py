# join method

# join method is used to join the elements of a list or any iteratable object(like tuple and set), with the help of a string
# join method is a string method, and can only be used with strings
# join method takes an iterable as an argument and returns a string


l = ['Karan', 'Ramesh', 'Mahesh', 'Suresh', 'Ram']

# Our aim is to create a string, from above list, joining all of its content, separated by 'and

sentence = ' and ' . join(l)
print("1 :",sentence)
# if u want to separate by any other word then use that word in place of 'and' in above program

sentence = ' or '.join(l)
print("2 :",sentence)


l = {'Mango', 'Grapes', 'Apple', 'Banana'}

example = '\n'.join(l)
print("3 :")
print(example)


print("4 :",type(example))




'''OUTPUT
1 : Karan and Ramesh and Mahesh and Suresh and Ram
2 : Karan or Ramesh or Mahesh or Suresh or Ram
3 :
Apple
Grapes
Mango
Banana
4 : <class 'str'>
'''

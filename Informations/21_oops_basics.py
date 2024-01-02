# Class name is represented in PascalCase (not necessary just prefered)
# Method and attribute name is represented in camelCase (not necessary just prefered)


class TestSum:
    test = 'Hello'
    def Sum(self):
        return self.a + self.b
    
num = TestSum()
num.a = 3
num.b = 4
print(f"1 : Sum of 3 and 4 is '{num.Sum()}'")

print(f"2 : Value of variable test is '{num.test}'")

# to call a variable or method we use object but to change it we use class name

TestSum.test = 'Hi, how are you'
# this will change the class attribute (here, test)
print(f"3 : Value of variable test now is '{num.test}'")

num.test = 'Hola'
# This is an instance attribute
# It will not change the value of class attribute (here, test)
print(f"4 : Value of variable test now after adding instance definition for it is '{num.test}'")

n = TestSum()
# new object created 
print(f"5 : Value of variable test in original class is '{n.test}'")

# We can also delete the attribute of a class
del TestSum.test
print(f"6 : Value of variable test after deleting it from original class is '{num.test}'")
# since the attribute is deleted this will print the instance definiton instead

# We can also delete the instance attribute
del num.test
# since the attribute is deleted this will print the class definiton instead
# but if class definiton and instance definition both are deleted then printing this will give error

# We can also delete the instance
del num
# since the instance is deleted, printing anything related to instance will give error

# We can also delete the class definiton
del TestSum
# since the class is deleted, printing anything related to class will give error

# if u use object to call a attribute then preference for assignment and retrival will be given to instance definition
# if there is no instance definition then class definition will be taken
# if there is no class definition then error will be given

# if u use class name to call a attribute then preference for assignment and retrival will be given to class definition
# if there is no class definition then error will be given


# while passing self, using object to call method, object.method is converted to class.method(object)
# using static method, object.method() is converted to class.method()




'''OUTPUT
1 : Sum of 3 and 4 is '7'
2 : Value of variable test is 'Hello'
3 : Value of variable test now is 'Hi, how are you'
4 : Value of variable test now after adding instance definition for it is 'Hola'
5 : Value of variable test in original class is 'Hi, how are you'
6 : Value of variable test after deleting it from original class is 'Hola'
'''

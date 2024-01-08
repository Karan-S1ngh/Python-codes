# Exception handling makes sure that a program is not crashed in case of a error and it continues working


# try block
# in this the code which is to be checked for error is written
# if there is no error then the code will run smoothly till there is no error
# if there is an error then the code will stop where error occured and the except block will run

# except block
# in this the code which is to be run if there is an error is written
# if there is no error then the code here will not run

# TRY AND EXCEPT BLOCKS 
a= 10
print("1 :")
try:
    print(a/0)
except Exception as e:
    print("Error occured")
print()
# here 10/0 will give error as its not possible so code in except block will be executed
# here custom message is printed that is error occured

# in except we can also print(e) this will give the exact error that is happening 
# and also what error python will give if we try to run it without exception handling will be given by print(e)
# if we just write 'except' then also ok

# TRY WITH ELSE
# we can also use else block in try except
# else block will be executed if there is no error and if there is error then except block will be executed
a= 10
print("2 :")
try:
    print(a/2)
except Exception as e:
    print("Error occured")
else:
    print("No error occured")
print()


# MULTIPLE EXCEPT BLOCK
# we can use multiple except types block
# but we cant use only 'except' multiple types
# if we want to use except multiple time then we have to define it differently every time
# eg, except Zerodivision, except Exceptiona as e, except, etc
# but only one except block will be executed 
print("3 :")
try:
    c ='ABC'
    a = int(c)
    print(1/a)
except ZeroDivisionError as e:
    print("ZeroDivisionError occured")
    # occurs when number is divided by 0
except ValueError as e:
    print("ValueError occured")
    # occurs when a string is given as an input where a number was expected
except:
    print("Some error occured")
    # for errors other than the above ones
print()


# RAISE KEYWORD
# we can raise custom exception using "raise" keyword
# example, put [raise ValueError("This is a custom exception")] in except block


# TRY WITH FINALLY BLOCK
# finally block will be executed no matter what
# if there is error or no error finally block will be executed
# finally block is used for closing files or closing database connections
print("4 :")
try:
    a = int('ABC')
    print(1/a)
except Exception as e:
    print("Error occured")
finally:
    print("Finally block executed")




'''OUTPUT
1 :
Error occured

2 :
5.0
No error occured

3 :
ValueError occured

4 :
Error occured
Finally block executed
'''

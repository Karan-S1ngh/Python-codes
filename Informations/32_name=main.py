# if __name__ = 'main' in python
# __name__ evaluated to name of module in python from where program is run

# if the module is being run directly from the command line, the __name__ is set to string '__main__'
# Thus this behaviour is used to check wheteher the module is run directly or imported to another file

# the code in this will not run if the file is being imported to another file and then run
# but if the file is run directly from the command line, the code will run

# this is used to prevent code from being run on import
# certain code is not needed to imported to another file, so this is useful in achieving that

# this is useful when you want to run certain code only when the file is run directly from the command line
# and not when the file is imported to another file


# For eg, we create a file named file1.py which contains the following
def greet(name):
    print(f'Hello {name}')
print(__name__) 
# This will give "main" as an output   
if __name__ == '__main__':
    name = input('Enter your name: ')
    greet(name)


# Now we create a file named file2.py which contains the following
## import file1
## file1.greet("Karan")
# Hello Karan will be printed here 
# here name will not be asked
# so running file2 wont ask name but running file1 will ask name
## print(__name__) 
# This will give "file1" as an output
# this is because the file is imported to another file, so __name__ is set to the name of the file



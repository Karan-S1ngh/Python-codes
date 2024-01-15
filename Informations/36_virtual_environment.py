# Virtual Environment

# It is same as system interpreter but is isloated from other python environments

# It is a tool that helps to keep dependencies required by different projects separate. 
# This is done by creating isolated python virtual environments for them. 
# This is one of the most important tools that most of the Python developers use.

# This creates separate environments for all projects running on different versions
# as there might be some issues in using the different version other than the used ones in the projects


# For eg, we can create a virtual env on which flask module is of version 0.5.2, 
# while also running another version of flask, for eg: 1.0.2, on another virtual env or on main one 
# without any conflicts between the two.
# This is done because there might be issue in project made with 0.5.2 version if a new version is installed there


# Virtual environment can be viewed in source folder as it will be present as a folder in it
# Also it will take up a lot of memeory 



# To install virtualenv, open command prompt and write:
""" pip install virtualenv """ 

# To create a virtual environment, open command prompt and write:
''' virtualenv <name of env> ''' 

# To activate the virtual environment, open command prompt and write:
''' <name of env>/bin/activate '''                  # for linux/MacOS
''' <name of env>\Scripts\activate '''              # for windows
# in windows that might give error of running script is diabled
# to enable that, open window powershell as administrator and write:
''' Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process '''
# and type 'y' and enter
# now the error wont exist and we can access the virtual env without any issues

# To deactivate the virtual environment, open command prompt and write:
''' deactivate '''

# To delete the virtual environment, open command prompt and write:
''' rmdir <name of env> /s '''
# /s is used to delete the folder even if it is not empty
# using /s we wont be asked to confirm for deletion
# if /s is not mentioned then we will be asked to type y if we want to really delete the virtual environment

# To create a virtual environment with a specific version of python, open command prompt and write:
''' virtualenv -p <path to python> <name of env> '''
# for eg: virtualenv -p C:\Python\Python37\python.exe myenv
# this will create a virtual environment with python 3.7 version
# if path is not given then it will create a virtual environment with the same version as the main environment


# pip commands
# All below pip commands can also be used in the main environment

# To install a module in virtual environment, open command prompt and write:
''' pip install <module name> '''

# To install a specific version of module in virtual environment, open command prompt and write:
''' pip install <module name>==<version> '''

# To view the modules along with the versions, open command prompt and write:
''' pip freeze '''
# This command is used to view all the modules with their versions present in the given environment

# It is used to create a requirements.txt file which contains all the modules and their versions
# To create requirements.txt file, open command prompt and write:
''' pip freeze > requirements.txt '''

# To install all the modules with the same version as in requirements.txt, open command prompt and write:
''' pip install -r requirements.txt '''
# This can be used to install the modules with the specific versions in different environment

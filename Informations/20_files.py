# File I/O
# It includes operations done on other files other than the current one 

# r is used to read the file
# w is used to write the file
# a is used to append the file
# x is used to create the file
# t is used to text file
# + is used to read and write the file

# b is used to binary file
# rb for read in binary mode
# wb for write in binary mode
# ab for append in binary mode
# xb for create in binary mode
# same for others too 



# READ FUNCTION

f = open('Files/read_function_sample.txt','r')
# used to open files in python in readmode (r)
# if the file is not present then it will be created
# by default the mode is r so if not mentioned then the file is in readable mode only

f.read(5)
# if we give any argument then it will read that many characters of the file 
# for eg here f.read(45) will read only first 45 characters of the file mentioned
f.readline()
# will read only one line of the file
# if we use it after f.read(5) which reads 5 character then it will read the remaining characters of the line
# /n will also be read as a line so an extra line will be printed between two f.readlines
f.readline()
# if we use this n times then we can read n lines of file

f.read()
# This will read the whole file
# if we use this after f.read(5) then it will read the remaining characters of the file

f.readlines()
# This will read all the lines of the file and will store them in a list
# so we can use for loop to print all the lines of the file
# each line is stored as a string in the list
# each line is separated by \n
# \n is not considered as a character in the string
# \n is considered as a character in the list
# \n is considered as a character in the file
# \n is considered as a character in the print statement

f.close()
# closes the file 
# always use this at the end of printing file operations
# if not used then the file will not be closed and will be in the memory which will cause problems later
# if we use f.close() and then try to operations on file then it will give an error as the file is closed
# so always open the file again after closing it


f = open('Files/read_function_sample.txt','r')
print("1 :",f.read(5))
f.close()

f = open('Files/read_function_sample.txt','r')
print("2 :",f.readline())
print("3 :",f.readline())
f.close()

f = open('Files/read_function_sample.txt','r')
print("4 :",f.read())
f.close()


f = open('Files/read_function_sample.txt','r')
print("5 :")
for line in f.readlines():
    print(line)
# this will print all the lines of the file
# this is the best way to print all the lines of the file
f.close()



# WRITE FUNCTION

f = open('Files/write_function_sample.txt','w')
f.write("This is a sample to test write function")
# if the file is not present then this will create a file with the mentioned contents
# if the file is present then it will overwrite the file with the mentioned contents
f.close()

# there will be nothing mentioned abt this in output
# directly the changes will be made



# WITH STATEMENT

print("6 :")
with open('Files/with_statement_sample.txt','r') as f:
    print(f.read())
# this will automatically close the file after the execution of the code
# this is the best way to open a file
# no need to use f.close() here




'''OUTPUT
1 : This 
2 : This is a sample 

3 : Read function is used to read files

4 : This is a sample 
Read function is used to read files

5 :
This is a sample

Read function is used to read files

6 :
A sample text file to check with statement
'''

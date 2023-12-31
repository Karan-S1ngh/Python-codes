# WAP to make exact copy of a file


# Method 1: Using read() and write() methods
with open("Files\make.txt") as f:
    content = f.read()
# reads the content of 'make.txt' in 'Files' folder

with open("Files\copy_of_make.txt", "w") as f:
    f.write(content)
# writes the content of 'make.txt' to 'copy_of_make.txt' in 'Files' folder

print("Copy created using read() and write() methods")



# Method 2: Using readlines() and writelines() methods
with open("Files\create.txt") as f:
    content = f.readlines()
# reads the content of 'create.txt' in 'Files' folder

with open("Files\copy_of_create.txt", "w") as f:
    f.writelines(content)
# writes the content of 'create.txt' to 'copy_of_create.txt' in 'Files' folder

print("Copy created using readlines() and writelines() methods")




'''OUTPUT
Copy created using read() and write() methods
Copy created using readlines() and writelines() methods
'''

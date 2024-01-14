# WAP to detect if a file is present or not ina given directory
# Also print the content of the file if present

file_name = input("Enter the name of the file from the folder 'Files' you want to search : ")
# taking input of the file name to be searched

print()


# Method 1
# using os.path.exists()
print("1 :")

import os
os.chdir("Files")
# changes the directory to 'Files'

b = os.listdir()
# listing all the files in the directory

if file_name in b:
    print(f"File {file_name} found")
    with open(file_name) as f:
            print(f"Content of {file_name} is printed below")
            print("{")
            print(f.read())
            print("}")
    
else:
    print(f"File {file_name} not found")

print()


# Method 2
# using exception handling

# here no need to import os module now as it is already imported and 
print("2 :")

def readFile(file_name):
    try:
        with open(file_name) as f:
            print(f"File {file_name} found")
            print(f"Content of {file_name} is printed below")
            print("{")
            print(f.read())
            print("}")
    except FileNotFoundError:
        print(f"File {file_name} not found")
    except Exception as e:
        print(e)
    
readFile(file_name)




'''OUTPUT
1 :
Enter the name of the file from the folder 'Files' you want to search : File_detection_program.txt

1 :
File File_detection_program.txt found
Content of File_detection_program.txt is printed below
{
This is a txt file for file detection program
It checks if a file is present in 'Files' Directory or not
}

2 :
File File_detection_program.txt found
Content of File_detection_program.txt is printed below
{
This is a txt file for file detection program
It checks if a file is present in 'Files' Directory or not
}



Enter the name of the file from the folder 'Files' you want to search : hello.py

1 :
File hello.py not found

2 :
File hello.py not found
'''

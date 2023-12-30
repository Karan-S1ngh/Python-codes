# WAP to make a folder and place multiple files, each file having a table of one number each


a = int(input("Enter the first number from where you want multiplication table : "))

b = int(input("Enter the last number till where you want multiplication table : "))

c = int(input("Enter the number till which u want each number's table : "))


import os
os.chdir("Files")
# changes the directory to 'Files'
os.mkdir("Tables")
# makes a table folder in the directory


for i in range(a, b+1):
    with open(f"Tables/Multiplication table of {i}",'w') as f:
        for j in range(1, c+1):
            f.write(f"{i} x {j} = {i*j}\n")
# creating files for each multiplication table
            

print("Folder generated")




'''OUTPUT
Enter the first number from where you want multiplication table : 2
Enter the last number till where you want multiplication table : 20
Enter the number till which u want each number's table : 10
Folder generated
'''

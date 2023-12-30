# WAP to censor multiple words in a file

words = input("Enter the words you want to censor (separated by commas) : ").split(",")
# split() converts string to list
# split(",") splits the string at every comma and stores the words in a list

with open("Files/Censor_program.txt") as f:
    content = f.read()
    
for word in words:
    if word in content:     
        content = content.replace(word,"*#%#*")
        with open("Files/Censor_program.txt",'w') as f:
            f.write(content)
        print(f"File updated after censoring '{word}'")
    else:
        print(f"'{word}' is not present in the file")
        


'''OUTPUT
Enter the words you want to censor (separated by commas) : donkey,fatman,hello
File updated after censoring 'donkey'
File updated after censoring 'fatman'
'hello' is not present in the file
'''

# WAP to censor a word in a file

word = input("Enter the word you want to censor : ")

with open("Files/Censor_program.txt") as f:
    content = f.read()


if word in content:     
    content = content.replace(word,"*#%#*")
    with open("Files/Censor_program.txt",'w') as f:
        f.write(content)
    print(f"File updated after censoring '{word}'")
else:
    print(f"'{word}' is not present in the file")




'''OUTPUT
Enter the word you want to censor : donkey
File updated after censoring 'donkey'

Enter the word you want to censor : hello
'hello' is not present in the file
'''

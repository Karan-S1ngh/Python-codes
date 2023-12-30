# Checking a word in file

f = open('Files/Check_program.txt','r')
t = f.read()
if 'Hello' in t:
    print("'Hello' is there in the mentioned file")
else:
    print("'Hello' is not there in the mentioned file")
# this will check if the word is present in the file or not  
# if present then it will print the first statement
# else it will print the second statement
f.close()



'''OUTPUT
'Hello' is there in the mentioned file
'''

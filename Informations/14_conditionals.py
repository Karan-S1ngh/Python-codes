# If-elif-else ladder
if(9>0):
    print("9 is greater than 0")
elif(9<0):
    print("9 is less than 0")
else:
    print("9 is equal to 0")

# We use elif instead of 'else if' in python  

# if multiple 'if' are used then all will be independent of each other
# if multiple 'elif' are used then all will be dependent on each other

# only that 'if' will create a ladder which has an 'elif' just right after

a = 8
if(a<9):
    print("a is less than 9")
# Independent if
    
if(a>9):
    print("a is greater than 9")
# Independent if
   
if(a==9):
    print("a is equal to 9")
# Independent if
    
a = 78
if(a>7):
    print("a is greater than 70")
else:
    print("a is lass than or equal to 70")
# if-else ladder




'''OUTPUT
9 is greater than 0
a is less than 9
a is greater than 70
'''
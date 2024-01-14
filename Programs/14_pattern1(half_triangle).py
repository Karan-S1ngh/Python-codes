# Half triangle pattern of *
n = int(input("\nEnter number of rows: "))
print("Half triangle pattern of * :")
for i in range(n):
    print("*" * (i+1))
    
# Half triangle pattern of * in reverse order
n = int(input("\nEnter number of rows: "))
print("Half triangle pattern of * in reverse order :")
for i in range(n):
    print("*" * (n-i))
    
# Half triangle pattern of numbers  
n = int(input("\nEnter number of rows: "))
print("Half triangle pattern of numbers :")
for i in range(n):
    print(str(i+1) * (i+1))

# Half triangle pattern of numbers in reverse order
n = int(input("\nEnter number of rows: "))
print("Half triangle pattern of numbers in reverse order :")
for i in range(n):
    print(str(n-i) * (n-i))


 

'''OUTPUT

Enter number of rows: 3
Half triangle pattern of * :
*
**
***

Enter number of rows: 4
Half triangle pattern of * in reverse order :
****
***
**
*

Enter number of rows: 4
Half triangle pattern of numbers :
1
22
333
4444

Enter number of rows: 3
Half triangle pattern of numbers in reverse order :
333
22
1
'''

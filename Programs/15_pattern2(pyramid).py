# Pyramid of *
n = int(input("\nEnter number of rows: "))
for i in range(n):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1))    
    
# Pyramid of * in reverse order
n = int(input("\nEnter number of rows: "))
for i in range(n):
    print(" " * i, end="")
    print("*" * (2*(n-i)-1))
    
# Pyramid of numbers
n = int(input("\nEnter number of rows: "))
for i in range(n):
    print(" " * (n-i-1), end="")
    print(str(i+1) * (2*i+1))

# Pyramid of numbers in reverse order
n = int(input("\nEnter number of rows: "))
for i in range(n):
    print(" " * i, end="")
    print(str(n-i) * (2*(n-i)-1))
    



'''OUTPUT

Enter number of rows: 3
  *
 ***
*****

Enter number of rows: 3
*****
 ***
  *

Enter number of rows: 3
  1
 222
33333

Enter number of rows: 3
33333
 222
  1

'''
    
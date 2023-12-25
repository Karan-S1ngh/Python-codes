# WAP to check wheter the given number by user is prime or not

num = int(input("Enter a number: "))
prime = True
for i in range(2, num):
    if num % i == 0:
        prime = False
        break
if prime :
    print(num,"is a Prime number")
else:
    print(num,"is not a Prime number")
    
    
    
'''OUTPUT
Enter a number: 7
7 is a Prime number

Enter a number: 8
8 is not a Prime number
'''

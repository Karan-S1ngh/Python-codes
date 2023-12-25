# WAP to find factorial of a given number

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(f"Factorial of {num} is {fact}")



'''OUTPUT
Enter a number: 5
Factorial of 5 is 120

Enter a number: 27
Factorial of 27 is 10888869450418352160768000000
'''

# WAP to find factorial of a given number

# Two methods

num = int(input("Enter a number: "))

# Without using recursion
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(f"1 : Factorial of {num} is {fact}")
# we can use function here

# Using recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(f"2 : Factorial of {num} is {factorial(num)}")
# if we dont use function then also ok but then it wont be an example of recursion




'''OUTPUT
Enter a number: 5
1 : Factorial of 5 is 120
2 : Factorial of 5 is 120

Enter a number: 27
1 : Factorial of 27 is 10888869450418352160768000000
2 : Factorial of 27 is 10888869450418352160768000000
'''

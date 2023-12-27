# WAP to find sum of first n natural numbers

num = int(input("Enter a number: "))

# Without using recursion
sum = 0
for i in range(1, num+1):
    sum = sum + i
print("1 : Sum of first",num,"natural numbers is",sum)


# Using recursion
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
print("2 : Sum of first",num,"natural numbers is",sum(num))
       
    
'''OUTPUT
Enter a number: 10
1 : Sum of first 10 natural numbers is 55
2 : Sum of first 10 natural numbers is 55

Enter a number: 45
1 : Sum of first 45 natural numbers is 1035
2 : Sum of first 45 natural numbers is 1035
'''

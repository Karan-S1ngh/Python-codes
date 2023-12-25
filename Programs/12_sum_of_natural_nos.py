# WAP to find sum of first n natural numbers

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num+1):
    sum = sum + i
print("Sum of first",num,"natural numbers is",sum)

       
    
'''OUTPUT
Enter a number: 10
Sum of first 10 natural numbers is 55

Enter a number: 45
Sum of first 45 natural numbers is 1035
'''

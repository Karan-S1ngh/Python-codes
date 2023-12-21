# Program to print whether age is greater than 18 or not

age = int(input("Enter your age : "))

if(age>18):
    print("You are above 18")
elif(age<18):
    print("You are below 18")
else:
    print("You are 18")
    
    
    
'''OUTPUT
Enter your age : 18
You are 18

Enter your age : 19
You are above 18

Enter your age : 17
You are below 18
'''
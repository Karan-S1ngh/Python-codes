def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        print("Cannot divide by zero")
        return None
    else:   
        return a/b
    
    
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("1.Addition, 2.Subtraction, 3.Multiplication, 4.Division")

choice = int(input("Enter your choice : "))

if choice==1:
    print("Addition is",add(a,b))
elif choice==2:
    print("Subtraction is",sub(a,b))
elif choice==3:
    print("Multiplication is",mul(a,b))
elif choice==4:
    print("Division is",div(a,b))
else:
    print("Invalid choice")
    
    


'''OUTPUT
Enter first number : 10
Enter second number : 20
1.Addition, 2.Subtraction, 3.Multiplication, 4.Division
Enter your choice : 1
Addition is 30

Enter first number : 10
Enter second number : 30
1.Addition, 2.Subtraction, 3.Multiplication, 4.Division
Enter your choice : 2
Subtraction is -20

Enter first number : 5
Enter second number : 20
1.Addition, 2.Subtraction, 3.Multiplication, 4.Division
Enter your choice : 3
Multiplication is 100

Enter first number : 10
Enter second number : 20
1.Addition, 2.Subtraction, 3.Multiplication, 4.Division
Enter your choice : 4
Division is 0.5

Enter first number : 5
Enter second number : 0
1.Addition, 2.Subtraction, 3.Multiplication, 4.Division
Enter your choice : 4
Cannot divide by zero
Division is None

Enter first number : 7
Enter second number : 5
1.Addition, 2.Subtraction, 3.Multiplication, 4.Division
Enter your choice : 5
Invalid choice
'''

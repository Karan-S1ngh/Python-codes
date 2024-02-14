a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

try :
  print(a/b)
except ZeroDivisionError as e:
  print("Exception occured:",e)
else :
  print("No exception occured")
finally :
  print("End of program")
  
  
  

'''OUTPUT
Enter the first number: 5
Enter the second number: 0
Exception occured: division by zero
End of program

Enter the first number: 5
Enter the second number: 5
1.0
No exception occured
End of program
'''

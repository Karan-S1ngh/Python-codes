# WAP to print multiplication table in form of list 
# and store it in a file named Multiplication_table_program_storage.txt
# make it store all the table asked by user as output


# Program to print the multiplication table of a number given by user

n = int(input("Enter the number till which you want the table: "))
num = int(input("Enter the number: "))
table = [num*i for i in range (1, n+1)]
print("Multiplication table list :",table)

# Now storing the data
with open("Files/Multiplication_table_program_storage.txt", "a") as f:
    f.write(str(table))
    f.write("\n")
# opening in append mode so that it will keep on adding tables on different lines

print("Table added to storage file")




'''OUTPUT
Enter the number till which you want the table: 20
Enter the number: 3
Multiplication table list : [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
Table added to storage file

Enter the number till which you want the table: 5
Enter the number: 15
Multiplication table list : [15, 30, 45, 60, 75]
Table added to storage file

Enter the number till which you want the table: 9
Enter the number: 7
Multiplication table list : [7, 14, 21, 28, 35, 42, 49, 56, 63]
Table added to storage file
'''

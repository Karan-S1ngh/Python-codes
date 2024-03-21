# Calculate sum and average of strings and display it


n = int(input("Enter no of strings: "))

list = []
for i in range (1,n+1):
    input_string = input(f"Enter string {i} : ") 
    int_string = int(input_string)
    list.append(int_string)
    
sum_string = sum(list)
print(sum_string)

avg_string = sum(list)/len(list)
if len(list) > 0:
    print(avg_string)
else:
    print(0)




'''OUTPUT
Enter no of strings: 0
0
0

Enter no of strings: 3
Enter string 1 : 5
Enter string 2 : 10
Enter string 3 : 15
30
10.0

Enter no of strings: 5
Enter string 1 : 1
Enter string 2 : 2
Enter string 3 : 3
Enter string 4 : 4
Enter string 5 : 5
15
3.0

Enter no of strings: 5
Enter string 1 : 0
Enter string 2 : 0
Enter string 3 : 0
Enter string 4 : 0
Enter string 5 : 0
0
0.0
''' 

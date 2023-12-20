# Take 5 subject marks input from user and display it in sorted manner

m1 = int(input("Enter marks 1 : "))
m2 = int(input("Enter marks 2 : "))
m3 = int(input("Enter marks 3 : "))
m4 = int(input("Enter marks 4 : "))
m5 = int(input("Enter marks 5 : "))

marks_list = [m1,m2,m3,m4,m5]

marks_list.sort()

print(marks_list)

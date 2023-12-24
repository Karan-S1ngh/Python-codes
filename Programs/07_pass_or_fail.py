# WAP to find out whether a student is pass or fail, if it requires total 40%
# and at least 33% in each subject to pass. Assume 3 subjects and take marks as
# an input from the user.


sub1 = int(input("Enter marks of the first subject : "))
sub2 = int(input("Enter marks of the second subject : "))
sub3 = int(input("Enter marks of the third subject : "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You fail because you have percentage less than 33 in one of the subjects")
elif(sub1+sub2+sub3)/3 < 40:
    print("You fail due to total percentage less than 40")
else:
    print("Congratulations! You passed the exam")
 
   


'''OUTPUT
Enter marks of the first subject : 45
Enter marks of the second subject : 67
Enter marks of the third subject : 32
You fail because you have percentage less than 33 in one of the subjects

Enter marks of the first subject : 39
Enter marks of the second subject : 38
Enter marks of the third subject : 40
You fail due to total percentage less than 40

Enter marks of the first subject : 50
Enter marks of the second subject : 99
Enter marks of the third subject : 78
Congratulations! You passed the exam
'''

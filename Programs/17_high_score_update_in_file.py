# Read a new score from user and read old score from Score_program file   
# if the new score is greater than the old score
# then update the score in file otherwise no changes to be made


a = int(input("Enter the highest score : "))
# input for the new score

with open('Files/Score_program.txt','r') as f:
    old_score = f.read()
# reading the old score from the file

if old_score == '':
    with open('Files/Score_program.txt','w') as f:
            f.write(str(a))
    print('No old score so new score registered')
# if there is no old score then write the new score in the file
    
elif a > int(old_score) :
    with open('Files/Score_program.txt','w') as f:
            f.write(str(a))
    print('New score updated')
# if the new score is greater than the old score then write the new score in the file
   
else:
    print('No changes made as this is not greater than the old score')
# if the new score is not greater than the old score then no changes to be made  




'''OUTPUT
Enter the highest score : 100
No old score so new score registered

Enter the highest score : 500
New score updated

Enter the highest score : 300
No changes made as this is not greater than the old score
'''

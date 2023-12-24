# A spam comment consists of following keywords
# "make a lot of money", "buy now", "subscribe this", "click this"
# Write a program to take a comment as input from the user and print whether it is spam or not.


comment = input("Enter your comment : ")

if("make a lot of money" in comment):
    spam = True
elif("buy now" in comment):
    spam = True
elif("subscribe this" in comment):
    spam = True
elif("click this" in comment):
    spam = True
else:
    spam = False
    
if(spam):
    print("This comment is spam")
else:
    print("This comment is not spam")
 
 
 
   
'''OUTPUT
Enter your comment : make a lot of money by participating in this
This comment is spam

Enter your comment : buy now to get max profit
This comment is spam

Enter your comment : subscribe this channel to get chance to earn money
This comment is spam

Enter your comment : click this link for easy money
This comment is spam

Enter your comment : gain a lot of profit by doing this survey
This comment is not spam
'''

# WAP to find names from list having first name S
names = ["Sachin","Sourav","Rahul","Saurabh"]
print("1 :")
for i in names:
    if i[0] == "S":
        print(i)
     
# WAP to find names from list having length 6 or first name S and last name h
print("2 :")
names = ["Karan","Sangeeta","Rahul","Sharma"]
for i in names:
    if len(i) == 6 or i[0] == "S" and i[-1] == "h":
        print(i)




'''OUTPUT
1 :
Sachin
Sourav
Saurabh
2 :
Sharma
'''        
        
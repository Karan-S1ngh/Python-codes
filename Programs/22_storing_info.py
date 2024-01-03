# WAP to store info of programmers working in google using class

class Programmer:
    company = 'Google'
    def __init__(self, name, age, salary, language):
        self.name = name
        self.age = age
        self.salary = salary
        self.language = language
    def getDetails(self):
        print(f"Name : {self.name} \nAge : {self.age} \nSalary : {self.salary} \nLanguage : {self.language}")
    
p1 = Programmer('Mohan', 29, 150000, 'C++')
p2 = Programmer('Ramesh', 30, 100000, 'Java')
p3 = Programmer('Sunil', 25, 200000, 'C')
p4 = Programmer('Hari', 22, 250000, 'Python')
p5 = Programmer('Karan', 19, 300000, 'Python')

print("Company :",p1.company)
print()

print("Programmer 1")
p1.getDetails()
print()             # prints a blank line

print("Programmer 2")
p2.getDetails()
print()

print("Programmer 3")
p3.getDetails()
print()

print("Programmer 4")
p4.getDetails()
print()

print("Programmer 5")
p5.getDetails()




'''OUTPUT
Company : Google

Programmer 1
Name : Mohan
Age : 29
Salary : 150000
Language : C++

Programmer 2
Name : Ramesh
Age : 30
Salary : 100000
Language : Java

Programmer 3
Name : Sunil
Age : 25
Salary : 200000
Language : C

Programmer 4
Name : Hari
Age : 22
Salary : 250000
Language : Python

Programmer 5
Name : Karan
Age : 19
Salary : 300000
Language : Python
'''

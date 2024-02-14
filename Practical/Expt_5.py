class Person:
    def __init__(self,id, name, age, grade):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"ID : {self.id}\nName: {self.name}\nAge: {self.age}\nGrade: {self.grade}")

class Sports(Person):
    def __init__(self,id, name, age, grade, sports_grade):
        super().__init__(id, name, age, grade)
        self.sports_grade = sports_grade

    def get_details(self):
      super().display()
      print(f"Sports Grade: {self.sports_grade}")

obj1 = Sports('22AD1027', 'Karan', '19', '99', '90')
print(obj1.get_details())
print()
obj2 = Sports('22AD1009', 'Luqmaan', '18', '90', '90')
print(obj2.get_details())
print()
obj2 = Sports('22AD1070', 'Dev', '19', '80', '80')
print(obj2.get_details())




'''OUTPUT
ID : 22AD1027
Name: Karan
Age: 19
Grade: 99
Sports Grade: 90
None

ID : 22AD1009
Name: Luqmaan
Age: 18
Grade: 90
Sports Grade: 90
None

ID : 22AD1070
Name: Dev
Age: 19
Grade: 80
Sports Grade: 80
None
'''

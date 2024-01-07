# @property is a decorator by which we define a dynamic property
# we define it in class as a method but can class it as a property

# Method name with @property decorator is called getter method 
# to define setter we will use @name.setter

# setter is used to change the value of attributes using object
# getter is used to get the value of attributes using object


class Employee:
    company = 'Apple'
    salary = 5000
    salaryBonus = 500
    # totalSalary = 5500
    # but by this if bonus is changes we have to change this everytime
    # so we use @property decorator
    
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus
    # we dont need to change total everytime bonus is changed now
    # we can call it as a property
    
    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary
    # here we are changing salaryBonus using totalSalary
    # we can call it as a property
    # if we change total using object then this automatically updates the salary and bonus
    

e = Employee()

print("1 : Total salary defined is",e.totalSalary)
# prints 5500 as salary = 5000 and bonus = 500 as defined in class
# totalSalary is being called as a property(not method)
print("2 : Salary defined is",e.salary)
print("3 : Bonus defined is",e.salaryBonus)

print()

e.totalSalary = 6000
# totalSalary should be 5500
# we are changing it here to 6000
# setter is called here
# so salaryBonus is changed to 1000 
# and salary remains 5000
# so totalSalary is 6000
print("4 : Total salary is changed to",e.totalSalary)
print("5 : Salary after changing total salary is",e.salary)
print("6 : Bonus after changing total salary is",e.salaryBonus)




'''OUTPUT
1 : Total salary defined is 5500
2 : Salary defined is 5000
3 : Bonus defined is 500

4 : Total salary is changed to 6000
5 : Salary after changing total salary is 5000
6 : Bonus after changing total salary is 1000
'''    
    
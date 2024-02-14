class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id
    
  def display(self):
    print(f"ID: {self.id} \nName: {self.name}")

object = Employee("Karan", "100")
object.display()




'''OUTPUT
ID: 100 
Name: Karan
'''

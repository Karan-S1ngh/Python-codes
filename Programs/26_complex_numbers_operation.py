# WAP to represent complex numbers and allows to do operations on it

class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real, self.imaginary * other.imaginary)

    def __truediv__(self, other):
        return Complex(self.real / other.real, self.imaginary / other.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    

c1 = Complex(2, 3)
c2 = Complex(4, 5)

print("0.Exit, 1.Addition, 2.Subtraction, 3.Multiplication, 4.Division")
print()

while True:
    choice = int(input("Enter your choice : "))
    if choice == 0:
        print("Ended")
        break
    elif choice == 1:
        print(f"Addition = {c1 + c2}")
    elif choice == 2:
        print(f"Subtraction = {c1 - c2}")
    elif choice == 3:
        print(f"Multiplication = {c1 * c2}")
    elif choice == 4:
        print(f"Division = {c1 / c2}")
    else:
        print("Invalid Choice")
    print()
    
# This could be made user defined too by asking the real and imaginary part of complex number from user 
# and then performing the operation on it
# and more operations can be added in class 
  


 
'''OUTPUT
0.Exit, 1.Addition, 2.Subtraction, 3.Multiplication, 4.Division

Enter your choice : 5
Invalid Choice

Enter your choice : 1
Addition = 6 + 8i

Enter your choice : 2
Subtraction = -2 + -2i

Enter your choice : 3
Multiplication = 8 + 15i

Enter your choice : 4
Division = 0.5 + 0.6i

Enter your choice : 0
Ended
''' 
        
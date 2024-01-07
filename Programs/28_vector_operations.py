# WAP to represent a vector of n dimension and allows to do operations on it

class Vector:
    def __init__(self, v):
        self.vec = v
        
    def __str__(self):
        vector = ''
        index = 0
        for i in self.vec:
            vector += f" {i}a^{index} +"
            index += 1
        return vector[:-1]
    
    def __add__(self, other):
        if len(self.vec) == len(other.vec):
            result = []
            for i in range(len(self.vec)):
                result.append(self.vec[i] + other.vec[i])
            return Vector(result)
        else:
            return "Addition not possible"
        
    def __sub__(self, other):
        if len(self.vec) == len(other.vec):
            result = []
            for i in range(len(self.vec)):
                result.append(self.vec[i] - other.vec[i])
            return Vector(result)
        else:
            return "Subtraction not possible"
        
    def __mul__(self, other):
        if len(self.vec) == len(other.vec):
            result = []
            for i in range(len(self.vec)):
                result.append(self.vec[i] * other.vec[i])
            return Vector(result)
        else:
            return "Dot product not possible"
    
    def cross(self, other):
            if len(self.vec) == len(other.vec) == 3:
                result = [
                    self.vec[1] * other.vec[2] - self.vec[2] * other.vec[1],
                    self.vec[2] * other.vec[0] - self.vec[0] * other.vec[2],
                    self.vec[0] * other.vec[1] - self.vec[1] * other.vec[0]
                ]
                return Vector(result)
            else:
                return "Cross product not possible"
        
         
    def __truediv__(self, other):
        if len(self.vec) == len(other.vec):
            result = []
            for i in range(len(self.vec)):
                result.append(self.vec[i] / other.vec[i])
            return Vector(result)
        else:
            return "Division not possible"
        
    def __len__(self):
        return len(self.vec)


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print(f"First vector = {v1}")
print(f"Second vector = {v2}")
print()

print("0.Exit, 1.Addition, 2.Subtraction, 3.Dot Product, 4.Cross Product, 5.Division, 6.Length")
print()

while True:
    choice = int(input("Enter your choice : "))
    if choice == 0:
        print("Ended")
        break
    elif choice == 1:
        print(f"Addition = {v1 + v2}")
    elif choice == 2:
        print(f"Subtraction = {v1 - v2}")
    elif choice == 3:
        print(f"Dot Product = {v1 * v2}")
    elif choice == 4:
        print(f"Cross Product = {v1.cross(v2)}")
    elif choice == 5:        
        print(f"Division = {v1 / v2}")
    elif choice == 6:
        print(f"Length of first vector = {len(v1)}")
        print(f"Length of second vector = {len(v2)}")
    else:
        print("Invalid Choice")
    print()



# This could be made user defined too by asking the real and imaginary part of complex number from user
# and then performing the operation on it
# and more operations can be added in class

        
        
  
'''OUTPUT
First vector =  1a^0 + 2a^1 + 3a^2 
Second vector =  4a^0 + 5a^1 + 6a^2 

0.Exit, 1.Addition, 2.Subtraction, 3.Dot Product, 4.Cross Product, 5.Division, 6.Length

Enter your choice : 7
Invalid Choice

Enter your choice : 6
Length of first vector = 3
Length of second vector = 3

Enter your choice : 5
Division =  0.25a^0 + 0.4a^1 + 0.5a^2

Enter your choice : 4
Cross Product =  -3a^0 + 6a^1 + -3a^2

Enter your choice : 3
Dot Product =  4a^0 + 10a^1 + 18a^2

Enter your choice : 2
Subtraction =  -3a^0 + -3a^1 + -3a^2

Enter your choice : 1
Addition =  5a^0 + 7a^1 + 9a^2

Enter your choice : 0
Ended
'''  
    
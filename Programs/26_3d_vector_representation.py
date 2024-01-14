# WAP to represent a 3d vector

class Vector:
    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[0]}k"
    
a = int(input("Enter the component of vector along x-axis : "))
b = int(input("Enter the component of vector along y-axis : "))
c = int(input("Enter the component of vector along z-axis : "))

v1 = Vector([a, b, c])
print("Vector =",v1)

# here we are self.vec[0],etc because we are giving the vec in object as a list
# if we dont use list then error would occur as vec is a single argument but a,b,c collectively are 3 arguments




'''OUTPUT
Enter the component of vector along x-axis : 4
Enter the component of vector along y-axis : 6
Enter the component of vector along z-axis : 8
Vector = 4i + 6j + 4k
'''

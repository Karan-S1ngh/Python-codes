# WAP to create a class for representing 2d vector and using it to create a class for representing 3d vector

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"{self.x}i + {self.y}j")
        
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def display(self):
        print(f"{self.x}i + {self.y}j + {self.z}k")
        

v2 = Vector2D(1, 2)
v2.display()

v3 = Vector3D(1, 2, 3)
v3.display()


# we can make this user defined program too easily
# also this can be expanded to 4d vector by inheriting the 3d vector and defining the 4th dim
# and so on




'''OUTPUT
1i + 2j
1i + 2j + 3k
'''

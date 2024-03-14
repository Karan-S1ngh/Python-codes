class Base(object): 
    pass 
 
class Derived(Base): 
    pass 

print(issubclass(Derived, Base)) 
print(issubclass(Base, Derived)) 

d = Derived() 
b = Base() 

print(isinstance(b, Derived)) 
print(isinstance(d, Base)) 




'''OUTPUT
True
False
False
True
'''

# some other dunder methods

# __str__()
# used to set what gets displayed upon calling str(object)
# it is called when we directly print object

class  Example:
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return f"Value of x is {self.x}"
    
obj = Example(5)
print("1 :",obj)


# __len__()
# used to set what gets displayed upon calling len(object)
# it is called when we call len(object)
class Nothing:
    def __init__(self):
        pass
    def __str__(self):
        return "Nothing"
    def __len__(self):
        return 2
    
obj = Nothing()
print("2 :",obj)
print("3 :",len(obj))



# if __str__ and __len__ are not defined in class then printing object and len(object) will give error




'''OUTPUT
1 : Value of x is 5
2 : Nothing
3 : 2
'''    

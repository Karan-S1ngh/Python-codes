class A: 
    def test(self): 
        print("test of A called") 
        
class B(A): 
    def test(self): 
        print("test of B called") 
        super().test() 
        
class C(A): 
    def test(self): 
        print("test if C called") 
        super().test() 
        
class D(B,C): 
 def test2(self): 
    print("test of D called") 
    
obj = D() 
obj.test() 




'''OUTPUT
test of B called
test if C called
test of A called
'''

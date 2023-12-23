a = None
if (a is None):
    print("1 : Yes")
else:
    print("2 : No")

a = None    
print("3 :",a is None)
# if true then true will be printed else false

print("4 :",15 is 14)
   
 
a = [23, 67, 89]
print("5 :",23 in a)
print("6 :",234 in a)
# If element present in a then true will be printed else false

a = {46, 67, 89}
if (46 in a):
    print("7 : Yes")
else:
    print("8 : No")
    
    
    

'''OUTPUT
1 : Yes
3 : True
4 : False
5 : True
6 : False
7 : Yes
'''

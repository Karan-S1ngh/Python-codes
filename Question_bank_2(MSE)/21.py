tup=(10,30,15,9) 
s=1 
t=0 
for i in range(s,4): 
    t=t+tup[i] 
    print(i,":",t) 
    t=t+tup[0]*10 
    print(t) 
    
    
    

'''OUTPUT
1 : 30
130
2 : 145
245
3 : 254
354
'''

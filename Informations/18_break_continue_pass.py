# Break statement 
# can be used to stop the loop before it has looped through all the items
print("'1' :")
for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("Loop ended")
# here the loop will stop when i becomes 2 and will not print nos from 2
# else will not be executed as loop is not terminated successfully due to break statement


# Continue statement 
# can be used to stop the current iteration of the loop and continue with the next
print("'2' :")
for i in range(5):
    if i == 2:
        continue
    print(i)
# here the loop will not print 2 but will continue with the next iteration 


# pass statement 
# A null statement. It instructs to do nothing 
# It can be used to leave a function or loop empty and methods on them can be decided later
print("'3' :")
for i in range(5):
    if i == 2:
        pass
    print(i)
# here the loop will print 2 as pass statement will not do anything and will continue with the next iteration


# pass, continue and break can be used with all loops (if, while and for)




'''OUTPUT
'1' :
0
1
'2' :
0
1
3
4
'3' :
0
1
2
3
4
'''

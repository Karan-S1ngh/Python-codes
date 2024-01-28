# Find greatest number among of the 4 numbers given as input by the user

# Two ways to do this without using loops and one way to do using loops

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
d = int(input("Enter 4th number : "))


# First method (using loops)
e = [a, b, c, d]
l = e[0]
for i in e:
    if i > l:
        l = i
print("1 :",l,"is greatest")
# we can also use this method to check max number in a array with its index 

# Alternative method (similar to previous method)
# for i in range(len(e)):
#     if e[i] > l:
#         l = e[i]
# print(l)



# Second method (easier way without loop)
def greatest():           
    if(a>b):
        f1 = a
    else:
        f1 = b
        
    if(c>d):
        f2 = c
    else:
        f2 = d
        
    if(f1>f2):
        return f1
    else:
        return f2
# if we dont use function then also ok just remove def greatest and use print instead of return in the program
print(f"2 : {greatest()} is greatest")


# Third method (without loop)
if (a > b):
    if (a > c):
        if (a > d):
            print("1 : 1st number is greatest")
        else:
            print("1 : 4th number is greatest")
    else:
        if (c > d):
            print("1 : 3rd number is greatest")
        else:
            print("1 : 4th number is greatest")
else:
    if (b > c):
        if (b > d):
            print("1 : 2nd number is greatest")
        else:
            print("1 : 4th number is greatest")
    else:
        if (c > d):
            print("1 : 3rd number is greatest")
        else:
            print("1 : 4th number is greatest")




'''OUTPUT
Enter 1st number : 5
Enter 2nd number : 6
Enter 3rd number : 4
Enter 4th number : 1
1 : 6 is greatest
2 : 6 is greatest
1 : 2nd number is greatest
'''

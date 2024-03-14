# Explain break, continue and pass statement with suitable example of each.


# break
# The break statement terminates the loop containing it. 
# Control of the program flows to the statement immediately after the body of the loop.
# Example:
for i in range(6):
    if i == 3:
        break
    print(i)
print("The end")
print()

# continue
# The continue statement is used to skip the rest of the code inside a loop for the current iteration only.
# Example:
for i in range(6):
    if i == 3:
        continue
    print(i)
print("The end")
print()

# pass
# The pass statement is used as a placeholder for future code.
# Example:
for i in range(6):
    if i == 3:
        pass
    print(i)
print("The end")




'''OUTPUT
0
1
2
The end

0
1
2
4
5
The end

0
1
2
3
4
5
The end
'''

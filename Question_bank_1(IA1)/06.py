# Explain all bitwise operators of python with suitable examples of each.


a = int(input("Enter a : "))
b = int(input("Enter b : "))

# In Python, we have the following bitwise operators:

# 1. Bitwise AND (&): It is used to perform bitwise AND operation on the binary representations of two numbers.
# Example:
c = a & b
print("Bitwise AND :",c)

# 2. Bitwise OR (|): It is used to perform bitwise OR operation on the binary representations of two numbers.
# Example:
c = a | b
print("Bitwise OR :",c)

# 3. Bitwise XOR (^): It is used to perform bitwise XOR operation on the binary representations of two numbers.
# Example:
c = a ^ b
print("Bitwise XOR :",c)

# 4. Bitwise NOT (~): It is used to perform bitwise NOT operation on the binary representation of a number.
# Example:
c = ~a
print("Bitwise NOT of a :",c)
c = ~b
print("Bitwise NOT of b :",c)

# 5. Bitwise Left Shift (<<): It is used to perform bitwise left shift operation on the binary representation of a number.
# Example:
c = a << 2
print("Bitwise Left Shift of a :",c)

# 6. Bitwise Right Shift (>>): It is used to perform bitwise right shift operation on the binary representation of a number.
# Example:
c = a >> 2
print("Bitwise Right Shift of a :",c)




'''OUTPUT
Enter a : 10
Enter b : 15
Bitwise AND : 10
Bitwise OR : 15
Bitwise XOR : 5
Bitwise NOT of a : -11
Bitwise NOT of b : -16
Bitwise Left Shift of a : 40
Bitwise Right Shift of a : 2
'''

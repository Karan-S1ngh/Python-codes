print("1  :",pow(2,3))
# prints 2 to the power 3


print("2  :",abs(-4))
# prints absolute value of -4


print("3  :",round(3.141592653589793))
# prints round figure of the given number

print("4  :",round(6.999999999,4))
# prints round figure of the given number till 2 decimal places

print("5  :","%0.4f" % 6.999999999)
# prints round figure of the given number till 2 decimal places

# difference between round function and %f
# Round(a,4) function for 6.9999 will give 7.0 But %f will give 7.0000
# so round function will not print extra zeroes but %f will print extra zeroes 


a = int(input('Enter a : '),2)   # 2 is the base of the input
# or a = int(input('Enter a '),base=2)
# Only 0,1 allowed to be given as input and any other number will give error
# eg, 001, 11110, etc
# typecastes binary input to decimal
print("6  :",a)
# prints the decimal output of the given binary input

'''a = bool(int(input('Enter a ')))  ''' 
# typecastes input to integer and then to boolean
''' print(a)'''
# any number other than 0 will give True and 0 will give False


print("7  : ",end='')
print('Karan', 'Ram', 'Shyam', sep = ' and ')
# separates the given strings by ' and '


a = 10
print("8  :",bin(a))
# prints binary of the given number
# 0b is added before the binary number

print("9  :",oct(a))
# prints octal of the given number
# 0o is added before the octal number

print("10 :",hex(a))
# prints hexadecimal of the given number
# 0x is added before the hexadecimal number


print("11 :",chr(65))
# prints the character of the given ASCII value

print("12 :",ord('A'))
# prints the ASCII value of the given character


print("13 :",divmod(10,3))
# prints the quotient and remainder of the given numbers
# prints (3,1) as output
# 3 is the quotient and 1 is the remainder


print("14 :",max(1,2,3,4,5,6,7,8,9))
# prints the maximum number from the given numbers

print("15 :",min(1,2,3,4,5,6,7,8,9))
# prints the minimum number from the given numbers

print("16 :",sum([1,2,3,4,5,6,7,8,9]))
# prints the sum of the given numbers


a,b = 10,20
print("17 :",a^b)
# prints the XOR of the given numbers

print("18 :",not(a^b))
# prints the XNOR of the given numbers

print("19 :",~a)
# prints the 1's complement of the given number

print("20 :",a<<2)
# prints the left shift of the given number by 2
# 10 is 1010 in binary
# 1010 << 2 = 101000 = 40

print("21 :",a>>2)
# prints the right shift of the given number by 2
# 10 is 1010 in binary
# 1010 >> 2 = 10 = 2

# All the operations from 17 to 21 are bitwise operations
# Bitwise operations are performed on binary numbers




'''OUTPUT
1  : 8
2  : 4
3  : 3
4  : 7.0
5  : 7.0000
Enter a : 1011
6  : 11
7  : Karan and Ram and Shyam
8  : 0b1010
9  : 0o12
10 : 0xa
11 : A
12 : 65
13 : (3, 1)
14 : 9
15 : 1
16 : 45
17 : 30
18 : False
19 : -11
20 : 40
21 : 2
'''

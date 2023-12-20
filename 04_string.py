name = 'Larry'
print("1 :",name[0])    
# will print 0th character(L here) of string

# u cannot change any character of string
# for example   name[0] = 'p'     will give error

name = 'Karan'
print("2 :",name[0:3])   
# this will print all character from 0th place to 2nd place
# 3rd place character not included 

# negative indices use to print from last character
# -1 represents last character, -2 second last character and so on
name = 'Harry'
print("3 :",name[-4])
# this prints the 4th last character of a string

name = 'HariIsHere'
print("4 :",name[0:4:2])
# this will print all character from 0 to 4 index skipping every 2nd index
# 2 is called step size
# so h,r will be printed and a,i will be ignored

name = 'SariIsHere'
print("5 :",name[1::2])
# prints character from first character to last character skipping every 2nd character, i.e, skips one character in between

name = 'Hari'
print("6 :",name[1:])
# prints character from 1st index till last index

name = 'Shree'
print("7 :",name[:4])
# prints character from first index till 4th index



'''OUTPUT
1 : L
2 : Kar
3 : a
4 : Hr
5 : aisee
6 : ari
7 : Shre
'''

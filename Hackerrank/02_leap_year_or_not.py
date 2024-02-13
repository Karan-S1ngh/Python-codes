# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. 
# It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

# Task
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.


def is_leap(year):
    
    # variable to check the leap year
    leap = False
    
    # divided by 100 means century year
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        leap = True
        # change leap to True

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 ==0) and (year % 100 != 0):
        leap = True
        # Change leap to true

    # else not a leap year
    else:      
        pass
    
    return leap




'''OUTPUT
1990
False

2000
True
'''

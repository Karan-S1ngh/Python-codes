# WAP to greet the user according to the time of the day

import time
current_time = time.strftime('%H:%M:%S')
print("Current time :",current_time)
if current_time < '12:00:00':
    print("Good Morning!")
elif current_time < '17:00:00':
    print("Good Afternoon!")
else:
    print("Good Evening!")

# This is the program to greet the user according to the time of the day
# We are using the time module to get the current time
# The time module has a method strftime() which returns the current time in the format we want
# We are using the format '%H:%M:%S' which returns the time in hours, minutes and seconds
# If the time is less than 12:00:00, it is morning
# If the time is less than 17:00:00, it is afternoon
# Else, it is evening




'''OUTPUT
Current time : 14:47:41
Good Afternoon!

Current time : 23:47:41
Good Evening!

Current time : 07:47:41
Good Morning!

Current time : 00:34:24
Good Morning!
'''  

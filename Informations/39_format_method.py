# format method

# It is used to format the values in string into desired output

# Before python 3.6 'f' was not there so format method had to be used
# After python 3.6 'f' is there so format method is not used that much


a = '{} is a good {}'.format('Ram','boy','gaming')
print("1 :",a)
# "gaming" wont be printed as there are only two placeholders ({})
# if there would have been a third placeholder then "gaming" would have been called there

# We can also use index to format the string    
a = '{1} is a good {0}'.format('athelete','Ram','gaming')
print("2 :",a)
# "gaming" wont be used here anywhere as it is at 2nd index and only 0th and 1st index are called

# We can also use keyword and index to format the string
a = '{0} is a good {skill}'.format('Ram','hello',skill = 'learner')
print("3 :",a)
# hello is not called so wont be printed

skill = 'playing games'
a = '{} is {}'.format("Ram",skill)
print("4 :",a)


# We can also use f string to format the string
# This is possible for version 3.6 and higher
name = 'Ram'
skill = 'Listening'
a = f'{name} is good at {skill}'
print("5 :",a)




'''OUTPUT
1 : Ram is a good boy
2 : Ram is a good athelete
3 : Ram is a good learner
4 : Ram is playing games
5 : Ram is good at Listening
'''

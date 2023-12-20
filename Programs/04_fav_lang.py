# Take input from 4 people their favourite subjects and display it with their names without using loops

# d = {}
# for i in range(4):
#     name = input("Enter your name : ")
#     fav_subject = input("Enter your favourite subject : ")
#     d[name] = fav_subject
# print(d)
# Using for loop


s = {}
s['Rajesh'] = input('Rajesh, what is your favorite subject? ')
s['Mohan'] = input('Mohan, what is your favorite subject? ')
s['Suresh'] = input('Suresh, what is your favorite subject? ')
s['Kamlesh'] = input('Kamlesh, what is your favorite subject? ')

print('\nFavorite Subjects:',s)

# If 2 names are same then the input given second time will be registered
# If 2 subjects will be same then no problem




'''OUTPUT
Rajesh, what is your favorite subject? C++
Mohan, what is your favorite subject? Python
Suresh, what is your favorite subject? Java 
Kamlesh, what is your favorite subject? C

Favorite Subjects: {'Rajesh': 'C++', 'Mohan': 'Python', 'Suresh': 'Java', 'Kamlesh': 'C'}
'''
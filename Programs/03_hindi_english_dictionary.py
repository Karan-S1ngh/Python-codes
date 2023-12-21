# Making a Hindi to English dictionary

d = {     
    'pankha' : 'fan' ,
    'aam' : 'mango' ,
    'gadi' : 'car' ,
    'bhains' : 'buffalo' ,
    'kutta' : 'dog' ,
    'billi' : 'cat' ,
    'kela' : 'banana' ,
    'kamra' : 'room' ,
    'kursi' : 'chair' ,
    'kagaz' : 'paper' ,
    'kalam' : 'pen' ,
    'kitaab' : 'book' ,
    'chandi' : 'silver'  
}

print("Options are :",list(d.keys()))
# Prints all the keys in a form of list

a = input("Enter the Hindi word : ")
# Takes input from user
print("English word for",a,"is :",d.get(a))




'''OUTPUT
Options are : ['pankha', 'aam', 'gadi', 'bhains', 'kutta', 'billi', 'kela', 'kamra', 'kursi', 'kagaz', 'kalam', 'kitaab', 'chandi']
Enter the Hindi word : kalam
English word for kalam is : pen

Options are : ['pankha', 'aam', 'gadi', 'bhains', 'kutta', 'billi', 'kela', 'kamra', 'kursi', 'kagaz', 'kalam', 'kitaab', 'chandi']
Enter the Hindi word : aam
English word for aam is : mango
'''

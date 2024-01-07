# Guessing game

# User has to guess number between 1 to 100
# Computer will generate a random number between 1 to 100
# Then it will tell if the number generated is greater or smaller than or greater than the user guess
# user will keep on guessing until they have guessed the correct number 
# computer also print in how many guesses the user has correctly guessed the number


import random
computer = random.randint(1,100)

user = None
count = 0

print("Welcome to the Guessing Game")
print()

while user != computer:
    user = int(input("Guess the number: "))
    count += 1
    if user == computer:
        print("You guessed it right!")
        print(f"You took '{count}' guesses to guess the number '{computer}'")
    else:
        if user > computer:
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
    print()




'''OUTPUT
Welcome to the Guessing Game

Guess the number: 56
You guessed it wrong! Enter a smaller number

Guess the number: 67
You guessed it wrong! Enter a smaller number

Guess the number: 78
You guessed it wrong! Enter a smaller number

Guess the number: 45
You guessed it wrong! Enter a smaller number

Guess the number: 34
You guessed it right!
You took '5' guesses to guess the number '34'

'''

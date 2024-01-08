# Rock paper scissors game against computer


# Game logic function
def game(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print("Please enter a valid move!")


# Main program function 
def Program():
    # Computer choice
    import random
    c = random.choice(["rock", "paper", "scissors"])

    # User input
    u = input("Please choose rock, paper or scissors: ")

    # Print user choice
    print("Your choice: " + u)

    # Print computer choice
    print("Computer choice: " + c)

    # Print Result
    game(u, c)


# Welcome message
print()
print("Welcome to the Rock Paper Scissors game!")
print()


# Asking user to continue or stop
while True:
    Program()
    print()
    q = input("Do you want to continue? (y/n): ")
    if q == "n":
        break
    else:
        print()
        continue
    
    
# Exit message
print()
print("Thanks for playing!")
print()



# Description
# First we intialised a function containing game logic
# Then we intialised a function containing main program
# Then we used while loop to ask user to continue or stop and used the main program function in it and 
# Then we used if else statement in the while loop to break the loop if user wants to stop


# in this instead of contiuning the game till user ending, we can create a file and store all the data of each game in it
# we can also do the combination of both




'''OUTPUT

Welcome to the Rock Paper Scissors game!

Please choose rock, paper or scissors: hello
Your choice: hello
Computer choice: paper
Please enter a valid move!

Do you want to continue? (y/n): y

Please choose rock, paper or scissors: rock
Your choice: rock
Computer choice: scissors
You win!

Do you want to continue? (y/n): y

Please choose rock, paper or scissors: paper
Your choice: paper
Computer choice: paper
It's a tie!

Do you want to continue? (y/n): y

Please choose rock, paper or scissors: scissors
Your choice: scissors
Computer choice: rock
Computer wins!

Do you want to continue? (y/n): n

Thanks for playing!

'''

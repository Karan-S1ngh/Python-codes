# Rock paper scissors game against computer


# Game logic function
def game(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "r":
        if computer_choice == "p":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == "p":
        if computer_choice == "s":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == "s":
        if computer_choice == "r":
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print("Please enter a valid move!")


# Main program function 
def Program():
    # Computer choice
    import random
    c = random.choice(["r", "p", "s"])

    # User input
    u = input("Please choose r (rock), p (paper) or s (scissors): ")

    # Print user choice
    print("Your choice: " + u)

    # Print computer choice
    print("Computer choice: " + c)

    # Print Result
    game(u, c)


# Welcome message
print()
print("Welcome to the Rock, Paper and Scissors game!")
print()


# Program with asking user to continue or stop
while True:
    Program()
    print()
    q = input("If you want to continue type 'y': ")
    # if the user enters anything other than y then the loop will break
    if q == "y":
        print()
        continue
    else:
        break
    
    
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

Please choose r (rock), p (paper) or s (scissors): hello
Your choice: hello
Computer choice: p
Please enter a valid move!

"If you want to continue type 'y': y

Please choose r (rock), p (paper) or s (scissors): r
Your choice: r
Computer choice: s
You win!

"If you want to continue type 'y': y

Please choose r (rock), p (paper) or s (scissors): p
Your choice: p
Computer choice: p
It's a tie!

"If you want to continue type 'y': y

Please choose r (rock), p (paper) or s (scissors): s
Your choice: s
Computer choice: r
Computer wins!

"If you want to continue type 'y': no

Thanks for playing!

'''

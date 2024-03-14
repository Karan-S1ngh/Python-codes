# Wap to create a dictionary with cricket players names and scores in matches, 
# also retrieve runs by entering players name (user defined)


# Function to create a dictionary with cricket player names and scores
def create_player_scores_dict():
    player_scores = {}
    n = int(input("Enter number of players: "))
    for i in range(n):
        name = input(f"Enter player {i+1}'s name: ")
        score = int(input(f"Enter {name}'s score: "))
        player_scores[name] = score
    return player_scores

# Function to retrieve runs by entering player's name
def retrieve_runs(player_scores):
    player_name = input("Enter player's name to retrieve runs: ")
    if player_name in player_scores:
        print(f"{player_name} scored {player_scores[player_name]} runs.")
    else:
        print("Player not found in the dictionary.")

# Main program
player_scores_dict = create_player_scores_dict()
print("Player scores dictionary:", player_scores_dict)

retrieve_runs(player_scores_dict)




'''OUTPUT
Enter number of players: 3
Enter player 1's name: karan
Enter karan's score: 100
Enter player 2's name: someone
Enter someone's score: 49
Enter player 3's name: anyone
Enter anyone's score: 99
Player scores dictionary: {'karan': 100, 'someone': 49, 'anyone': 99}
Enter player's name to retrieve runs: karan
karan scored 100 runs.
'''

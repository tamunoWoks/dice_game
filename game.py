#Import necessary module
import random

def roll():
    """Roll a die and return a value between 1 and 6."""
    return random.randint(1, 6)
    
def get_number_of_players():
    """Prompt the user for the number of players and validate the input."""
    while True:
        players = input("Enter the number of players (2-4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                return players
            else:
                print("Number must be between 2-4.")
        else:
            print("Invalid input. Please enter a number")

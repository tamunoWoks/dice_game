"""
Python script to implement a dice game for 2 to 4 players. 
"""

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

def play_turn(player_no, player_scores):
    """Simulate a player's turn."""
    print(f"\nPlayer number {player_no + 1} turn has just started")
    print(f"Your total score is: {player_scores[player_no]}")
    current_score = 0

    while True:
        should_roll = input("Would you like to roll (y)? ")
        if should_roll.lower() != "y":
            break

        value = roll()
        if value == 1:
            print("You rolled a 1! Turn done!")
            current_score = 0
            break
        else:
            current_score += value
            print(f"You rolled a {value}")

        print(f"Your current score is: {current_score}")

    player_scores[player_no] += current_score
    print(f"Your total score is: {player_scores[player_no]}")

def display_leaderboard(player_scores):
    """Display the current leaderboard based on player scores."""
    print("\n--- Leaderboard ---")
    sorted_scores = sorted(
        [(i + 1, score) for i, score in enumerate(player_scores)],
        key=lambda x: x[1],
        reverse=True,
    )
    for position, (player_no, score) in enumerate(sorted_scores, 1):
        print(f"{position}. Player {player_no} - {score} points")
    print("-------------------")

def main():
    """Main function to control the game flow"""
    # Get the number of players
    players = get_number_of_players()
    max_score = 50
    player_scores = [0 for _ in range(players)]

    # Continue the game until one or more players reach the maximum score
    while max(player_scores) < max_score:
        for player_no in range(players):
            play_turn(player_no, player_scores)
            display_leaderboard(player_scores)

    # Determine the highest score and identify the winners
    max_score = max(player_scores)
    winning_idx = [i + 1 for i, score in enumerate(player_scores) if score == max_score]
    if len(winning_idx) > 1:
        print(
            f"\nIt's a tie between players: {', '.join(map(str, winning_idx))} with {max_score} points"
        )
    else:
        print(f"\nPlayer number {winning_idx[0]} is the winner with {max_score} points")

if __name__ == "__main__":
    main()


# Create a rock, paper, scissors game
# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.

# The computer will be the opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent
# By the end of each round, the player can choose whether to play again
# Display the player's score at the end of the game
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid
# The game must handle the player's choice, the computer's choice, and the result of the round

import random

def rock_paper_scissors():
    print("Welcome to the Rock, Paper, Scissors game!")
    player_score = 0
    computer_score = 0
    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid option. Please choose rock, paper, or scissors.")
        else:
            print(f"Player: {player_choice}")
            print(f"Computer: {computer_choice}")
            if player_choice == computer_choice:
                print("It's a tie!")
            elif player_choice == "rock":
                if computer_choice == "scissors":
                    print("Player wins!")
                    player_score += 1
                else:
                    print("Computer wins!")
                    computer_score += 1
            elif player_choice == "scissors":
                if computer_choice == "paper":
                    print("Player wins!")
                    player_score += 1
                else:
                    print("Computer wins!")
                    computer_score += 1
            elif player_choice == "paper":
                if computer_choice == "rock":
                    print("Player wins!")
                    player_score += 1
                else:
                    print("Computer wins!")
                    computer_score += 1
            print(f"Player score: {player_score}")
            print(f"Computer score: {computer_score}")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing!")
                break

rock_paper_scissors()
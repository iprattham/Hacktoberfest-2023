# Python Program for Rock-Paper-Scissors Game
import random

# Function to determine the winner for a single round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to display the user's and computer's choices
def display_choices(user_choice, computer_choice):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("Rock, Paper, or Scissors?")
        user_choice = input("Enter your choice: ").lower()

        if user_choice not in ("rock", "paper", "scissors"):
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])

        display_choices(user_choice, computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing!")
            break

# Start the game
play_game()

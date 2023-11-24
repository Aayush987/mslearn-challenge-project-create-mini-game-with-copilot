# create a rock,paper,scissors game where the user plays against the computer
# user will enter their choice through input and will show invalid if they enter something other than rock,paper,scissors
# computer will randomly generate a choice and will compare it to the user's choice to declare a win.lose or tie.
# user will be asked if they want to play again and will be taken back to the beginning if they say yes
# if they say no, the game will end
# user will be able to see their score and the computer's score when they will choose to end the game

import random   
import sys

print("Welcome to Rock, Paper, Scissors!")

user_score = 0
comp_score = 0

while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)
    if user_choice in possible_choices:
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")

    # check if the user choice is invalid display error mesaage
    elif user_choice not in possible_choices:
        print("Invalid choice, please try again.")
        sys.exit()
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
            user_score += 1
        else:
            print("Paper covers rock! You lose.")
            comp_score += 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
            user_score += 1
        else:
            print("Scissors cuts paper! You lose.")
            comp_score += 1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
            user_score += 1
        else:
            print("Rock smashes scissors! You lose.")
            comp_score += 1
    print(f"\nPlayer Score: {user_score}\nComputer Score: {comp_score}\n")
    user_choice = input("Would you like to play again? (y/n): ")
    if user_choice != "y":
        break

print("Thanks for playing!")
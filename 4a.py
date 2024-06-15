'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import random

def get_user_choice():
    while True:
        choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
        if choice in ('rock', 'paper', 'scissors'):
            return choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0
   
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
       
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
       
        result = determine_winner(user_choice, computer_choice)
        print(result)
       
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
       
        print(f"\nYour score: {user_score}")
        print(f"Computer's score: {computer_score}")
       
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()




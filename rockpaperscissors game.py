# rockpaperscissors game.py

import random  

print("Welcome to Rock, Paper, Scissors!")  
print("=" * 50)  
print("Starting the game...")  
print("=" * 50)  

def get_computer_choice():  
    choices = ['rock', 'paper', 'scissors']  
    return random.choice(choices)  

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    global winning_count, losing_count, tie_count
    
    if user_choice == computer_choice:
        tie_count += 1
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        winning_count += 1
        return "You win!"
    else:
        losing_count += 1
        return "Computer wins!"

# Initialize counters
winning_count = 0  
losing_count = 0  
tie_count = 0

# Main game loop
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    print(f"\nScore - Wins: {winning_count}, Losses: {losing_count}, Ties: {tie_count}")
    
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
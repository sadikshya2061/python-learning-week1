# random number guessing game with emojis and hints when user is close to the number is guessed

import random

print("Welcome to the ULTIMATE Guessing Game!")
print("I'm thinking of a number between 1 and 100")

print("Starting the game...")
print("=" * 50)

# STEP 1: Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
guess_count = 0
previous_guess = None

print(" Hint: The number is between 1 and 100")
print("-" * 30)

# STEP 2: Game loop
while True:
    # STEP 3: Get user input with error handling
    try:
        guess = int(input(" Make a guess: "))
        guess_count += 1
        
        # Check if guess is out of range
        if guess < 1 or guess > 100:
            print(" Please enter a number between 1 and 100!")
            guess_count -= 1  # Don't count invalid guesses
            continue
        
        # Check if it's the same as previous guess
        if guess == previous_guess:
            print(" You just tried that number! Try a different one.")
            guess_count -= 1
            continue
        
        previous_guess = guess  # Remember this guess for next time
        
        # Give feedback with emojis and distance hints
        difference = abs(guess - secret_number)
        
        if guess < secret_number:
            if difference <= 5:
                print(" So close! Just a bit higher! ")
            elif difference <= 15:
                print(" Too low! Getting warmer... ")
            else:
                print(" Too low! Brrr... it's cold!")
                
        elif guess > secret_number:
            if difference <= 5:
                print(" So close! Just a bit lower! ")
            elif difference <= 15:
                print(" Too high! Getting warmer... ")
            else:
                print(" Too high! Way too high! ")
        else:
            # WINNER!
            print("=" * 50)
            print(f" CONGRATULATIONS! YOU WON! ")
            print(f" The number was {secret_number}")
            print(f" Number of attempts: {guess_count}")
            
            # Performance rating
            if guess_count <= 5:
                rating = " EXPERT LEVEL! Amazing!"
            elif guess_count <= 10:
                rating = " GREAT JOB! Very impressive!"
            elif guess_count <= 15:
                rating = " GOOD WORK! Well played!"
            else:
                rating = "You got there! Persistence pays off!"
            
            print(f" Performance: {rating}")
            print("=" * 50)
            break
        
        # Show progress every few guesses
        if guess_count % 5 == 0:
            print(f" You've made {guess_count} guesses so far...")
            
        # Give a hint after 10 wrong guesses
        if guess_count == 10:
            if secret_number % 2 == 0:
                print(" Hint: The number is EVEN")
            else:
                print(" Hint: The number is ODD")
                
        # Give another hint after 15 wrong guesses  
        if guess_count == 15:
            if secret_number < 50:
                print(" Hint: The number is less than 50")
            else:
                print(" Hint: The number is 50 or greater")
        
    except ValueError:
        print(" Please enter a valid number (1-100)!")
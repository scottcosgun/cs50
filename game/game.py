import random

while True:
    try:
        # Get user input
        level = int(input("Level: "))
        # If user inputs a positive int, break the loop
        if level > 0:
            break
    # If not an int, prompt again
    except ValueError:
        pass

# Generate a random int from 1 to "level"
num = random.randint(1, level)

# Initialize variable for user's guess
guess = 0

# Continuously prompt user to guess the number
while True:
    try:
        # Prompt user to guess
        guess = int(input("Guess: "))
        if guess > num:
            print("Too large!")
        elif guess < num:
            print("Too small!")
        # If user guesses number, break loop and exit
        else:
            print("Just right!")
            break
    # Ignore non-int guesses
    except ValueError:
        pass
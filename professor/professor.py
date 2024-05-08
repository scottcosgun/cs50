import random

def main():
    # Prompt user for level
    level = get_level()

    # Initialize variable for score
    score = 0

    # Generate 10 math problems user must solve
    for i in range(10):
        # Generate equation
        x, y = generate_integer(level)
        z = x + y
        tries = 0
        # Give user 3 tries to solve math problem
        while tries < 3:
            try:
                # Prompt user to solve math problem
                answer = int(input(f"{x} + {y} = "))
                # If correct, add to score and move on
                if answer == z:
                    score += 1
                    break
            except ValueError:
                pass

            # If incorrect, print EEE and add to # tries
            print("EEE")
            tries += 1

        # If user tries 3 times, output correct answer
        if tries == 3:
            print(f"{x} + {y} = {z}")

    # Print out user's score
    print(f"Score: {score}")

def get_level():
    # Prompt user for level
    while True:
        try:
            level = int(input("Level: "))
            # Ensure level is 1, 2, or 3
            if level in [1, 2, 3]:
                break
        # If not an int, prompt again
        except ValueError:
            pass

    return level

def generate_integer(level):
    # Generate a math problem. Ints must have n = level digits
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError

    return x, y

if __name__ == "__main__":
    main()
from PyDictionary import PyDictionary
import sys
import random
import cowsay

dictionary=PyDictionary()

def main():
    while True:
        level = get_level()
        word = get_word(level)
        scrambled = scramble(word)
        play(word, scrambled)
        print(get_def(word), "\n")
        try_again()

def get_level():
    # Continue to prompt user until they input an int or quit
    while True:
        try:
            # Level corresponds to number of characters in word
            return int(input("Level: "))
        # Handle exception in case input is not an int
        except ValueError:
            # Prompt the user to try again or quit
            if input("Level must be an int. Try again? y/n ").lower().strip() in ["n", "no"]:
                sys.exit("Ok, goodbye.")

def get_word(n):
    words_list = []
    # Open English words list
    with open("words.txt") as file:
        # Iterate through each word and select those with n letters
        for word in file:
            # n + 1 since each word has \n
            if len(word) == n + 1:
                # Add word to list, stripped of \n
                words_list.append(word.strip())
    # Generate a random int to index into the words list and return the word at that location
    index = random.randrange(0, len(words_list))
    return words_list[index]

def scramble(word):
    # Convert word str to list
    word = list(word)
    # Shuffle the chars in the word
    random.shuffle(word)
    # Return scrambled word as a str
    return ''.join(word)

def play(word, scrambled):
    tries = 0
    # Print out scrambled word
    print(f"Scrambled word: {scrambled}")
    print("You have 3 tries to guess the unscrambled word")
    # Allow the user 3 tries to guess the word
    while tries < 3:
        if input(f"Guess {tries + 1}: ").lower().strip() != word:
            if tries < 2:
                print("Try again!")
            tries += 1
        else:
            cowsay.cow("Correct!")
            break
    if tries == 3:
        print(f"\nSorry! The correct word is {word}.\n")

def get_def(word):
    return dictionary.meaning(word)

def try_again():
    if input("Try again? y/n ").strip().lower() not in ["y", "yes"]:
        sys.exit("Ok, goodbye!")

if __name__ == "__main__":
    main()
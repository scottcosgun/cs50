def main():
    # Prompt user for string
    word = input("Input: ")
    print("Output: ", end="")
    print(shorten(word))

def shorten(word):
    # Store vowels in a dict
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Initialize new word
    new_word = ""
    # Iterate over letters in text
    for letter in word:
        # Add all non-vowels to new word
        if letter.lower() not in vowels:
            new_word += letter
    return new_word

if __name__ == "__main__":
    main()
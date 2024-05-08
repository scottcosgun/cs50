# **Word Scramble**
### Video Demo:  <https://www.youtube.com/watch?v=yjki-9Pthh0>
### **Description:**

Word scramble is an fun, interactive word game. The program takes an English word and scrambles the letters around, and the user must guess what the unscrambled version of the word is in 3 tries or less.

### **words.txt**

words.txt is a text file containing 10,000 common English words. The game referenes this file in selecting a word to scramble.

### **Usage**

```
python project.py
```

Upon running python project.py, the program will prompt the user to choose a level, an int corresponding to the number of characters that will be in the scrambled word. Ex: Level 6 will scramble a 6 letter word for the user to guess.

Upon level selection, the program alerts the user that they will have 3 tries to guess the word correctly, and will present the scrambled word.

If the user guesses the word correctly within 3 tries, a cow will appear on the screen and say "Correct!" Otherwise, no such cow will appear on the screen

Once 3 tries are up OR the user guesses the word correctly, the program will print out the definition of the word.

Afterwards, the user is prompted to input whether they would like to play again or not. Anything that's not "y" or "yes" (case insensitively) will be considered a "no", and the program will quit. If the user inputs "y" or "yes", then the game starts over again with level selection.

## **Functions**

Several functions have been defined to implement this game:

### **main()**

```
def main():
    while True:
        level = get_level()
        word = get_word(level)
        scrambled = scramble(word)
        play(word, scrambled)
        print(get_def(word), "\n")
        try_again()
```

### **get_level()**

Prompts the user to choose a level, corresponding to the number of characters. Input must be an int. If not, this function will continuously prompt the user to input an int or quit.
Returns an int corresponding to the level

### **get_word(n)**

Takes an int, n, and generates a list of words from words.txt that have exactly n characters. The function then returns a random word from the list.

### **scramble(word)**

Takes a str, word, and returns that word with the letters rearranged, or scrambled.

### **play(word, scrambled)**

Takes two strs as input: The scrambled word and the original word. This function prints out the scrambled word and allows the user 3 tries to guess it correctly. If the user guesses the word, a cow will exclaim "Correct!" If the user does not guess the word after 3 tries, the function will show the user the correct word.

### **get_def(word)**

Returns the dictionary definition of word

### **try_again()**

Prompts the user to input whether they would like to try again or not. If the input is not "y" or "yes", quit the game.

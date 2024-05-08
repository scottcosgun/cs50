from cs50 import get_string

# Prompt user for text
text = get_string("Text: ")

# Initialize variables
num_letters = 0
num_words = 1
num_sentences = 0
# Iterate through each character in text
for i in range(len(text)):
    if text[i].isalpha():
        num_letters += 1
    elif text[i] == " ":
        num_words += 1
    elif text[i] == "." or text[i] == "!" or text[i] == "?":
        num_sentences += 1

# Calculate average number of letters per 100 words
L = (num_letters * 100) / num_words

# Calculate average number of sentences per 100 words
S = (num_sentences * 100) / num_words

# Calculate Coleman-Liau index
index = 0.0588 * L - 0.296 * S - 15.8
# Round index to nearest int
grade = round(index)

# Check if index < 1
if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")
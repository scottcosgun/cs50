# Import modules
import emoji
import sys

# Input text from user
text = input("Input: ")

# Convert text to emoji
emojized = emoji.emojize(text)

# Print output
print("Output: ", emojized)